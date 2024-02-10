# Notes from Build a Data Warehouse Using BigQuery Coursera Course
* [Course Link](https://www.coursera.org/learn/build-a-data-warehouse-using-bigquery)

  # Creating Datasets for Data Organization
* [Docs](https://cloud.google.com/bigquery/docs/datasets)
  There are different ways you can create dataset. either through UI Console, SQL, Python etc.

  SQL eg.
  ```
  CREATE SCHEMA `my-bi-project-406904.testdataset`
  OPTIONS (
    description = 'DESCRIPTION');
  ```

