## Create python virtual environment
```
python -m venv dbt-env
```

## How to activate in gitBash
```
. dbt-env/Scripts/activate
```
## How to activate in powershell and cmd
```
 dbt-env/Scripts/activate.bat //In CMD
dbt-env/Scripts/Activate.ps1 //In Powershel
```
## Installing dbt-postgres
Use pip to install the adapter, which automatically installs dbt-core and any additional dependencies. Use the following command for installation:
```
pip install dbt-postgres
```
## Profile Configuration
Postgres targets should be set up using the following configuration in your profiles.yml file.
This file should in main ~ default folder. in my case, it was user folder.  ```C:\Users\vighn\.dbt\profiles.yml```
```
dbt_project:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      user: root
      password: root
      port: 5432
      dbname: ny_taxi # or database instead of dbname
      schema: public
      threads: 1
      keepalives_idle: 30 # default 0, indicating the system default.
```
## create new project using above profile
```
dbt init --profile profilename projectname
```

      
