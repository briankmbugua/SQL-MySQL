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
 # SQL Wildcards
 A wildcard chracter is used to substitute one or more charcters in a string
 They are used with LIKE operator.The LIKE operator is used in WHERE clause to search for a specified pattern in a column.
 In MySQL the use of wildcard characters can impact query performance.Therefore it is recommended to use them judiciously and optimize queries as necessary.

  - "%" (percent sign): Matches any sequence of zero or more characters. For example, "a%" matches any string that starts with "a", such as "apple", "apricot", and "alligator".

  - "_" (underscore): Matches any single character. For example, "h_t" matches "hat", "hot", and "hit".

  - "[]" (square brackets): Matches any single character within the brackets. For example, "[aeiou]" matches any vowel.

  - "[^]" (caret inside square brackets): Matches any single character not within the brackets. For example, "[^aeiou]" matches any consonant.

  - "*" (asterisk): Matches any sequence of zero or more characters, similar to the "%" wildcard.

  - "?" (question mark): Matches any single character, similar to the "_" wildcard
  ## IN MySQL
  - "%" and "_" can be used with the LIKE operator to match one or more characters in a string. For example, the query "SELECT * FROM customers WHERE name LIKE 'J%'" will return all customers whose names start with the letter "J".

  - The "[...]" and "[^...]" syntax can be used to match any character in a specific range or set. For example, the query "SELECT * FROM products WHERE name REGEXP '^[A-D].*$'" will return all products whose names start with the letters A, B, C, or D.

  - MySQL also supports the "REGEXP" operator, which allows for more advanced pattern matching using regular expressions.

  - In MySQL, the "%" and "_" wildcard characters can also be used with the "RLIKE" operator for regular expression pattern matching.
 # SQL IN Operator
 The IN operator allows you to specify multiple values in a WHERE clause
 The IN operator is a shorthand for multiple OR conditions
 ## IN Syntax
 ```sql
 SELECT column_name(s)
 FROM table_name
 WHERE column_name IN (value1, value2, ...);
 ```
 or

 ```sql
 SELECT column_name(s)
 FROM table_name
 WHERE column_name IN (SELECT STATEMENT);
 ```
 ### EXAMPLE
 selects all customers that are located in germany, france or uk
 ```sql
 SELECT * FROM Customers
 WHERE Country IN ('Germany', 'France', 'UK');
```
selects all customers that are  not located in germany, france or uk
 ```sql
 SELECT * FROM Customers
 WHERE Country NOT IN ('Germany', 'France', 'UK');
```

selects all customers that are from the same countries as suppliers
 ```sql
 SELECT * FROM Customers
 WHERE Country NOT IN (SELECT Country FROM Suppliers);
```
# The SQL BETWEEN Operator
BETWEEN operator selects values within a given range.The values can be numbers, text or dates.
The BETWEEN operator is inclusive: begin and end values are included

# Syntax
```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value1 AND value2;
```
# Examples
All products with a price between 10 nad 20
```sql
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20;
```
```sql
SELECT * FROM Products
WHERE Price NOT BETWEEN 10 AND 20;
```
All products with a price between 10 and 20 and not products with a categoryID of 1,2 or 3
```sql
SELECT * FROM Products
WHERE Price BETWEEN 10 AND 20
AND CategoryID NOT IN (1,2,3)
```
## BETWEEN Text Values
all products with a productName Between Tigers and Giovanni
```sql
SELECT * FROM Products
WHERE ProductName BETWEEN 'Tigers' AND 'Giovanni'
ORDER BY ProductName
```
all products with a productName Not Between Tigers and Giovanni
```sql
SELECT * FROM Products
WHERE ProductName BETWEEN 'Tigers' AND 'Giovanni'
ORDER BY ProductName
```
## BETWEEN Dates
```sql
SELECT * FROM Orders
WHERE OrderDate BETWEEN #07/01/1996# AND #07/31/1996#;
```
or

```sql
SELECT * FROM Orders
WHERE OrderDate BETWEEN '1996-07-01' AND '1996-07-31';
```

# SQL Aliases
give a table or a column in a table a temporary name
Alias Column Syntax
```sql
SELECT column_name AS alias_name
FROM table_name;
```
Aliase Table Syntax
```sql
SELECT column_name(s)
FROM table_name AS alias_name;
```
# SQL Joins
A JOIN clause is used to combine rows from two or more tables, based on a related column between them.
## keyword
OUTER is an optional keyword.
# INNER JOIN
The INNER JOIN keyword selects records that have matching values in both tables.
## INNER JOIN SYNTAX
```sql
SELECT column_name(s)
FROM table1
INNER JOIN table2
ON table1.column_name = table2.column_name;
```
## EXAMPLE
```sql
SELECT * FROM Customer INNER JOIN City ON Customer.CityId=City.CityId;
```
CityId is the column that is similar on both tables.
INNER JOIN is the most used

# LEFT JOIN
## LEFT JOIN Syntax
```sql
SELECT column_name(s)
FROM table1
LEFT JOIN table2
ON table1.column_name = table2.column_name;
```
In the syntax example it returns all records from the left table(table1), and matching records from the right table(table2).The result is 0 records from the right side, if there is no match.

 Get all records from the left table and also everything that matches on both tables
 We want everything that matches on both tables and everything that does not match in the left table.
 ```sql
 SELECT * FROM Customer LEFT JOIN City ON Customer.CityId=City.CityId;
```
The left tables is the table on the left side of the JOIN clause.

