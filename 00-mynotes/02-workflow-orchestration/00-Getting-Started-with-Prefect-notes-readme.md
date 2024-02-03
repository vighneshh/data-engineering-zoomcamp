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
## Install perfect 
```
pip install -U prefect
```
## Check if installation is right
```
prefect version
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
## Use this command to prefect command using api key
``` 
prefect cloud login --key pnu_0sPiIMkgF2kMdBG4av9hDXAQB7Ljd84eKtj1 --workspace vighneshgawad/default
```

## Run apply command again so cloud can pick up
```
prefect deployment apply hello_world-deployment.yaml
```
## Run agent again so cloud can pick up
```
prefect agent start -q 'default'
```

## deploy code on github and create github block so deployment can take code from github repo but you still need to run agent on local
```
prefect deployment build hello-prefect.py:hello_world --name second-deployment --tag dev -sb github/github-helloworld -a
```
## To change instance of Deployment server. Need to change ENV Variables
```
prefect config view
prefect config set PREFECT_API_URL="http://127.0.0.1:4200/api"
```



