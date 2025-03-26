# Databricks notebook source

spark.conf.set("fs.azure.account.auth.type.robustmodeldatalake.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.robustmodeldatalake.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.robustmodeldatalake.dfs.core.windows.net", "Secret Here")
spark.conf.set("fs.azure.account.oauth2.client.secret.robustmodeldatalake.dfs.core.windows.net", "Secret Here")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.robustmodeldatalake.dfs.core.windows.net", "https://login.microsoftonline.com/Secret Here")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Data Transformation Script:  

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Loading: 

# COMMAND ----------

# MAGIC %md
# MAGIC #### Reading Calendar Data from Data Lake Gen 2: 
# MAGIC
# MAGIC  - Create a Dataframe by importing the data using the Python Library Spark
# MAGIC

# COMMAND ----------

# Raw dataframe: 
df_ProductsCategories = spark.read.format("csv").option("header", True).option("inferSchema",True).load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Product_Categories')
df_Calendar  = spark.read.format("csv").option("header", True).option("inferSchema",True).load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Calendar')
df_Customers  = spark.read.format("csv").option("header", True).option("inferSchema",True).load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Customers')
df_Products = spark.read.format("csv").option("header", True).option("inferSchema",True).load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Products')
df_Returns  = spark.read.format("csv").option("header", True).option("inferSchema",True).load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Returns')
df_Sales_2015  = spark.read.format("csv").option("header", True).option("inferSchema",True).load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Sales_2015')
df_Sales_2016  = spark.read.format("csv").option("header", True).option("inferSchema",True).load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Sales_2016')
df_Sales_2017  = spark.read.format("csv").option("header", True).option("inferSchema",True).load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Sales_2017')
df_Territories = spark.read.format("csv").option("header", True).option("inferSchema",True).load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Territories')
df_Product_Subcategories = spark.read.format("csv").option("header", True).option("inferSchema",True).load('abfss://low@robustmodeldatalake.dfs.core.windows.net/Product_Subcategories')

# COMMAND ----------

df_ProductsCategories.display()


# COMMAND ----------

df_Territories.display()

# COMMAND ----------

df_Customers.display()

# COMMAND ----------

df_Products.display()

# COMMAND ----------

df_Returns.display()

# COMMAND ----------

# Do Advanced Data Import Function::::::
df_Date= spark.read.format("csv")\
                       .option("header", True)\
                       .option("inferSchema",True)\
                       .load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Sales*')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Code Explanation: 
# MAGIC
# MAGIC - Spark.read.format() --- callable syntax: 
# MAGIC - load(
# MAGIC    - 'abfss':
# MAGIC     - //low:
# MAGIC     - @robustmodeldatalake.dfs.core.windows.net/ ---  Standard Callable syntax for path to Data Lake
# MAGIC     - AdventureWorks_Product_Categories' ---- Folder that we need to Use to upload the data into our Databricks: 
# MAGIC   )

# COMMAND ----------

# Do Advanced Data Import Function::::::
df_sales = spark.read.format("csv")\
                       .option("header", True)\
                       .option("inferSchema",True)\
                       .load('abfss://low@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Sales*')

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales.columns

# COMMAND ----------

from pyspark.sql.functions import sum,avg,max, count
### What is the total numbers for the 3 years and the total orders made by date: 
#main_columns = ["OrderDate"]
df_sales.groupby('OrderDate').agg(count('OrderNumber').alias('total_order')).display()

# COMMAND ----------

df_ProductsCategories.display()

# COMMAND ----------

df_Product_Subcategories.display()

# COMMAND ----------

df_Territories.display()

# COMMAND ----------

# MAGIC %md 
# MAGIC #### Moving the Dataframes Available to the Middle Layer from Lower: 

# COMMAND ----------

df_Calendar.display()

# COMMAND ----------

print(type(df_Calendar['Date']))

# COMMAND ----------

from datetime import datetime
import pandas as pd
from pyspark.sql.functions import to_date, year, month
from pyspark.sql.functions import when, col

df_Calendar = df_Calendar.withColumn('Date', to_date(df_Calendar['Date'], 'MM-dd-yyyy'))

# Add 'Year' and 'Month' columns:
df_Calendar = df_Calendar.withColumn('Year', year(df_Calendar['Date']))
df_Calendar = df_Calendar.withColumn('Month', month(df_Calendar['Date']))

# Mapping the Month Column: 
month_order = {1:'January', 
               2:'February', 
               3:'March', 
               4:'April', 
               5:'May', 
               6:'June', 
               7:'July', 
               8:'August', 
               9:'September', 
               10:'October', 
               11:'November', 
               12:'December'
            }
        
# Create a new column 'Month_Name' based on the mapping
df_Calendar = df_Calendar.withColumn(
    'Month_Name',
    when(col('Month') == 1, month_order[1])
    .when(col('Month') == 2, month_order[2])
    .when(col('Month') == 3, month_order[3])
    .when(col('Month') == 4, month_order[4])
    .when(col('Month') == 5, month_order[5])
    .when(col('Month') == 6, month_order[6])
    .when(col('Month') == 7, month_order[7])
    .when(col('Month') == 8, month_order[8])
    .when(col('Month') == 9, month_order[9])
    .when(col('Month') == 10, month_order[10])
    .when(col('Month') == 11, month_order[11])
    .when(col('Month') == 12, month_order[12])
    .otherwise("Unknown")  # Optional: handle unexpected values
)


df_Calendar.show()

# COMMAND ----------

### Storing data in different mode:  Parquet-, Append, Overwrite- Store fresh data, error()-, ignore-if data is in a folder it will note through nor write the data as well: 
df_sales.write.format("Parquet")\
    .mode("append")\
    .option("path", "abfss://middle@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Sales*")\
    .save()


# COMMAND ----------

df_Calendar.write.format("Parquet")\
    .mode("append")\
    .option("path", "abfss://middle@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Calendar")\
    .save()

# COMMAND ----------

df_Products.write.format("Parquet")\
    .mode("append")\
    .option("path", "abfss://middle@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Products")\
    .save()

# COMMAND ----------

df_Returns.write.format("Parquet")\
    .mode("append")\
    .option("path", "abfss://middle@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Returns")\
    .save()

# COMMAND ----------

df_Product_Subcategories.write.format("Parquet")\
    .mode("append")\
    .option("path", "abfss://middle@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Product_Subcategories")\
    .save()

# COMMAND ----------

df_ProductsCategories.write.format("Parquet")\
    .mode("append")\
    .option("path", "abfss://middle@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_ProductsCategories")\
    .save()

# COMMAND ----------

df_Territories.write.format("Parquet")\
    .mode("append")\
    .option("path", "abfss://middle@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Territories")\
    .save()

# COMMAND ----------

df_Customers.write.format("Parquet")\
    .mode("append")\
    .option("path", "abfss://middle@robustmodeldatalake.dfs.core.windows.net/AdventureWorks_Customers")\
    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC from pyspark.sql.functions import sum,avg,max