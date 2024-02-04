
# # For Workflow 
from prefect import flow, task

# for extract
import platform
import os

import pandas as pd


import pandas_gbq

# TODO: Get Key from creating service account 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'bqadmin_key.json'

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


task
def load_data(trans_df,project_id, table_id):
    ''' Loading Data into Big Query  '''
    print("Loading data into Big Query")
    pandas_gbq.to_gbq(trans_df, table_id, project_id=project_id)



@flow
def main_etl_flow(url,project_id, table_id):
    df = extract_data(url)
    trans_df = transform_data(df)
    load_data(trans_df,project_id, table_id)
    

if __name__ == "__main__":
    project_id = "dataengzoomcamp-413305"
    table_id = 'ny_taxi.greentaxibq'
    
    #url = 'https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv'
    url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-01.csv.gz'
    main_etl_flow(url,project_id, table_id)
    
    
    


    
