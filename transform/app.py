from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, ArrayType, StringType, LongType

def main():
    # Initialize Spark Session
    spark = SparkSession.builder \
        .appName("Read JSON File") \
        .getOrCreate()

    # Read JSON file into a DataFrame
    json_file_path = "files/repositories.json"  # Replace with the path to your JSON file
    df = spark.read.option("multiLine", True).json(json_file_path)
    
    # Show the DataFrame content
    
    repo_id = df.select("id").rdd.flatMap(lambda x: x).collect()
    num_prs = {}
    
    for id in repo_id:     
        pr_json_file_path = f"files/{id}.json"
        pr_df = spark.read.option("multiLine",True).json(pr_json_file_path)
        
        # Defaults
        num_prs[id] = {
            "num_prs":0,
            "num_prs_merged":0,
            "merged_at":None   
        }
        
        if pr_df.count() > 0:
            num_prs[id]['num_prs'] = pr_df.count()
            num_prs[id]['num_prs_merged'] = pr_df.filter(pr_df['state'] == 'merged').count()
            num_prs[id]['merged_at'] = pr_df.select("merged_at").rdd.flatMap(lambda x: x).collect()
            
            
            
    schema = StructType([
        StructField("pr_id", LongType(), True),
        StructField("num_prs", IntegerType(), True),
        StructField("num_prs_merged", IntegerType(), True),
        StructField("merged_at", ArrayType(StringType()), True)
    ])

    
    # Transform the nested JSON into a list of rows with flat dictionaries
    rows = [{"pr_id": key, **value} for key, value in num_prs.items()]
    
    rows_df = spark.createDataFrame(rows, schema=schema)
    # num_prs_df = spark.createDataFrame(num_prs.items(), ["id", "num_prs"])
    df_with_num_prs = df.join(rows_df, df["id"] == rows_df["pr_id"], "left")

    df_with_num_prs.select("full_name","id","name","owner.login","num_prs",'num_prs_merged','merged_at').write.mode('overwrite').parquet('files/output.parquet')

    
 

if __name__ == "__main__":
    main()
