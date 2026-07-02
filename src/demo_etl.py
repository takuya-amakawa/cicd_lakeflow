# Databricks notebook source
# MAGIC %md
# MAGIC # demo_etl — DAB CI/CD デモ
# MAGIC
# MAGIC 取引データを金額区分ごとに集計する最小の ETL。
# MAGIC ロジック本体は `lib/transforms.py` にあり、CI（pytest）でユニットテスト済みのものだけがここに届く。

# COMMAND ----------

import os
import sys

# バンドルは lib/ ごとワークスペースに同期されるため、相対パスで import できる
sys.path.append(os.path.abspath("../lib"))
from transforms import categorize_amount

# COMMAND ----------

from pyspark.sql import functions as F
from pyspark.sql.types import StringType

tx = [
    ("t-0001", 120),
    ("t-0002", 5_400),
    ("t-0003", 89_000),
    ("t-0004", 700),
    ("t-0005", 32_000),
    ("t-0006", 150_000),
]
df = spark.createDataFrame(tx, ["tx_id", "amount"])

categorize_udf = F.udf(categorize_amount, StringType())
result = (
    df.withColumn("category", categorize_udf("amount"))
    .groupBy("category")
    .agg(F.count("*").alias("tx_count"), F.sum("amount").alias("total_amount"))
    .orderBy("category")
)
result.show()
