from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("MinIOETLJob").getOrCreate()

spark.conf.set("fs.s3a.endpoint", "http://minio:9000")
spark.conf.set("fs.s3a.access.key", "minioadmin")
spark.conf.set("fs.s3a.secret.key", "minioadmin")
spark.conf.set("fs.s3a.path.style.access", "true")

df = spark.createDataFrame([(1, "foo"), (2, "bar")], ["id", "value"])
df.write.mode("overwrite").parquet("s3a://raw/sample_etl_output/")
spark.stop()
