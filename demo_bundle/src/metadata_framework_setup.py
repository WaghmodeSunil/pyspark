# Databricks notebook source
# DBTITLE 1,Create Catalog metadata_framework
# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS metadata_framework;
# MAGIC
# MAGIC COMMENT ON CATALOG metadata_framework IS 'Metadata framework catalog for multi-layer data architecture (source, bronze, silver, gold).';

# COMMAND ----------

# DBTITLE 1,Create Catalog metadata_framework
# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS metadata_framework;
# MAGIC
# MAGIC COMMENT ON CATALOG metadata_framework IS 'Metadata framework catalog for multi-layer data architecture (source, bronze, silver, gold).';

# COMMAND ----------

# DBTITLE 1,Create Schemas: source, bronze, silver, gold
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS metadata_framework.source;
# MAGIC CREATE SCHEMA IF NOT EXISTS metadata_framework.bronze;
# MAGIC CREATE SCHEMA IF NOT EXISTS metadata_framework.silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS metadata_framework.gold;
# MAGIC
# MAGIC COMMENT ON SCHEMA metadata_framework.source IS 'Source layer: raw external data as-is.';
# MAGIC COMMENT ON SCHEMA metadata_framework.bronze IS 'Bronze layer: ingested raw data with minimal transformation.';
# MAGIC COMMENT ON SCHEMA metadata_framework.silver IS 'Silver layer: cleansed, conformed, and integrated data.';
# MAGIC COMMENT ON SCHEMA metadata_framework.gold IS 'Gold layer: business-level aggregates and curated tables.';

# COMMAND ----------

# DBTITLE 1,Verify Catalog & Schemas
# MAGIC %sql
# MAGIC SHOW CATALOGS LIKE 'metadata_framework';
# MAGIC
# MAGIC SHOW SCHEMAS IN metadata_framework;