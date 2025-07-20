from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from enrich_accounts.config.ConfigStore import *
from enrich_accounts.functions import *

def SelectFields(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.select(
        col("AccountId"), 
        col("Amount"), 
        col("ExpectedRevenue"), 
        concat(year(to_date(col("CloseDate"))), lit("Q"), quarter(col("CloseDate"))).alias("CloseQtr")
    )
