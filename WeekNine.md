<h1>Week9</h1>

<h2>Goals:</h2>

By the end of the week, the goal is to be able to answer "yes" to the week's primary questions:

Containerisation

Can you explain the basics of how Docker works? In particular:
What a Docker container is
What a Docker image is
What containers are useful for
What a Dockerfile is used for
What Docker Hub is used for
Can you use Docker to containerise a simple web app?
Using the Cloud

Can you illustrate a deployment process using a diagram?
Can you follow an effective process for learning to use a new Cloud service?
Can you deploy a containerised web app to AWS?
Can you gain visibility into your deployed application using logging and telemetry?

<h3>Monday 30th October</h3>
Today I reviewed the process of setting up a flask application and deploying it in a docker container. I delved deeper into the necessary components of a Dockerfile. This includes starting with a base image, in my case it was a base image to set up Python within the container. Then I needed to install the required dependencies by installing pipenv. I copied the files from the project I was working in to docker and set up the working directory. Then finally when docker is ran, I specified that I want python and my app file to run. I pair programmed a simple flask application to display "Hello World" and deployed it in docker. We then also had time for an extension task to an image upload feature to our application. The challenge was researching what command to use to persist data in a volume and how to save it outside of the container. Firstly, we needed to create a volume using: docker volume create saved_images and then we needed to run docker with the volume and then specify where we want to save the information from the folder: docker run -v saved_images:/uploads hello_cloud_world.

I learned some new commands such as 'docker ps' to see active running containers and also learned how to stop a container from running using 'docker stop' followed by container name. I figured out how to see the folder outside of the docker container as I wanted to see whether the files were being saved. I entered the docker terminal using 'docker exec -it <name of container> /bin/bash' command and the listing the files using 'ls' to see the folder. 

It was a challenging start to the module but it was a really good opportunity to review and improve my understanding of docker.

<h3>Tuesday 31st October</h3>

Today we created an EC2 instance which is a virtual machine in the cloud provided by Amazon Web Services. Once I created a pem key to access my instance, I connected to the instance using my local machine using ssh that contained the path to my pem key and the details to get to the ec2 instance including its IP address. 
I also had to set permissions using chmode 0600 on the pem key file before it could be used. 

My task was then to research and learn how to transfer the containerised image from the local machine to the instance. I used ChatGPT a lot to help me figure this out. The steps were quite simple once I understood what was happening. I had to first encapsulate the image into a tarball file using docker command 'docker export <image name>  > <name of tarball file>'. I then transferred this file from my local machine to the ec2 instance using scp and then transfer it to the ec2 instance. This initially didn't work as I needed to use the pem key again to access the ec2 instance. I transferred the file using 'scp -i <pem_key>.pem <tar_file>.tar ec2-user@<IP_ address>:~/<tar_file>.tar'. I then accessed the ec2 instance using the ssh command again and loaded the image using 'docker load -i <tar_file>'. This however, did not work, after some investigation I figured out that I wasn't trying to load the image but the container as I saved the container as a tar file not the image. I completed the steps again and loaded the image to ec2.

This was a really good learning opportunity as there was a lot of trail and error, and figuring things out which helped me test my understanding.

<h3>Wednesday 1st November</h3>

Today I learned how to deploy my application using Elastic Beanstalk which is part of AWS. Elastic Beanstalk abstracts a lot of infrastructure away allowing the user to focus on their application. In order to deploy the application, I learned a different way of transferring docker images, which was using Docker Hub. This method consists of uploading the docker image to Docker Hub which is available online. In order to save the image in Docker Hub, I first signed up to Docker Hub, then I had to 'tag' my image locally using docker tag 'hello_cloud_world:latest sandrasoi/hello_cloud_world:tagname' and then I was able to push the image to repository I created on Docker Hub using 'docker push sandrasoi/hello_cloud_world:tagname'. 

Then I set up the application and environment within Beanstalk and uploaded the docker image. However, this did not work. I did a lot of troubleshooting and researching where my error could be. I loaded a different publicly available docker image and that did work so it led me to conclude there was an issue with my image. I downloaded the image back from DockerHub and ran it locally and it worked. I then decided to follow the steps from the beginning and set up a new application within Beanstalk. I uploaded the image straight away as previously I tried to set it up after creating the application. This made all the difference and it allowed my application to run on the browser. 
