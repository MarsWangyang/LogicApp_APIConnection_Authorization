# API Connection Auto Authentication

> You can directly execute Windows or MacOS code locally after add `.env` file.
> <br>
> You must have <a href="https://www.google.com/chrome/downloads/">Chrome</a> browser first! <src>

Before you start using it, clone this repository and choose what OS you use.

For Example (MacOS):

```sh
git clone https://github.com/MarsWangyang/LogicApp_APIConnection_Authorization.git
cd MacOS/
python3 -m venv .venv # create a virtual environment
source .venv/bin/activate # launch your virtual environment
pip install -r requirements.txt
```

## Mac OS version

**_Service Principal_</a>**

> An Azure service principal is an identity created for use with applications, hosted services, and automated tools to access Azure resources. This access is restricted by the roles assigned to the service principal, giving you control over which resources can be accessed and at which level

Before using it, I choose Service Principal to implement this authentication.
How to create a service principal? Check <a href="https://learn.microsoft.com/en-us/powershell/azure/create-azure-service-principal-azureps?view=azps-8.3.0">here</a>

### How to use: <br>

0. copy the information of the service principal you just created.
1. add file `.env`
2. revise `.env` file to changet to your service princial info and save it
   ```
   TENANT_ID=XXXXXXXX
   CLIENT_ID=XXXXXXXX
   CLIENT_SECRET=XXXXXXXX
   SUBSCRIPTION_ID=XXXXXXXX
   OBJECT_ID=XXXXXXX
   ```
3. open `main.py` and press F5 to run the code.
4. Enter the information of your API connection.
5. Done!

## Windwos Version

**_Service Principal_**

### How to use: <br>

0. add file `Windows Executable Folder/.env`
1. revise `.env` file to changet to your service princial info and save it
   ```
   TENANT_ID=XXXXXXXX
   CLIENT_ID=XXXXXXXX
   CLIENT_SECRET=XXXXXXXX
   SUBSCRIPTION_ID=XXXXXXXX
   OBJECT_ID=XXXXXXX
   ```
2. **Double click** to open `/Windows Executable Folder/main.exe` to run your app

## Troubleshooting

**For MacOS version:** <br>

### How to pack MacOS/ code to excutable file (.app)?

please go to `/MacOS`, adding `.env` file include your service prinicpal credential, and `pip install py2app` in your environment and run script below

```bash
$ python setup.py py2app -A # rebuild your application
```

or follow this reference: https://zhuanlan.zhihu.com/p/454550005 from zhihu by @风影忍着
