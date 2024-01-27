## Create python virtual environment
```
python -m venv prefectvenv
```

## How to activate in gitBash
```
. prefectvenv/Scripts/activate
```
## How to activate in powershell and cmd
```
 prefectvenv/Scripts/activate.bat //In CMD
 prefectvenv/Scripts/Activate.ps1 //In Powershel
```
## To start local prefect instance
 ```
 prefect server start
```
## To create deployment file to deploy flow to server
```
prefect deployment build hello-prefect.py:hello_world -n firstdeployment
```
## Deploy flow to server
```
prefect deployment apply hello_world-deployment.yaml
```
## To start agent so you can run flow from prefect server
```
prefect agent start -q 'default'
```
## Login into Preset login (not working)
```
prefect cloud login
```



