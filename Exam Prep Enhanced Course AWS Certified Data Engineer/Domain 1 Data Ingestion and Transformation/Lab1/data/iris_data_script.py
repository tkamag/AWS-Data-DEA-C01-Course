import argparse

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def iris_data_exploration(data_source, output_uri):
    """
    Processes iris data and queries the data to find the average of sepal length of each iris class.

    :param data_source: The URI of your iris data CSV, such as 's3://LAB-BUCKET/iris-data.csv'.
    :param output_uri: The URI where output is written, such as 's3://LAB-BUCKET/output'.
    """
    with SparkSession.builder.appName("Data Exploration").getOrCreate() as spark:
        # Load the iris CSV data as Spark DataFrame
        if data_source is not None:
            iris_df = spark.read.option("header", "true").csv(data_source)

        # Convert String attributes to INT
        iris_df_new = iris_df.selectExpr('CAST(sepal_length AS INT) AS Sepal_Length',
                                         'CAST(sepal_width AS INT) AS Sepal_Width',
                                         'CAST(petal_length AS INT) AS Petal_Length',
                                         'CAST(petal_width AS INT) AS Petal_Width',
                                         'class')

        # Create a DataFrame of the average sepal length of each iris class
        avg_sepal_length_per_class = iris_df_new.select('Sepal_Length','class').groupBy('class').agg(mean("Sepal_Length"))

        # Merge data from all partitions into a single partition
        avg_sepal_length_per_class.coalesce(1).write.option("header", "true").mode("overwrite").csv(output_uri)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_source', help="The URI for your CSV iris data, like an S3 bucket location.")
    parser.add_argument(
        '--output_uri', help="The URI where output is saved, like an S3 bucket location.")
    args = parser.parse_args()

    iris_data_exploration(args.data_source, args.output_uri)
