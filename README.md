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
```
# NOT Example
The following SQL statement selects all fields from "Customers" Where country is NOT "Germany"
```sql
SELECT * FROM Customers
WHERE NOT Country='Germany'
```
# Combining AND, OR and NOT operators
The following SQL statement selects all fields from "Customers" where country is "Germany" AND city must be "Berlin" OR "Munchen" We use parenthesis to form complex expressions

```sql
SELECT * FROM Customers
WHERE Country='Germany' AND (City='Berlin' OR City='Munchen');
```
Select all fields from "Customers" Where country is NOT "Germany" AND NOT "USA"

```sql
SELECT * FROM Customers
WHERE NOT Country='Germany' AND NOT Country='USA';
```
# SQL ORDER BY keyword
Used to sort the result in ascending or descending order, sorts the records in asceding order by default for descending use <span style="color:red">DESC</span> keyword
```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2,...ASC|DESC; 
```
# SQL INSERT INTO Statement
Use to insert new records in a table
## INSERT INTO syntax
Can be used in two ways
- Specify both the column names and the values to be inserted:
```sql
INSERT INTO table_name (column1, column2, column3, ...)
VALUES (value1, value2, value3, ...);
```
- If your adding values to all the columns of the table, you do not need to specify the column name in the SQL query.Make sure the order of values is in the same order as the columns in the table
```sql
INSERT INTO table_name
VALUES (value1, value2, value3, ...);
```
It's also possible to insert data in specific columns.

# SQL NULL Values
A field with a NULL value is a field with no value.Null is different from a zero value or a field that contains spaces.A field with a NULL value is one that has been left blank during record creation!
## How to Test for NULL Values?
It is not possible to test for NULL values with comparison operators
We will have to use <span style="color:red">IS NULL</span> and <span style="color:red">IS NOT NULL</span> operators instead.
## IS NULL Syntax
```sql
SELECT column_names
FROM table_name
WHERE column_name IS NULL;
```
## IS NOT NULL Syntax
```sql
SELECT column_names
FROM table_name
WHERE column_name IS NOT NULL;
```
Always use IS NULL to look for NULL values.

# The SQL UPDATE Statement
The <span style="color:red">UPDATE</span> statement is use to modify the existing records in a table
## UPDATE sysntax
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```
The WHERE clause in the UPDATE statement specifies which record(s) should be updated.If you ommit the WHERE clause, all records in the table will be updated.
### EXAMPLE
```sql
UPDATE customers
SET name = 'alfred', city='Nairobi'
WHERE CustomerID = 1;
```
# UPDATE Multiple Records
It is the <span style="color:red">WHERE</span> clause that determines hom many records will be updated

# SQL DELETE Statement
used to delete existing records in a table
# DELETE Syntax
```sql
DELETE FROM table_name WHERE condition;
```
If you ommit WHERE clause all records in the table will be deleted

## Delete All Records
It is possible to delete all rows in a table without deleting the table.This means that the table structure, attributes, and indexes will be intact
```sql
DELETE FROM table_name;
```
Example Delete all rows from the Customers table
```sql
DELETE FROM Customers;
```
# The SQL SELECT TOP Clause
The SELECT TOP clause is used to specify the the number of records to return
It is useful on large tables with thousands of records.
Not all database systems support the SELECT TOP clause
## MySQL Syntax
```sql
SELECT column_name(s)
FROM table_name
WHERE condition
LIMIT number;
```
```sql
SELECT * FROM Customers
LIMIT 3;
```
```sql
SELECT * FROM Customers
WHERE Country='Germany'
LIMIT 3;
```
# The SQL MIN() and MAX() Functions
MIN() returns the smallest value of the selected column
MAX() returns the largest value of the selected column
## MIN() Syntax
```sql
SELECT MIN(column_name)
FROM table_name
WHERE condtion;
```
```sql
## MAX() Syntax
SELECT MAX(column_name)
FROM table_name
WHERE condition;
```

# The SQL COUNT(), AVG() and SUM() Functions
COUNT() returns the number of rows that matches a specfied criterion
## COUNT() Syntax
```sql
SELECT COUNT(column_name)
FROM table_name
WHERE condtion;
```
## AVG() Syntax
```sql
SELECT AVG(column_name)
FROM table_name
WHERE condtion;
```
## SUM() Syntax
```sql
SELECT SUM(column_name)
FROM table_name
WHERE condtion;
```
# SQL LIKE Operator
The LIKE operator is used in a WHERE clause to search for a specified pattern in a column
There are two wildcards often used in conjuction with the LIKE operator
 - (%) represents zero, one, or multiple characters
 - The underscore sign(_) represents one, single character
 The percent sign and the underscore can also be used in combinations
 - LIKE 'a%'  starts with a
 - LIKE '%a'  ends with a
 - LIKE '%or%'  any values that have or in any position
 - LIKE '_r%'   any values that have r in the second position
 - LIKE 'a_%'   any values that start with a and at least 2 characters in length
 - LIKE 'a__%'  any values that start with a and are atleast 3 characters in length
 - LIKE 'a%o'   any values that start with a and ends with o






