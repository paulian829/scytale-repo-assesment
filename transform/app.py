from pyspark.sql import SparkSession

def main():
    # Initialize Spark Session
    spark = SparkSession.builder \
        .appName("Read JSON File") \
        .getOrCreate()

    # Read JSON file into a DataFrame
    json_file_path = "files/repositories.json"  # Replace with the path to your JSON file
    df = spark.read.option("multiLine", True).json(json_file_path).cache()
    
    # Show the DataFrame content
    df.select("full_name","id","name","owner.login").show()
    # Stop the SparkSession
    spark.stop()

if __name__ == "__main__":
    main()