# RIGHT JOIN

## RIGHT JOIN Syntax
```sql
SELECT column_name(s)
FROM table1
RIGHT JOIN table2
ON table1.column_name = table2.column_name;
```
The RIGHT JOIN keyword returns all records from the right table (table2), and the matching records from the left table (table1). The result is 0 records from the left side, if there is no match.

 Get all columns from the right table and also everything that matches on both tables
 We want everything that matches on both tables and everything that does not match in the right table.
 ```sql
 SELECT * FROM Customer RIGHT JOIN City ON Customer.CityId=City.CityId;
```
# FULL OUTER JOJN
Get everything that matches on both tables but also everything that does not match from both tables.
 ```sql
 SELECT * FROM Customer FULL JOIN City ON Customer.CityId=City.CityId;
```
## FULL OUTER JOIN Syntax
```sql
SELECT column_name(s)
FROM table1
FULL OUTER JOIN table2
ON table1.column_name = table2.column_name
WHERE condtion;
```
Returns all matching records from both tables whether the other table matches or not.

## stored procedures
This is a prepared SQL code that you can save, so the code can be reused over and over again
### syntax
```sql
CREATE PROCEDURE procedure_name
AS
sql_statement
GO;
```
### Executing a stored procedure
```sql
EXEC procedure_name;
```
### Stored procedure example
Create a stored procedure named "SelectAllCustomers" that select all records from the "Customers" table
```sql
CREATE PROCEDURE SelectAllCustomers
AS
SELECT * FROM Customers
GO;

-- Execute the stored procedure as follows
EXEC SelectAllCustomers;

-- Stored procedure with one parameter
CREATE PROCEDURE SelectAllCustomers @city nvarchar(30)
AS
SELECT * FROM Customers WHERE City = @City```

-- Execute it as follows
EXEC SelectAllCustomers @City = 'London';

-- Stored procedure with Multiple parameters
-- Setting up multipe parameters is very easy, just list each parameter and the data type separated by a comma
-- select customers from a particular city with a particular postalcode from the customers table

CREATE PROCEDURE SelectAllCustomers @City nvarchar(30),
@PostalCode nvachar(10)
AS
SELECT * FROM Customers WHERE city = @city AND PostalCode = @PostalCode
GO;

-- Execute the statement as follows
EXEC SelectAllCustomers @City = 'London', @Postalcode = 'WA11DP';
```

# SQL DATABASE
```SQL
-- create database statement
CREATE DATABASE databasename;
-- Deleting a database
DROP DATABASE databasename;
-- backup a database this creates a full backup of an existing database
BACKUP DATABASE databasename
TO DISK = 'filepath';
-- backup with differential this back ups the parts of the database that have changed since the last full database backup.
BACKUP DATABASE databasename
TO DISK = 'filepath'
WITH DIFFERENTIAL;
 -- a differential backup reduces the back up time since only the changes are backed up

-- create table
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype,
    ...
)

-- Create Table Using Another Table
-- a copy of an existing table can also be created using CREATE TABLE.The new table gets the same column definations.All columns or specific columns can be selected.if you create a new table using an existing table, the new table will be filled with the existing values from the old table.

CREATE TABLE new_table_name AS
     SELECT column1, column2, ...
     FROM existing_table_name
     WHERE ....;

-- SQL DROP TABLE statement is used to drop an existing table in a database
DROP TABLE table_name;
-- this will result in loss of complete information stored in the table
-- The TRUNCATE TABLE statement is used to delete the data inside a table, but not the table itself
TRUNCATE TABLE table_name;


-- SQL ALTER TABLE Statement
-- The ALTER TABLE statement is used to add, delete, or modify columns in an existing table.It is also used to add and drop various constraints on an existing table.

-- ALTER TABLE - ADD Column
ALTER TABLE table_name
ADD column_name datatype;

-- ADD an "Email" column to the "Customers" table
ALTER TABLE Customers
ADD Email varchar(255);

-- ALTER TABLE - DROP COLUMN
ALTER TABLE table_name
DROP COLUMN column_name;

-- ALTER TABLE - RENAME COLUMN
ALTER TABLE table_name
RENAME COLUMN old_name to new_name;


-- SQL Constraints
-- SQL constraints are used to specify rules for data in a table. Constraints can be specified when the table is created with the CREATE TABLE statement, or after the table is created with the ALTER TABLE statement

CREATE TABLE table_name (
    column1 datatype constraint;
    column2 datatype constraint;
    column3 datatype constraint;
    ....
);
```
Constraints can be column level or table level constraints
The following constraints are commonly used in SQL:
- NOT NULL - ensures that a column cannot have a NULL value
- UNIQUE - Ensures that all values in a column are different
- PRIMARY KEY - A combination of NOT NULL and UNIQUE.Uniquely identifies each row in a table
- FOREIGN KEY - Prevents actions that would destroy links between tables
- CHECK - Ensures that values in a column satisfies a specif condtion
- DEFAULT - Sets a default value for a column if no value is specified
- CREATE INDEX - used to create and retrieve data from the database very quickly

# SQL PRIMARY KEY Constraint
The PRIMARY KEY constraint uniquely identifies each record in a table. Primary keys must contain UNIQUE val

