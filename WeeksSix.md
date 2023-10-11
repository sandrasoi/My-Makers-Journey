<h1>Week6</h1>

<h2>Goals:</h2>

- Explain how HTTP requests and responses work at a high level
- Write integration tests for a web application
- Implement web routes using a lightweight web framework
- Follow a debugging process for a web applicatio

<h3>Monday 9th October</h3>

I learned two basic HTTML methods GET and POST and tested my understanding of them by sending requests with arguments to a URL using curl which is a HTTP client run on the command line and POSTMAN which is also a HTTP client but with a graphical interface which makes it easier to use. 

I am using Flask which is a Python library that creates a web server which allows me to test for HTTP requests and responses. I test-drove routes to create a simple hello_web_app. Routes determine which code to execute based on the HTTML request. 

<h3>Tuesday 10th October</h3>

I put together what I learned yesterday to test-drive routes that interact with a database. This adds another layer to the complexity of the program and builds on yesterday's exercises. When a client sends a HTTP request to the flask application, the flask application will call a method in the repository class which will send a SQL query to the database. The result is returned to the repository class, which returns the value to the flask application which then sends a HTTP response to the client.

The program I created was a music_web_app that used a POST /albums route to add an album and a GET /albums route to see all the albums.

<h3>Wednesday 11th October</h3>
