# %%

# %%
from hyperopt_prophet_spark import DatabricksSQLSession

# %%
spark_sql = DatabricksSQLSession()
# %%
pdf = spark_sql.sql("select * from microchip_logs limit 10")
print(pdf.head())
# %%
sqlalchemy_engine = spark_sql.get_session()
# %%
df = spark_sql.read(sqlalchemy_engine, "microchip_logs")

# %%
from hyperopt_prophet_spark import DatabricksJDBCSession

# %%
spark_jdbc = DatabricksJDBCSession().get_session()


# %%

from hyperopt_prophet_spark import DatabricksSparkSession

# %%
spark = DatabricksSparkSession().get_session()

# %%
sdf = spark.read.table("microchip_logs")
print(sdf.show())
# %%

from hyperopt_prophet_spark import DatabricksMLFlowSession

# %%
mlflow_session = DatabricksMLFlowSession().get_session()

# %%
print(mlflow_session.client.MlflowClient())
# %%
