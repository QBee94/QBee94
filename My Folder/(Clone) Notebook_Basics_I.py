# Databricks notebook source
print("Hello World")

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT "Hello world from SQL"

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC # Title 1 
# MAGIC ## Title 2
# MAGIC ### Ttitle 3
# MAGIC
# MAGIC text with a **bold** and *italicized* in it 
# MAGIC
# MAGIC Ordered List 
# MAGIC 1. once
# MAGIC 1. two
# MAGIC 1. three
# MAGIC
# MAGIC Unordered List
# MAGIC *apples
# MAGIC *peaches
# MAGIC *bananas
# MAGIC
# MAGIC | user_id | user_name |
# MAGIC |---------| --------- |
# MAGIC |1|Adam|
# MAGIC |2|Sarah|

# COMMAND ----------

# MAGIC
# MAGIC %run ../Folder_II/Notebook_Basics_II

# COMMAND ----------

print(full_name)

# COMMAND ----------

# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help ()

# COMMAND ----------

dbutils.fs.help ()

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets')
print(files)

# COMMAND ----------

display (files)
