<h1>Week11</h1>

<h2>Goals:</h2>

By the end of the week, the goal is to be able to answer "yes" to the week's primary questions:
- Do you have a solid knowledge of IAM in AWS? You can explain the following concepts: users, groups, policies and roles
- Can you work as part of a team to build your own CI-CD solution using GitHub Actions?
- Can you work as part of a team to deploy an existing application on EC2?
- Can you apply security best practices around credentials and token storage?
- Are you more familiar now with potential connectivity issues that may arise as part of your system design and architecture?


<h3>Monday 13th November</h3>

Today was focused on figuring out what the application does. The main way of doing this was to set up the application locally and see what it looks like. In order to run it, I needed to set up Node.js as this application runs on Node.js. Then I downloaded ESLint for VSCode in order to run tests and installed mongodb. This then allowed me to run tests and run the server to view the application in the browser. I also looked at the various files to make sense of their functions. 

Setting up node, eslint, getting app running in browser.

<h3>Tuesday 14th November</h3>

The first step of deploying this application to AWS, is to set up GitHub actions. This works similarly to Jenkins as it enables the pushed code to be tested. GitHub actions is set up using a main.yml file that builds and sets up the environment and tests the application. This required looking through documentation and figuring out how to set up node, install dependencies, set up mongo database, and run Jest and Cypress tests. 

The next step was to set up the EC3 bucket. I diagrammed the process of pushing code to GitHub, then GitHub needs to deploy the code to EC3 bucket. I learned that can be also done using yml file. I also diagrammed the permissions required for the deployment to EC3 bucket (such as editing access). Here is the diagram I created to visualise this steps: [here.](https://github.com/sandrasoi/My-Makers-Journey/blob/main/My-Programs/githubactions.png)

<h3>Wednesday 15th November</h3>

I created the code required to push files from github to bucket. I created IAM roles and users to give permission to those users to access the bucket and ec2 instance.

A lot of today was spent figuring out how codedeploy works, what the codedeploy agent does and how to push files from the bucket to ec2 instance. We figured out that codedeploy doesn't have a trigger to start deployment to ec2 instance. We researched about the trigger and realised we need to add specific deployment code. 

<h3>Thursday 16th November</h3>
Today we spent implementing the code we found to deploy the bucket to the EC2 instance. We got several different errors during our deployment efforts and debugged each one. One of the last errors that we did not spot despite working in a group of 3 was a lack of a space at the end of a sentence and before a forward slash. This made me learn a really valuable lesson of looking at formatting patters in code and make sure everything is correct. Once we added this space, codedeploy was triggered and a deployment attempt started. This, however, still did not work in setting up the instance. We continued working on this the next day. 

<h3>Friday 17th November</h3>

Today we spent time diagramming the problem and redoing the whole process to really understand what was happening. This helped us as we forgot how codedeploy talks with the EC2 instance and how the deployment occurs. When codedeploy is set up, we give it the key-value pair associated with the instance, and we also set up codedeploy agent on the instance. We checked that codedeploy works properly on the instance to make sure that is not the problem. Altough all this troubleshooting and diagramming was really useful, it still didn't help us figure out our problem and with the module coming to an end, we had a final workshop to go through all the steps and figure out where we went wrong. 
