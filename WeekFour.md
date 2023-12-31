<h1>Week4</h1>

<h2>Goals:</h2>

- Learning to test-drive programs with multiple classes.
- Learn to break programs up into classes.
- Learn to debug your programs.
- Learn to build software as a pair.
- Learn to explain why test-driving, object-oriented design, debugging, and pairing are powerful practices for software engineers.

<h3>Monday 25th September</h3>

I began designing a mutli-class system program to store diary entries containing to-dos, phone numbers and normal entries in a diary. Given only user stories, it was very challenging to work out how many classes were needed and their relationship with each other. I found pair programming really useful as it helped me to speak out loud my thoughts and design the program. 

<h3>Tuesday 26th September</h3>

I attended a workshop on using git when pair programming. I learned how to make new branches, merge them and resolve conflicts. When pair programming, I employed this technique to solidify my understanding. I used git checkout -b <name of branch> to create a new branch and git push --set-upstream origin <branch name> to push these changes to GitHub. I have been focused on developing better practises including regularly commiting my code at key stages of development. 

<h3>Wednesday 27th September</h3>

I attended an empathy session where I learned what empathy is and its importance, how to train empathy and what the hindurances are. I learned that it's important to show empathetic concern and not affective or cognitive empathy alone. That is because in order to be most helpful we should use both our emotions and cognition when helping someone. 

I learned how to test multi-class programs by testing individual classes without relying on other classes. I first practised testing by creating fake classes that return chosen values that the tested class relies on. Then I learned about mocks and I imported Mock class that saves time by having a fake class that can be used for testing. I found these concepts really difficult to grasp and despite discussing it with a peer, simplifying the tests and going through the material, I could not make sense of this. We sought support from a coach who explained things in simple terms which helped me understand. 

<h3>Thursday 28th September</h3>

I learned about unit testing using mocks and fake classes. This allows an indiviudual class to be tested even if it requires another class to work. By creating a fake class or using mocking, we can request a certain value to return from another class that can be used within the class we are testing. This took me a little while to understand as it was quite a different concept to what I was familiar with. 

<h3>Friday 29th September</h3>

I learned how to test APIs. As we cannot control what an API returns, we can replace the requests library we are using to request the API with a mock and control what is returned. I unit tested this [TimeError class](https://github.com/sandrasoi/unit_test_API_requests) by replacing requests with self.requestor which enabled me to call a mock. I then used a mock to control what value is returned when callin the response.  

I rounded this module off with a retro where I reflected with my cohort. I felt that I managed my time a lot better during this module by taking regular breaks and allowing myself to seek help faster when I was stuck on a problem to ensure I am making progress. I have really enjoyed this module and learned a lot about test-driving classes, debugging, designing multi-class systems and pair-programming. I have found pair programming really useful in testing my understanding and speaking out loud my thought processes. I found designing a program quite challenging and I hope to get more comfortable doing this.
