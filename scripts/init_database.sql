-- Create a new database named datawarehouse. If the database exists, it will be dropped and recreated.
DROP DATABASE IF EXISTS datawarehouse;
CREATE DATABASE datawarehouse;

-- Set up schemas following Medallion architecture: bronze, silver and gold.
CREATE SCHEMA bronze;
CREATE SCHEMA silver;
CREATE SCHEMA gold; 
