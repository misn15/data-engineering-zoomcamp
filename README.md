# Week 3 HW

## BigQuery Setup
```sql
CREATE OR REPLACE EXTERNAL TABLE zoomcamp.external_yellow_tripdata
OPTIONS  (
  format = 'parquet',
  uris = ['gs://kestra-zoomcamp-nicole-demo/yellow_tripdata_2024-*.parquet']
);
```

```sql
CREATE OR REPLACE TABLE zoomcamp.yellow_tripdata_non_partitioned AS
SELECT * FROM zoomcamp.external_yellow_tripdata;
```

## Question 1
### Number of records is 20,332,093
`SELECT COUNT(*) FROM zoomcamp.external_yellow_tripdata;`

## Question 2
### Estimated to read 155.12 MB
```sql
SELECT DISTINCT PULocationID
FROM zoomcamp.yellow_tripdata_non_partitioned;
```

### Estimated to read 0 MB
```sql
SELECT DISTINCT PULocationID
FROM zoomcamp.external_yellow_tripdata;
```

## Question 3
```sql
SELECT DISTINCT PULocationID
FROM zoomcamp.yellow_tripdata_non_partitioned;
```

```sql
SELECT DISTINCT PULocationID, DOLocationID 
FROM zoomcamp.yellow_tripdata_non_partitioned;
```

## Question 4
### Returns 8,333 records
```sql
SELECT COUNT(*)
FROM zoomcamp.yellow_tripdata_non_partitioned
WHERE fare_amount = 0.0;
```

## Question 5 
```sql
CREATE OR REPLACE TABLE zoomcamp.yellow_tripdata_partitioned
PARTITION BY DATE(tpep_dropoff_datetime) 
CLUSTER BY VendorID AS
SELECT * FROM zoomcamp.external_yellow_tripdata;
```

## Question 6
### Estimated to read 26.84 MB
```sql
SELECT DISTINCT(VendorID) 
FROM zoomcamp.yellow_tripdata_partitioned
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
```

### Estimated to read 310.24MB
```sql
SELECT DISTINCT(VendorID) 
FROM zoomcamp.yellow_tripdata_non_partitioned
WHERE DATE(tpep_dropoff_datetime) BETWEEN '2024-03-01' AND '2024-03-15';
```

## Question 9
`SELECT count(*) From zoomcamp.yellow_tripdata_non_partitioned;`
