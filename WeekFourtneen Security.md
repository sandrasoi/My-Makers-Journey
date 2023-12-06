<h1>Week14 Security </h1>

<h2>Goals:</h2>

- Explain the importance of security and its implications
- Use SAST and DAST tools to uncover security risks
- Use the practice of Threat Modelling to uncover security risks in a deployed application

<h3>Monday 4th December</h3>

I have focused today on understanding different security risks in an application. Injections are a big risk where someone with malicious intent could submit a form with code that hacks the system. In order to prevent that, the code has to validate against user inputs. It's also important not to store any sensitive enough in the HTML code which can be accessed by others. It also must not be easy to guess routes that could cause damage to the application such as commands to delete information collected. Debug mode has to be disabled as to not make it easy for hackers to figure things out about the application based on the error messages received. 

<h3>Tuesday 5th December</h3>

Today I worked in a pair to go through a node.js app and identify security issues. I did this by looking at the issues which I researched yesterday and using different tools such as bearer and zap. For example, when my account is accessed, it includes a number in the URL, changing this number gives me access to other users details. The session cookie encryption is not secure, it uses the key 'SECRET' to encrypt which a hacker can guess. Bearer suggested using Helmet as middleware to obscure some header details. 

Looking at the infrastructure, the S3 buckets that store website assets and the logs are publicly available. The permissions associated with the buckets allow for any changes to the bucket. Similarly, the EC2 instance is not secure as it allows access from all ports. Loadbalancer also allows traffic from all when it should only allow the EC2 instance access. It also uses HTTP 80 which is not as secure as HTTPS 443.

This was a good exercise to identify various security issues.

<h3>Wednesday 6th December</h3>


<h3>Thursday 7th December</h3>

<h3>Friday 8th December</h3>


