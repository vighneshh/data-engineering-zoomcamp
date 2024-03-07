import pandas_gbq

import os
from tqdm import tqdm

# TODO: Get Key from creating service account 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'bqadmin_key.json'

# TODO: Set project_id to your Google Cloud Platform project ID.

project_id = 'dataengzoomcamp-413305'


table_names =['bikeshare_regions','bikeshare_station_info','bikeshare_station_status','bikeshare_trips']


# sql = """
# SELECT * 
# FROM `bigquery-public-data.san_francisco_bikeshare.bikeshare_regions`
# """
# # df = pandas_gbq.read_gbq(sql, project_id=project_id,progress_bar_type=None)
# df = pandas_gbq.read_gbq(sql, project_id=project_id)

# df.to_csv (r'bikeshare_regions.csv', index = None, header=True)
# print(df)


for table_name in table_names:
    # Set your BigQuery SQL query for the current table
    sql = f"""
    SELECT * 
    FROM `bigquery-public-data.san_francisco_bikeshare.{table_name}`
    """
    
    # Read data from BigQuery into a DataFrame
    df = pandas_gbq.read_gbq(sql, project_id=project_id)
    
    # Set the path where you want to save the CSV file
    csv_file_path = f'{table_name}.csv'
    
    print(df)

    # Write the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False, header=True)



