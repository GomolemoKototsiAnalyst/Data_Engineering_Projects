# Data Engineering End-To-End Project Based Learning: 
In this project I was learning and putting my skills to practice for the data engineering frameworks, principles and methodologies I have been learning in the previous months. 

#### Process Engaged: 
-  Design & Implementation of a robust data pipeline using Azure Data Factory.
-  Intermediate Data Integration and Transformation with Databricks.
-  Utilizing Azure Synapse Analytics for efficient data warehousing and analytics.
-  Lastly, Integrated Azure Data Warehouse to Power BI.

Data Architecture Schema: 

Steps: 
1. Created an Azure Free Account
-  Username: **Gomolemo.kot@gmail.com**
2. Data Ingestion Process:
      - Created a resource group named: Data_Engineering_Project
      - Created a Azure Data Factory(V2) Account named: Robustmodeldatalake:
         - Created 3 Containers Named: 1. Low Layer (Raw Data/Bronze Layer) , 2 Middle( Silver Layer) 3. Premium Layer( Gold Layer)
         - Dynamic Data Migration from Github to Azure Data Factory(**Azure Data Lake Gen 2**) Using **HTTP API** and Data Format to migrate as **CSV**.
              - Since Dynamic Process was used and not static:
                   - Used 3 Parameters(1 for the **Source** & 2 for the **Sink/Destination**) :
                                       1. Source: Url Parameter for the **Base URL**
                                       2. Sink 1. Folder Parameter named **Folder Name**
                                       3. Sink 2: Parameter named **File Name**
                      
                   - Create a Compute( This is simply to create a loop that could iterate through the github folder until all files are copied to my Data Lake)
                     
3. Created a **Databricks** Account named adb-Data_engineering_project : After the Data Ingestion process was completed I did the ETL process with Databricks.
  - In Order for **Databricks** & **Azure Data Factory** to communicate I had to create a linked service to ***Manage Access/Access Control** named **Microsoft Entra**
  - Creating Microsoft Entra App:
       - Register an application(Access Management application named)
       - Created Certifications & Secrets
       - Access Rights Assigned: **Storage Blob Contributer** ( Offers Databricks read & write access to the Data Lake Gen 2 resource)
      - Initial Layer Named: Low Layer(Synonymus to Bronze Layer)
  - After the above, Created a Cluster in Databricks -- Manage Costs.
 -  Begin ***Silver Layer Process***: Transforming & Cleaning Data Using Notebooks  ---- PySpark Python Library
 -  The data cleaned was then pushed the data to the Data Factory Container named Middle using **PARQUETS** data format in PySpark.
4. Reporting Process Build:
- Create an Azure Synapse Analytics Workspace:
    - Create resource using a Managed Account
    - Link the account to my Resouce Group( Data Engineering Project)
    - Named the Workspace: **defaultsynapse**
    - Created a Storage Account of Synapse named it **defaultsynapse-storage**
- Create a Azure SQL Serverless Workspace in Synapse:
  - Created a serverless domain and not dedicated to link my Synapse too for Reporting( I did not want to Use an API so I instead went the managed identity route for ease and less complexity)
  - Created an External data lake ( Named resource.premium/ **GOLD Layer** to be used in Reporting for Power BI)
  - SQL DataBase (Lake House = Built my Data Lake & Data Warehouse in the same resource reduce potential cloud costs and just built basic efficiencies in the resouce)
       - Created Tables using SQL **Openrowset** then Created multiple VIEWS to the Schema stored it in my Container named Premium/GOLD Layer.
5. Reporting: Linking my Synapse SQL Severless Data Lake to Power BI:
 - CURRENLTY BUSY WITH THIS STEP....
