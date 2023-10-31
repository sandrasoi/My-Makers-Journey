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
