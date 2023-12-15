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

create a flask app that can validate requests sent and then sends it to web server
create git repository to create flask app
set up ec2 
set up jenkins on ec2
set up webhook and pipeline on jenkins
pipeline needs to copy repository, and build image and run docker. we need to stop containers at each deployment

<h3>Wednesday 13th December</h3>

validate against 404 errors
flask app contains the different requests such as GET, POST, PATCH, DELETE
    then app validates for the right data type, authorization included

<h3>Thursday 14th December</h3>

manage 500 errors

<h3>Friday 15th December</h3>

Our next task was to only allow https connections to make sure the information is sent securely. To only allow https requests we first tried to forward all requests from listener 80 to listener 443 on our loadbalancer, that didn't work as data was already transferred via http over the internet we needed to find a way to force a https connection from the client side. After some research we discovered that is something cloudfront handles currently route 53 directs traffic to the load balancer. we needed to route traffic from route 53 to cloud front and cloud front to loadbalancer. This proved tricky as we couldn't figure out how the traffic is getting directed. after some looking we noticed route53 has a CNAME that routes traffic to loadbalancer. We set up cloud front and once that was set up, tested it by connecting to it from the terminal this worked we then changed where traffic is directed on route 53 to cloudfront. We started getting errors and after sending a request from the terminal, realised the error was due to a missing authorization header this meant that cloudfront was losing the authorization header that is required to connect with our server after some research we found a way to cache data stored by authorization header and got around this issue.

