# Data Engineering Framework

This project provides a complete Data Engineering framework using modern data stack tools, including PySpark for distributed data processing, MinIO as a cloud-native data lake storage solution, dbt for structured data transformations, and Docker for easy deployment.

## 🚀 Technologies

- **PySpark:** Powerful distributed data ingestion, transformation, and processing.
- **dbt:** Enables modular and maintainable data transformations via SQL.
- **MinIO:** High-performance, distributed object storage compatible with AWS S3.
- **Docker & Docker Compose:** Containerizes all services for seamless local deployment.

## 📌 Project Structure

```
data-eng-framework/
├── docker-compose.yml
├── spark/
│   ├── Dockerfile
│   └── scripts/
│       └── etl_job.py
├── dbt/
│   └── data_eng_dbt_project/
│       ├── models/
│       └── profiles.yml
└── data/
```

## 🚀 Technology Stack

- **Spark:** bitnami/spark (Master/Worker)
- **Spark Thrift Server:** apache/spark
- **dbt:** dbt-core with dbt-spark adapter
- **MinIO:** Object storage compatible with S3 API

## ⚙️ Getting Started

### Step 1: Launch the Environment

```bash
docker-compose up --build
```

### Step 2: Run PySpark Jobs

Run your PySpark jobs clearly from within the Spark container:

```bash
docker exec -it spark-master spark-submit --master spark://spark-master:7077 /opt/bitnami/spark/scripts/etl_job.py
```

### Step 2: Configure and Run dbt

Access dbt:

```bash
docker-compose run --rm dbt bash
```

Inside the dbt container:

```bash
cd data_eng_dbt_project
dbt debug
dbt run
```

### Step 3: Verify Data in MinIO

- Open MinIO UI: `http://localhost:9090`
- Username: `minioadmin`, Password: `minioadmin`
- Verify your datasets clearly in buckets (`raw`, `curated`, `aggregated`).

## ✅ Next Steps

- Integrate Apache Airflow for pipeline orchestration.
- Set up CI/CD with GitHub Actions for automatic builds and tests.
- Expand monitoring with tools like Prometheus and Grafana.

## 📚 Documentation

- [Apache Spark](https://spark.apache.org/)
- [dbt Documentation](https://docs.getdbt.com/)
- [MinIO Documentation](https://min.io/docs/minio/)
- [Docker Compose Docs](https://docs.docker.com/compose/)

---

Happy Data Engineering!

