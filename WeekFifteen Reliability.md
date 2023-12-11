<h1>Week15 Reliability </h1>

<h2>Goals:</h2>

- Learn to improve and upgrade a system with minimal compromise to availability.
- Explain the importance of observability in a system.
- Learn to make a system more observable.
- Learn to resolve security issues in a running system.

<h3>Monday 11th December</h3>

Today we were put into groups to work on the Reliability module which is our final end of course project. Our task it resolve issues that a veterinary hospital is experiencing such as slow, unreliable or offline service. We are working as an intermediate team with only access to the loadbalancer that controls traffic to the app which is stored on a web server that we don't have access to. We can send requests to the API to get information such as staff details, notes about patients or hospital details. 

We started by monitoring traffic that goes to the API by checking the dashboard and noticed that some requests were failing. We did not know why this was happening or which requests were failing. In order to gain visibility, we enabled monitoring logs on the loadbalancer. Logs had to be stored in an S3 bucket so we set this up by allowing permissions to the loadbalancer and set up the logs. We then viewed the logs and noticed that there were 404 and 500 errors. 404 errors related to requests to sites that did not exist. 500 errors related to server related issues.

Our plan is to direct traffic from the balancer to an application that verifies whether requests are valid and then passing them to the API. This should reduce errors as only requests that can be managed by the API will be sent.

Today we also set up a listener to enable traffic from HTTPS as this is a more secure method. In order to achieve this we had to create a certificate and then use it for the listener.

<h3>Tuesday 12th December</h3>
