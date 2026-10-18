# Solutions

## Question 1. Redpanda version

```bash
docker exec -it workshop-redpanda-1 rpk version
```

Answer: `v25.3.9` (matches the image tag in docker-compose.yml)


## Question 2. Sending data to Redpanda

Create the topic:

```bash
docker exec -it workshop-redpanda-1 rpk topic create green-trips
```

Run the producer:

```bash
python producer.py
```

The dataset has 49,416 rows. Sending takes roughly 10 seconds depending
on the machine.

Answer: 10 seconds


## Question 3. Consumer - trip distance

Run the consumer:

```bash
python consumer.py
```

Answer: 8506 trips have `trip_distance` > 5.0


## Question 4. Tumbling window - pickup location

Create the PostgreSQL table:

```sql
CREATE TABLE tumbling_pickup_counts (
    window_start TIMESTAMP(3),
    PULocationID INT,
    num_trips BIGINT,
    PRIMARY KEY (window_start, PULocationID) NOT ENFORCED
);
```

Copy `tumbling_job.py` to `07-streaming/workshop/src/job/` and run:

```bash
docker exec -it workshop-jobmanager-1 \
    flink run -py /opt/src/job/tumbling_job.py
```

Query results:

```sql
SELECT PULocationID, num_trips
FROM tumbling_pickup_counts
ORDER BY num_trips DESC
LIMIT 3;
```

Answer: PULocationID 74 (with 15 trips in the busiest 5-minute window)


## Question 5. Session window - longest streak

Create the PostgreSQL table:

```sql
CREATE TABLE session_pickup_counts (
    session_start TIMESTAMP(3),
    session_end TIMESTAMP(3),
    PULocationID INT,
    num_trips BIGINT,
    PRIMARY KEY (session_start, PULocationID) NOT ENFORCED
);
```

Copy `session_job.py` to `07-streaming/workshop/src/job/` and run:

```bash
docker exec -it workshop-jobmanager-1 \
    flink run -py /opt/src/job/session_job.py
```

Query results:

```sql
SELECT PULocationID, num_trips, session_start, session_end
FROM session_pickup_counts
ORDER BY num_trips DESC
LIMIT 3;
```

Answer: 81 trips (PULocationID 74, session on 2025-10-08 morning)

Note: the session job must use parallelism 1, since the `green-trips`
topic has only 1 partition. With higher parallelism, idle subtasks
prevent the watermark from advancing and session windows won't emit.


## Question 6. Tumbling window - largest tip

Create the PostgreSQL table:

```sql
CREATE TABLE hourly_tips (
    window_start TIMESTAMP(3),
    total_tips DOUBLE,
    PRIMARY KEY (window_start) NOT ENFORCED
);
```

Copy `tip_job.py` to `07-streaming/workshop/src/job/` and run:

```bash
docker exec -it workshop-jobmanager-1 \
    flink run -py /opt/src/job/tip_job.py
```

Query results:

```sql
SELECT window_start, total_tips
FROM hourly_tips
ORDER BY total_tips DESC
LIMIT 3;
```

Answer: 2025-10-16 18:00:00 (total tips: ~$524.96)
