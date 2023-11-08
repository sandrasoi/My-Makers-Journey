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
