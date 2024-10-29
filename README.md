# etlpipeline

![Alt text](dlt-pipeline/blob/main/dltpipeline.png)

## Overview:
This project builds an efficient data pipeline that transfers data from a PostgreSQL database into BigQuery using the Data Load Tool (DLT) for streamlined loading. Once the data is in BigQuery, dbt is leveraged to handle transformation logic, ensuring modularity, data quality, and consistency across data models. Finally, Power BI provides the front-end visualization, enabling users to access insights through interactive dashboards.

Pipeline Breakdown:

Data Extraction and Loading (DLT):

Data is extracted from PostgreSQL tables and loaded into BigQuery using DLT. DLT handles data extraction efficiently, automating the data load process and ensuring data arrives in BigQuery in a consistent and structured format.
Data Transformation (dbt in BigQuery):

dbt is layered on top of BigQuery to transform raw data into meaningful, analysis-ready models. dbt applies data quality checks, creates clean data models, and enables data lineage tracking, enhancing the transparency and reliability of the data transformation process.
Analytics and Visualization (Power BI):

Power BI serves as the front end, allowing users to interact with the processed data through dashboards and reports. By connecting directly to BigQuery, Power BI can visualize real-time data, supporting dynamic filtering and analysis to meet business intelligence needs.
Key Benefits:

Automated Loading: DLT provides an automated path from PostgreSQL to BigQuery, reducing manual intervention.
Data Quality and Governance: dbt offers a well-documented and governed transformation layer.
Real-time Analytics: Power BI facilitates up-to-date data insights for stakeholders.
This pipeline is a robust solution for moving, transforming, and analyzing data efficiently, providing stakeholders with actionable insights and a scalable architecture.
