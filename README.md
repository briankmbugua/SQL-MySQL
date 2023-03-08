# Introduction to SQL
SQL is a standard for accesing and manipulating databases
# What is SQL?
- SQL stands for Structured Query Language
- SQL lets you access and manipulate databases
- SQL is an ANSI
# What Can SQL do?
- SQL can execute queries against a database
- SQL can retrieve data
- SQL can insert records inside a database
- SQL can update records
- SQL can delete records
- SQL can create new databases
- SQL can create new tables in a database
- SQL can create stored procedures in a database
- SQL can create views in a database
- SQL can set permissions on tables, procedures, and views

# SQL is a Standard - BUT...
Although SQL is an ANSI standard, there are different version of the SQL language
However to be compliant with the ANSI standard, they all support atleast major  
commands (such as SELECT, UPDATE, DELETE, INSERT, WHERE) in a similar manner

# Using SQL in Your Web Site
To build a web site that shows data from a database, you will need
- An RDMS database program (i.e MS Access, SQL Server, MySQL)
- To use a server-side scripting language or framework like PHP or ASP NodeJS, Flask
- To use HTML / CSS to style the page or ReactJS

# RDBMS
RDBMS stands for Relational Database Management System
RDMS is the basis for SQL, and for all modern database systems such MS SQL Server,  
IBM DB2, Oracle, MySQL, and microsoft Access.
The data in RDMS is stored in database objects called tables, A table is a  
collection of related data entries and it consists of columns and rows
Every tables is broken up into smaller entities called fields.  
A field is a column in a table that is desinged to mantain specific information  
about every record in the table
A record also called a row, is each individual entry that exists in a table. A  
record is a horizontall entity in a table.
A column is a vertical entity in a table that contains all information associated  
with a specific field in a table.

# Below is a selection from the "customers" table:
| Customer ID | CustomerName | ContanctName | Address | City   | PostalCode | Country |
| ------------| -------------| ------------ | --------|------  |  ------    |-------- |
|    1        |    Alfreds   | Maria Andres | Obere   | berlin |    12209   | Germany |
|    2        | Ana Trujilo  | Ana Trujilo  | Avda    | Mexico |    05021   | Mexico  |
|    3        | brian        | briank       | kiambu  | 0100   |    30433   | Kenya   |

The table above contains two records(one for each customer) and seven columns(CustomerID  
,CustomerName, ContactName, Address, City, PostalCode, and Country).

# SQL Statements

Most actions you need to perform on the database are done with SQL statements.  
The following SQL statement selects all the records in the "Customers" table:
```sql
SELECT * FROM Customers
```
# Keep in Mind That...
- SQL keywords are NOT case sensitive: select is the same as SELECT it is  
recommended you use uppper-case SQL statements

# Semicolon after SQL Statements?
Some databases require a semicolon at the end of each SQL statement.  
Semicolon is the standard way to separate each SQL statement in the database systems  
that allow more than one SQL statement to be executed in the same call to the server

# Some of The Most Important SQL Commands
- SELECT - extracts data from a database
- UPDATE - updates data in a database
- DELETE - deletes data from a database
- INSERT INTO - insert new data into a database
- CREATE DATABASE - creates a new database
- ALTER DATABASE - modifies a database
- CREATE TABLE - creates a new table
- ALTER TABLE - modifies a database
- DROP TABLE - deletes a table
- CREATE INDEX - creates an index(search key)
- DROP INDEX - deletes an index

# The SQL SELECT Statement
The <span style="color:red;">SELECT</span> statement is used to select data from a database.  
The data returned is stored in a result table, called the result-set.
# SELECT Syntax
```sql
SELECT column1, column2, ...
FROM table_name;
```
Here, column1, column2,...are fields names of the table you want to select data from.  
If you want to select all the fields available in the table use the following syntax
```sql
SELECT * FROM table_name;
```



















