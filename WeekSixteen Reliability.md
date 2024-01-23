<h1>Week16 Reliability </h1>

<h2>Goals:</h2>

- Learn to improve and upgrade a system with minimal compromise to availability.
- Explain the importance of observability in a system.
- Learn to make a system more observable.
- Learn to resolve security issues in a running system.

<h3>Monday 8th January</h3>

Review of what we accomplished before the break in preparation for end of bootcamp presentation.

<h3>Tuesday 9th January</h3>

<h3>Wednesday 10th January</h3>

Today we had a large spike in traffic. As we prepared for this by caching results. Our success rate was not affected. However, we did get 2 errors. After investigating, we noticed we were getting some 403 errors which meant we had a time out. We then used threading so that a request would be made at the same time. This meant a user would get a response at the same time a note was being added with screening results. This only happened when requesting screening results and adding them to a note. This meant time was reduced and we didn’t have a time our error anymore. 

I originally thought this was because threading was putting too much load on the server.

When we made a change and added it. We got a lot of errors.
This is because all the cached data was lost when the container was stopped. Due to high traffic the server was timing out before it could cache data. As a result we needed to cache data independent of a container being stopped. We can persist data using a volume

This still did not reduce number of errors.

We switched off cloud front and authorisation headers and error rate still did not go down.

<h3>Thursday 11th January</h3>

After leaving everything overnight, our errors went down to 0. This appeared to be an issue with caching. 

Couldn’t handle higher traffic because when logging we were sending a request to server. We realised that the staff name we can get from the authorisation header, not by requesting it from the server.

Prepared for presentation

Fixing authorisation - 
Only cache authorisation from the same person for requests

Docker compose
Docker file, create volume and then add it

Reddis is memory, volume is storage

Staging build - kubernates - elastic beanstalk

<h3>Friday 12th January</h3>

PRESENTATION! LINK [HERE](https://github.com/sandrasoi/My-Makers-Journey/blob/main/My-Programs/RELIABILITY_FINAL_PROJECT.pdf)
