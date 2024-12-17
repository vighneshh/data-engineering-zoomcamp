import os
import snowflake.connector

# Snowflake connection parameters
SNOWFLAKE_ACCOUNT = "ncoprzj-vbb49474"  # E.g., 'abc123.snowflakecomputing.com'
SNOWFLAKE_USER = "Vighnesh"
SNOWFLAKE_PASSWORD = "Meguri@20242024"
SNOWFLAKE_DATABASE = "thelook_ecommerce"
SNOWFLAKE_SCHEMA = "PUBLIC"
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_STAGE = "CSV_FILES"  # Snowflake stage for staging files

csv_directory = 'data';

# List of CSV file names
# table_names = [
#     "products.csv"
    # "events.csv",
# ]
table_names = [
    "distribution_centers.csv",
    "inventory_items.csv",
    "order_items.csv",
    "orders.csv",
    "products.csv",
    "users.csv"
]

# Connect to Snowflake
conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA,
)
cursor = conn.cursor()

# Iterate through each CSV file
for file_name in table_names:
    try:
        
         # Construct the full file path
        file_path = csv_directory + '/'+ file_name

        # Extract table name without the `.csv` extension
        table_name = file_name.split('.')[0]

        # print(file_path);

        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue
        else:
            print(file_name);
            # Upload the CSV file to Snowflake stage
            put_command = f"PUT 'file://{file_path}' @{SNOWFLAKE_STAGE} auto_compress=false"
            cursor.execute(put_command)
            print(f"File {file_name} staged successfully.")


             # Load data into the Snowflake table
            copy_command = f"""
            COPY INTO {table_name}
            FROM @{SNOWFLAKE_STAGE}/{file_name}
            file_format =(format_name = csv_format);
            """
            cursor.execute(copy_command)
            print(f"Table {table_name} loaded successfully.")
           


    except Exception as e:
        print(f"Error processing {file_name}: {e}")

# Close the cursor and connection
cursor.close()
conn.close()
