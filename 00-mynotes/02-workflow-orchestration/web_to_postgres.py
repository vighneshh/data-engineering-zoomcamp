
# # For Workflow 
from prefect import flow, task

# for extract
import platform
import os

# import io
import requests

import pandas as pd

from sqlalchemy import create_engine



@task
def load_data(trans_df,user, password, host, port,db, table_name):
    ''' Loading Data into Postgres  '''
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')


    trans_df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    trans_df.to_sql(name=table_name, con=engine, if_exists='append')

    

@flow
def extract_data(url,year, service):
    ''' Extracting Data from web '''
    for i in range(12):
        
        # sets the month part of the file_name string
        month = '0'+str(i+1)
        month = month[-2:]

        # csv file_name
        file_name = f"{service}_tripdata_{year}-{month}.csv.gz"

        # download it using requests via a pandas df
        request_url = f"{url}{service}/{file_name}"
        r = requests.get(request_url)
        open(file_name, 'wb').write(r.content)
        print(f"Local: {file_name}")

        # read it back into a parquet file
        df = pd.read_csv(file_name, compression='gzip')
        file_name = file_name.replace('.csv.gz', '.parquet')
        df.to_parquet(file_name, engine='pyarrow')
        print(f"Parquet: {file_name}")


        # upload it to postgres
        print(f"Postgres: {service}/{file_name}")

        load_data(df,user, password, host, port,db, table_name)
    








@flow
def main_etl_flow(url,user, password, host, port,db, table_name,year, service):
    df = extract_data(url,year, service)
    # trans_df = transform_data(df)
    # load_data(trans_df,user, password, host, port,db, table_name)
    

if __name__ == "__main__":
    user = 'root'
    password = 'root'
    host = 'localhost'
    port = 5432
    db = 'ny_taxi'
    table_name = 'green_taxi_trips'
    
    #url = 'https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'
    # url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-01.csv.gz'
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/'
    main_etl_flow(url,user, password, host, port,db, table_name,'2019', 'green')
    main_etl_flow(url,user, password, host, port,db, table_name,'2020', 'green')
    
    
    


    