<h1>Week12 Terraform</h1>

<h2>Overview of the week:</h2>
- You'll work in teams to build your own CI-CD solution and to deploy an existing application using different AWS services.<br>
- You'll organise your own work based on the goals for the week

<h2>Goals:</h2>

By the end of the week, the goal is to be able to answer "yes" to the week's primary questions:
- Do you have a solid knowledge of IAM in AWS? You can explain the following concepts: users, groups, policies and roles
- Can you work as part of a team to build your own CI-CD solution using GitHub Actions?
- Can you work as part of a team to deploy an existing application on EC2?
- Can you apply security best practices around credentials and token storage?
- Are you more familiar now with potential connectivity issues that may arise as part of your system design and architecture?


<h3>Monday 20th November</h3>

Reviewed content from last week in high detail.

Started the new module on Terraform understanding its advantages over manually setting up instances. We met in a group and discussed how we want to work this week.

<h3>Tuesday 21st November</h3>

Today I looked through documentation and tutorials for Terraform to understand how it works. As a group, we first needed to set up an IAM user to have access to several AWS services. Using that user, we set up an S3 bucket whith versioning enabled using AWS CLI to store terraform states. This came as a bit of a challenge as we set up a bucket and we could see it on AWS but we were not getting the right message after it was set up. We realised it is because json output is not selected. Once we fixed that, we got confirmation that the bucket is set up. 
