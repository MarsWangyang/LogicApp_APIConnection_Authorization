# Import the required libraries
from http.server import executable
import os
import undetected_chromedriver as uc
import adal
from decouple import config, Config, RepositoryEnv
import time
import requests as rq

DOTENV_FILE = os.path.join(os.getcwd(), ".env")
env_config = Config(RepositoryEnv(DOTENV_FILE))

# Tenant ID for your Azure Subscription
TENANT_ID = config('TENANT_ID')
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
SUBSCRIPTION_ID = config('SUBSCRIPTION_ID')
OBJECT_ID = config('OBJECT_ID')


def getBearerToken():
    # generate your bearer token to access Azure resource
    authority_url = 'https://login.microsoftonline.com/'+TENANT_ID
    context = adal.AuthenticationContext(authority_url)
    token = context.acquire_token_with_client_credentials(
        resource='https://management.azure.com/',
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )
    bearerToken = token['accessToken']
    return bearerToken


def getAuthLink(bearerToken: str):
    # POST url
    post_url = f"https://management.azure.com/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{rg_name}/providers/Microsoft.Web/connections/{connection_name}/listConsentLinks"
    # your request body for POST url
    request_body = {
        "parameters": [
            {
                "objectId": OBJECT_ID,
                "parameterName": "token",
                "redirectUrl": "https://ema1.exp.azure.com/ema/default/authredirect",
                "tenantId": TENANT_ID
            }
        ]
    }
    headers = {
        "Authorization": f"Bearer {bearerToken}",
        "Content-Type": "application/json"
    }
    params = {
        "api-version": '2018-07-01-preview'
    }
    auth_link = ''
    consent_link = rq.post(post_url, params=params, headers=headers,
                           json=request_body).json()
    for connectionAPI in consent_link['value']:
        if connectionAPI['status'] != "Authenticated":
            auth_link = connectionAPI['link']
    return auth_link


def getConsentCode(redirect_url: str):
    code = redirect_url.split('=')[1]
    return code


def confirmConsentCode(code: str, bearerToken: str):
    # post url for confirm consent code
    post_url = f"https://management.azure.com/subscriptions/{SUBSCRIPTION_ID}/resourceGroups/{rg_name}/providers/Microsoft.Web/connections/{connection_name}/confirmConsentCode"
    # your request body for POST url
    request_body = {
        "objectId": OBJECT_ID,
        "code": code,
        "tenantId": TENANT_ID
    }

    headers = {
        "Authorization": f"Bearer {bearerToken}",
        "Content-Type": "application/json"
    }
    params = {
        "api-version": '2018-07-01-preview'
    }
    confirm_request = rq.post(post_url, params=params,
                              headers=headers, json=request_body)
    return confirm_request.status_code


if __name__ == '__main__':
    # your resource group name
    rg_name = str(input("Enter your resource group name:"))
    # your connection name
    connection_name = str(input("Enter your connection name:"))
    bearerToken = getBearerToken()
    auth_link = getAuthLink(bearerToken)
    driver = uc.Chrome(use_subprocess=True)
    driver.get(auth_link)
    redirect_url_prefix = "https://ema1.exp.azure.com/ema"
    redirect_url = ''
    while driver.current_url:
        time.sleep(5)
        if str(driver.current_url).startswith(redirect_url_prefix):
            redirect_url = driver.current_url
            break
    consentCode = getConsentCode(redirect_url)
    if (confirmConsentCode(consentCode, bearerToken) == 200):
        print("Successfully Connected")
    else:
        print("Staus: Error, Please revalidate your credential.")
