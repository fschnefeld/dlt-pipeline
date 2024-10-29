import dlt
from dlt.sources.credentials import ConnectionStringCredentials
from dlt.sources.sql_database import sql_database


def load_select_tables_from_database() -> None:
    """Load select tables from a PostgreSQL database to BigQuery without incremental loading."""
    
    # Create a pipeline to load from PostgreSQL to BigQuery
    pipeline = dlt.pipeline(
        pipeline_name="postgres_to_bigquery", destination='bigquery', dataset_name="coloplast"
    )

    # PostgreSQL credentials
    credentials = ConnectionStringCredentials(
        "postgresql+psycopg2://postgres:WXnqNB9bqMEC@localhost:5432/coloplast"
    )
    # Load select tables without incremental loading
    source = sql_database(credentials, schema='public').with_resources("supplychain_data")


    # Run the pipeline with 'replace' to overwrite the entire table in BigQuery each time
    info = pipeline.run(source, write_disposition="replace")
    print(info)

if __name__ == "__main__":
    load_select_tables_from_database()
