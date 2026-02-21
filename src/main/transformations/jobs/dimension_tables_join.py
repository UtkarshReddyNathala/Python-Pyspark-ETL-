from pyspark.sql.functions import col
from src.main.utility.logging_config import logger

# Enriching the data from different tables
def dimensions_table_join(final_df_to_process,
                          customer_table_df,
                          store_table_df,
                          sales_team_table_df):
    """
    Joins the main DataFrame with customer, store, and sales team tables.
    Drops unnecessary columns after each join and adds selected sales team info.
    """

    # Step 1: Join with customer table
    logger.info("Joining final_df_to_process with customer_table_df")
    s3_customer_df_join = final_df_to_process.alias("s3_data") \
        .join(customer_table_df.alias("ct"),
              col("s3_data.customer_id") == col("ct.customer_id"), "inner") \
        .drop("product_name", "price", "quantity", "additional_column",
              "s3_data.customer_id", "customer_joining_date")

    # Step 2: Join with store table
    logger.info("Joining s3_customer_df_join with store_table_df")
    s3_customer_store_df_join = s3_customer_df_join.join(store_table_df,
                                                        store_table_df["id"] == s3_customer_df_join["store_id"],
                                                        "inner") \
                                                   .drop("id", "store_pincode", "store_opening_date", "reviews")

    # Step 3: Join with sales team table and enrich sales info
    logger.info("Joining s3_customer_store_df_join with sales_team_table_df")
    s3_customer_store_sales_df_join = s3_customer_store_df_join.join(sales_team_table_df.alias("st"),
                                                                    col("st.id") == s3_customer_store_df_join["sales_person_id"],
                                                                    "inner") \
        .withColumn("sales_person_first_name", col("st.first_name")) \
        .withColumn("sales_person_last_name", col("st.last_name")) \
        .withColumn("sales_person_address", col("st.address")) \
        .withColumn("sales_person_pincode", col("st.pincode")) \
        .drop("id", "st.first_name", "st.last_name", "st.address", "st.pincode")

    return s3_customer_store_sales_df_join
