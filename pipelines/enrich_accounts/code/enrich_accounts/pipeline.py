from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from enrich_accounts.config.ConfigStore import *
from enrich_accounts.functions import *
from prophecy.utils import *
from enrich_accounts.graph import *

def pipeline(spark: SparkSession) -> None:
    df_salesforce_Account = salesforce_Account(spark)
    df_salesforce_Opportunity = salesforce_Opportunity(spark)
    df_SelectFields = SelectFields(spark, df_salesforce_Opportunity)
    df_AggbyAccountID = AggbyAccountID(spark, df_SelectFields)
    df_account_opportunity_join = account_opportunity_join(spark, df_salesforce_Account, df_AggbyAccountID)
    enriched_accounts(spark, df_account_opportunity_join)

def main():
    spark = SparkSession.builder.enableHiveSupport().appName("enrich_accounts").getOrCreate()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/enrich_accounts")
    spark.conf.set("spark.default.parallelism", "4")
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF", "true")
    registerUDFs(spark)
    
    MetricsCollector.instrument(spark = spark, pipelineId = "pipelines/enrich_accounts", config = Config)(pipeline)

if __name__ == "__main__":
    main()
