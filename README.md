# **README**

## **Files**
Because we have several houndred lines of code I will give a quick rundown of what the different files contain and are responsible for.
#### ***main.py***
This is the applications EntryPoint and where the application loop is located. It contains the global variables that hold the database connection information. Such as username, password etc.
#### ***funcs.py***
Here is where the application specific functionality is placed. Such as calling functions from sql.py and building specific queries, retrieving the data and passing that data on to the responsible print function inside ui.py.
#### ***sql.py***
This file contains both generalized SQL queries as well as application specific queries.
#### ***CDatabaseManager.py***
This class is responsible for managing the mysql connector and mysql cursor. When provided with data stored in memory it creates schemas, tables and inserting data into the newly created tables. This includes creating the Primary keys and Foreign keys and linking them togheter.

It relies on that the data recieved is formatted correctly. This format can be observed by openeing the csv file included in this project. Here's a quick rundown:
* The names of a schemas attributes are placed in line one (1).
* Primary keys are prefixed with  *
* Foreign keys are prefixed with &
* Attributes are divided by ~
* All junction tables are placed at the end after all other tables.
#### ***CFileStream.py***
This class is responsible for retriving the current working directory and loading a csv file from disk into memory.
#### ***ui.py***
Has several convinent wrapper functions for input and printing colored text to the terminal.
#### ***Debugger.py***
This file contains code for attaching the debugger at runtime and logging error and warning messages to the screen. It exist to help with development.