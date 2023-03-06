# INTRODUCTION
mysql(sometimes reffered to as the "terminal monitor" or just "monitor") is an interactive  
program that enables you to connect to a MySQL server, run queries, and view the results.  
mysql may also be used in batch mode: you place your queries in a file beforehand, then  
tell mysql to execute the contents of the file

To see a list of options provided by mysql, invoke it with the --help option:
```bash
$>mysql --help
```

# Connecting to and Disconnecting from the Server
To connect to the server, you usually need to provide a MySQL user name when you invoke  
mysql and, most likely, a password. If the server runs on a machine other than the one  
where you log in, you must also specify a host name.
Once you know the proper parameters, you should be able to connect like this:
```bash
$>mysql -h host -u user -p
Enter password: ******
```
host and user represent the host name where your MySQL server is running and the user name  
of your MySQL account.
if that works you should see some introductory information follwed by a mysql> prompt:
```bash
$>mysql -h host -u user -p
Enter password:*******
Welcome to the MySQL monitor. Commands end with ; or \g.
Your MySQL connection id is 25338 to server version: 8.0.32-standard
Type 'help;' or '\h' for help. Type '\c' to clear the buffer.
mysql>
```
