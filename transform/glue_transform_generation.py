# Glue job to transform raw ENTSO-E XML data into a structured format and save as Parquet files.

import sys

from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F


args = getResolvedOptions(
    sys.argv,
    [
        "JOB_NAME",
        "RAW_PATH",
        "OUTPUT_PATH",
    ],
)

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

job = Job(glueContext)
job.init(args["JOB_NAME"], args)

raw_path = args["RAW_PATH"]
output_path = args["OUTPUT_PATH"]

df = (
    spark.read
    .format("xml")
    .option("rowTag", "TimeSeries")
    .load(raw_path)
)

clean_df = df.select(
    F.col("mRID").cast("string").alias("timeseries_id"),
    F.col("businessType").alias("business_type"),
    F.col("curveType").alias("curve_type"),
    F.col("objectAggregation").alias("object_aggregation"),
    F.col("MktPSRType.psrType").alias("production_type"),
    F.col("`inBiddingZone_Domain.mRID`._VALUE").alias("in_domain_code"),
    F.col("`outBiddingZone_Domain.mRID`._VALUE").alias("out_domain_code"),
    F.col("`quantity_Measure_Unit.name`").alias("unit"),
    F.col("Period.timeInterval.start").alias("period_start"),
    F.col("Period.timeInterval.end").alias("period_end"),
    F.col("Period.resolution").alias("resolution"),
    F.explode(F.col("Period.Point")).alias("point")
)

final_df = clean_df.select(
    "timeseries_id",
    "business_type",
    "curve_type",
    "object_aggregation",
    "production_type",
    "in_domain_code",
    "out_domain_code",
    "unit",
    "period_start",
    "period_end",
    "resolution",
    F.col("point.position").cast("int").alias("position"),
    F.col("point.quantity").cast("double").alias("quantity"),
    F.current_timestamp().alias("ingestion_time")
)

final_df.show(20, truncate=False)

final_df.write.mode("overwrite").parquet(output_path)


# Entsoe Dayahead Price 
raw_df = (
    spark.read
    .format("xml")
    .option("rowTag", "TimeSeries")
    .load(raw_path)
)

cleaned_df = raw_df.select(
    F.col("mRID").cast("string").alias("timeseries_id"),
    F.col("businessType").alias("business_type"),
    F.col("curveType").alias("curve_type"),
    F.col("`in_Domain.mRID`._VALUE").alias("in_domain_code"),
    F.col("`out_Domain.mRID`._VALUE").alias("out_domain_code"),
    F.col("`currency_Unit.name`").alias("currency"),
    F.col("`price_Measure_Unit.name`").alias("price_unit"),
    F.col("Period.timeInterval.start").alias("period_start"),
    F.col("Period.timeInterval.end").alias("period_end"),
    F.col("Period.resolution").alias("resolution"),
    F.explode(F.col("Period.Point")).alias("point")
)

price_df = cleaned_df.select(
    "timeseries_id",
    "business_type",
    "curve_type",
    "in_domain_code",
    "out_domain_code",
    "currency",
    "price_unit",
    "period_start",
    "period_end",
    "resolution",
    F.col("point.position").cast("int").alias("position"),
    F.col("point.`price.amount`").cast("double").alias("price_amount"),
    F.current_timestamp().alias("ingestion_time")
)

price_df.show(20, truncate=False)

price_df.write.mode("overwrite").parquet(output_path)

job.commit()
