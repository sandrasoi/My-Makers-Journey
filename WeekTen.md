<h1>Week10</h1>

<h2>Goals:</h2>

By the end of the week, the goal is to be able to answer "yes" to the week's primary questions:

CI-CD

Can you illustrate your CI-CD pipeline using a diagram?
Can you work as part of a team to build your own CI-CD solution using Jenkins?
Can you work as part of a team to deploy a static website on AWS using your own CI-CD solution?
Can you follow an effective process for learning to use new DevOps tooling and Cloud services?
Serverless

Can you work as part of a team to add a basic Serverless backend to your website?

<h3>Monday 6th November</h3>

This week is focused on learning about continuous integration and continuous deployment. Today I set up S3 on AWS which is an object storage service. I had to change the bucket policy to enable public access to this storage. This enabled me to upload a static webpage and view it online. 

I then learned to set up a Cloud Formation stack. Cloud Formation is used to build and manage the infrastructure that we require. I then connected to the stack locally using the ssh command followed by -i, pem key and the DNS. I created a diagram to improve my understanding of how the bucket and Cloud Formation work together. 

<h3>Tuesday 7th November</h3>

I set up Jenkins on my instance which is a tool that connects to a GitHub repository and when the repository is updated, Jenkins runs tests and if they pass, integrate the changes to the S3 bucket. It was a good challenge as the instructions suggested using a tool called dnf to download Java, however, after some research my pair and I discovered that the operating system that we were using (Amazon Linux 2) was not compatible with dnf and we had to use another tool called yum to install Java. Java was necessary as this is what Jenkins runs on. 

<h3>Wednesday 8th November</h3>

Today was spent setting up the Pipeline that connected GitHub to Jenkins and my EC2 instance. This was a bit of a challenge as it required setting up AWS credentials and GitHub credentials to establish a connection. I also set up a webhook which means whenever there is a push to GitHub repository, GitHub informs Jenkins of this change. My next step is to learn how Jenkins can then update this change in my S3 bucket.

<h3>Thursday 9th November</h3>

I learned to set up a lambda function on AWS and then an API endpoint. I had to set up CORS which give permissions only to a site I specify to be able to access the lambda function. I then linked this to my static page to allow the function to be performed. I learned an important lesson which was that CORS needs access to the S3 bucket in which the site is located not the site itself. This is because when permissions are given to the bucket, lambda can list of the elements and select the correct one but when permissions are only set for the site, lambda can't list all the files and can't find the correct one. 

<h3>Friday 10th November</h3>

This is the [diagram](https://github.com/sandrasoi/My-Makers-Journey/blob/main/My-Programs/project_summary_diagram.png) we have worked on throughout this week to visualise what is happening. 


