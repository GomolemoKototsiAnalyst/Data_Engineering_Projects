------------------------
-- CREATE VIEW CALENDAR
------------------------
CREATE VIEW premium.Calendar
AS
SELECT 
    * 
FROM 
    OPENROWSET
        (
            BULK 'https://robustmodeldatalake.blob.core.windows.net/middle/AdventureWorks_Calendar/',
            FORMAT = 'PARQUET'
        ) as QUER1

------------------------
-- CREATE VIEW SALES
------------------------

CREATE VIEW premium.Adventure_Sales
AS
SELECT 
    * 
FROM 
    OPENROWSET
        (
            BULK 'https://robustmodeldatalake.blob.core.windows.net/middle/AdventureWorks_Sales*/',
            FORMAT = 'PARQUET'
        ) as QUER1
------------------------
-- CREATE VIEW CUSTOMERS
------------------------
CREATE VIEW premium.Adventure_Customers
AS
SELECT 
    * 
FROM 
    OPENROWSET
        (
            BULK 'https://robustmodeldatalake.blob.core.windows.net/middle/AdventureWorks_Customers/',
            FORMAT = 'PARQUET'
        ) as QUER1

------------------------
-- CREATE VIEW Product Categories
------------------------
CREATE VIEW premium.Adventure_ProductCategories
AS
SELECT 
    * 
FROM 
    OPENROWSET
        (
            BULK 'https://robustmodeldatalake.blob.core.windows.net/middle/AdventureWorks_ProductCategories/',
            FORMAT = 'PARQUET'
        ) as QUER1
------------------------------------
-- CREATE VIEW Product Subcategories
------------------------------------
CREATE VIEW premium.Adventure_ProductSubcategories
AS
SELECT 
    * 
FROM 
    OPENROWSET
        (
            BULK 'https://robustmodeldatalake.blob.core.windows.net/middle/AdventureWorks_ProductSubcategories/',
            FORMAT = 'PARQUET'
        ) as QUER1

------------------------
-- CREATE VIEW PRODUCTS
------------------------
CREATE VIEW premium.AdventureWorks_Products
AS
SELECT 
    * 
FROM 
    OPENROWSET
        (
            BULK 'https://robustmodeldatalake.blob.core.windows.net/middle/AdventureWorks_Products/',
            FORMAT = 'PARQUET'
        ) as QUER1

------------------------
-- CREATE VIEW RETURNS
------------------------
CREATE VIEW premium.Adventure_Returns
AS
SELECT 
    * 
FROM 
    OPENROWSET
        (
            BULK 'https://robustmodeldatalake.blob.core.windows.net/middle/AdventureWorks_Returns/',
            FORMAT = 'PARQUET'
        ) as QUER1

---------------------------
-- CREATE VIEW TERRITORIES
--------------------------
CREATE VIEW premium.Adventure_Territories
AS
SELECT 
    * 
FROM 
    OPENROWSET
        (
            BULK 'https://robustmodeldatalake.blob.core.windows.net/middle/AdventureWorks_Territories/',
            FORMAT = 'PARQUET'
        ) as QUER1
