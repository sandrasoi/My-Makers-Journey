<h1>Week5</h1>

<h2>Goals:</h2>

- Design a database schema with at least two tables from a specification, including a one-to-many relationship between two tables, and create the schema in a database using SQL.
- Use SQL to query a database to read data from one table or resulting of a join, create new records, update and delete.
- Integrate a relational database to a program by test-driving classes which implement CRUD methods to send SQL queries to a database.
- Explain how your program communicates with the database by creating a sequence diagram.

<h3>Monday 2nd October</h3>

Today I learned about SQL which is a language that lets us query, create or modify data stored in a database. Up until now, the programs we created only exitst in the memory so it is not good if data needs to be stored for a long time.

I set up PostgresSQL which is a rational database software to learn about databases and SQL. I learned simple commands to retrieve, update, delete and insert data to a database. I also set up TablePlus which is a Graphical User Interface which allows me to see the database much easier than my using psql to return values in a database.

I am continuing to pair-program and today I worked on short SQL exercises to practise SQL and reinforce my understanding. 

<h3>Tuesday 3rd October</h3>

I learned how to connect to a database, and what model and repository classes are. I completed a [test-driving challenge](https://github.com/sandrasoi/book_store) where I created a book class and a book repository class to retrieve data from the book store database. This solidified my understanding of various concepts such how to connect to the database and how to use SQL to retrieve data. 

<h3>Wednesday 4th October</h3>

I learned to create a [sequence diagram](https://github.com/sandrasoi/My-Makers-Journey/blob/main/My-Programs/databases/sequence%20diagram%20book%20store.svg) for my book_store program using diagram.codes which helps to create a diagram for programs. This visual representation of the program and the system within which it sits, really helped me understand how the classes interact with the database_connection file and the database to request and receive information. Diagrams are really useful as they are easier to digest, enable people to see how the different components of an app are working and make it easier to see how different components interact with each other. 

I learned to use a recipe template to design a single table based on user stories. I first extracted the nouns, then inferred the table name and columns, decided column types, write SQL that creates the table and write the command that creates the table in the database. 

Once I completed my design, I created a database by writing 'createdb <database_name>' in the terminal, then I copied the SQL code into a file which allowed me to create a table into the newly formed database by writing psql -h 127.0.0.1 student_directory_1 < students_table.sql. 

<h3>Thursday 5th October</h3>

I practised using the design recipe today, creating a new database and adding a table to it. I test-drove a single [recipes table](https://github.com/sandrasoi/recipe_directory/tree/main) by creating a model and repository class that contained a couple of methods. This program showed all the recipes within the table and allowed a specific recipe to be extracted. 

<h3>Friday 6th October</h3>

I designed a [blog](https://github.com/sandrasoi/blog) program that contains two tables. I learned how to figure out the relationship between the two tables, posts and comments. I had an issue where two appearing identical objects were different. After debugging, I figured out that the data type of one of the data types was different. This was because I added it to the table incorrectly. 

I added a create and delete method to my Album Repository class.


This was a very good module where I learned how to design database schema and create the database using SQL, use SQL to query a database, how to integrate a database to a program by test-driving model and repository classes, and create a diagram for a program to understand the interactions between classes and the database. 
