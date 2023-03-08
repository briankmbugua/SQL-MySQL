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

# The SQL SELECT DISTINCT statement
The SELECT DISTINCT statement is used to return only distinct(different) values.
Inside a table, a column often contains many duplicate values;and sometimes you only  
want to list the distinc(different)values.

# SELECT DISTINCT Syntax
```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```
# SELECT DISTINCT Examples
The following SQL statement selects only the DISTINCT values from the "Country"  
column in the "Customers" table:
```sql
SELECT DISTINCT Country FROM Customers;
```
The following SQL statement lists the number of different(distinct) customer countries:
```sql
SELECT COUNT(DISTINCT Country) FROM Customers;
```

# SQL WHERE Clause
The <span style="color:red">WHERE</span> clause is used to filter records.
It is used to extract only those records that fulfill a specified condition.
# WHERE Syntax
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```
> **Note**: The <span style="color:red">WHERE</span> clause is not only used in <span style="color:red">SELECT</span> statements, it also used in  
><span style="color:red">UPDATE, DELETE</span>, etc.!
# WHERE Clause Example
The following SQL statement selects all the customers from the country "Mexico", in the  
"Customers" table:
```sql
SELECT * FROM Customers
WHERE Country='Mexico';
```
# Text Fields vs. Numeric Fields
SQL requires single quotes around text values(most database systems will also allow double quotes).  
However numeric fields should not be enclose in quotes
```sql
SELECT * FROM Customers
WHERE Customer1D=1;
```
# Operators in The WHERE Clause
The following operators can be used in the <span style="color:red">WHERE</span> clause:

| Operator | Description                                |
| -------  | -------------------------------------------|
|  =       | Equal                                      |
|  >       | Greator than                               |
|  <       | Less than                                  |
|  >=      | Greator than or equal                      |
| <=       | Less than or equal                         |
| <>       | Not equal. **Note:** in some versions of SQL this operator may be written as !=|
| BETWEEN  | Between a certain range SELECT * FROM Products WHERE Price BETWEEN 50 AND 60;
| lIKE     | Search for a pattern |
| IN       | To specify multiple possible values for a column SELECT * FROM Customers WHERE City IN ('Paris','London');|

# SQL AND, OR and NOT Operators
The <span style="color:red">WHERE</span> clause can be combined with <span style="color:red">AND</span>, <span style="color:red">OR</span> and <span style="color:red">NOT</span> operators.
The <span style="color:red">AND</span> and <span style="color:red">OR</span> operators are used to filter records based on more than one condition:
- The <span style="color:red">AND</span> operator displays a record if all the conditions separeted by <span style="color:red">AND</span> are TRUE
- The <span style="color:red">OR</span> operator displays a record if any of the conditions separated by <span style="color:red">OR</span> is TRUE

The <span style="color:red">NOT</span> operator displays a record if the condition(s) is NOT TRUE

# AND Syntax
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```
# OR Syntax
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition1 AND condition2 AND condition3 ...;
```
# NOT Syntax
```sql
SELECT column1, column2, ...
FROM table_name
WHERE NOT condition;
```
# AND Example
The following SQL statement selects all fields from "Customers" Where country is
"Germany" AND city is "Berlin"
```sql
SELECT * FROM Customers
WHERE Country='Germany' AND City='Berlin';
```
# OR Example
The following SQL statement selects all fields from 'Customers' where city is 'Berlin'
OR 'Munchen':
```sql
SELECT * FROM Customers
WHERE City='Berlin' OR City='München';
``















