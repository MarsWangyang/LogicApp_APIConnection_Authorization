# Executable File

> You can directly execute Windows or MacOS application locally after add `.env` file.
> <br>
> You must have <a href="https://www.google.com/chrome/downloads/">Chrome</a> browser first! <src>

## Mac OS version

**_Service Principal_**
How to use: <br>

0. add file `MacOS Executable Folder/Resources/.env`
1. revise `.env` file to changet to your service princial info and save it
   ```
   TENANT_ID=XXXXXXXX
   CLIENT_ID=XXXXXXXX
   CLIENT_SECRET=XXXXXXXX
   SUBSCRIPTION_ID=XXXXXXXX
   OBJECT_ID=XXXXXXX
   ```
2. Click to open `MacOS Executable Folder/MacOS/main` to run your app
   ```bash
   $open /MacOS/main
   ```

## Windwos Version

**_Service Principal_**
How to use: <br>

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
if `/MacOS Executable Folder` can't run, please go to `/MacOS`, adding `.env` file include your service prinicpal credential, and `pip install py2app` in your environment and run script below

```bash
$ python setup.py py2app -A # rebuild your application
```

or follow this reference: https://zhuanlan.zhihu.com/p/454550005 from zhihu by @风影忍着
