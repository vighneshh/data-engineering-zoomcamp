
# # For Workflow 
from prefect import flow, task

# for extract
import platform
import os

import pandas as pd

from sqlalchemy import create_engine


@task
def extract_data(url):
    ''' Extracting Data from web '''
    if url.endswith('.csv.gz'):
        csv_name = 'green_tripdata_2020-01.csv.gz'
    else:
        csv_name = 'output.csv'

    if platform.uname().system == 'Windows':
        os.system(f"curl -L {url} -o {csv_name}")
        # curl -L https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-09.csv.gz -o output.csv.gz
    else:
        os.system(f"wget {url} -O {csv_name}")

    if url.endswith('.csv.gz'):
        df = pd.read_csv(csv_name, compression='gzip')
    else:
        df = pd.read_csv(csv_name)

    

    print(len(df.index))
    print(csv_name)
    return df


@task
def transform_data(trans_df):
    ''' Transforming Data  '''
    trans_df.lpep_pickup_datetime = pd.to_datetime(trans_df.lpep_pickup_datetime)
    trans_df.lpep_dropoff_datetime = pd.to_datetime(trans_df.lpep_dropoff_datetime)

    print(f"Transforming data{len(trans_df.index)}")
    return trans_df


@task
def load_data(trans_df,user, password, host, port,db, table_name):
    ''' Loading Data into Postgres  '''
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')


    trans_df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    trans_df.to_sql(name=table_name, con=engine, if_exists='append')


@flow
def main_etl_flow(url,user, password, host, port,db, table_name):
    df = extract_data(url)
    trans_df = transform_data(df)
    load_data(trans_df,user, password, host, port,db, table_name)
    

if __name__ == "__main__":
    user = 'root'
    password = 'root'
    host = 'localhost'
    port = 5432
    db = 'ny_taxi'
    table_name = 'green_taxi_trips'
    
    #url = 'https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-01.csv.gz'
    main_etl_flow(url,user, password, host, port,db, table_name)
    
    
    


    
