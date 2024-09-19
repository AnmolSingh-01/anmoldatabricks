# Databricks notebook source
''' Store the scope & Secret Key in a variable 
'''

anmolaccountkey = dbutils.secrets.get(
    scope='anmolsecretscope', 
    key='sapphirestorageak2accountkey'
)

display(type(anmolaccountkey))   # just for knowing it returns 'str'

# COMMAND ----------

'''Set configs for storage A/C 'sapphirestorage2' by access key 'anmolaccountkey'
which holds scope & key '''

spark.conf.set(
    "fs.azure.account.key.sapphirestorageak2.dfs.core.windows.net",
     anmolaccountkey
    )

# COMMAND ----------

#List the files from 'raw' container of 'sapphirestorage2' storage account.

display(dbutils.fs.ls("abfss://raw@sapphirestorageak2.dfs.core.windows.net"))

# COMMAND ----------

# Lets use the intended file 

display(spark.read.csv("abfss://raw@sapphirestorageak2.dfs.core.windows.net/pizza_sales.csv"))


# COMMAND ----------


