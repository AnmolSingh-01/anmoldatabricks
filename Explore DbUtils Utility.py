# Databricks notebook source
dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.list('anmolsecretscope')

# COMMAND ----------

dbutils.secrets.get('anmolsecretscope','sapphirestorageak2accountkey')

# COMMAND ----------


