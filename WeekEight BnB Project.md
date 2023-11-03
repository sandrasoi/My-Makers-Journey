<h1>Week8</h1>

<h2>Goals:</h2>

- Learn to work and communicate effectively as part of a team to build a web application.
- Learn to break down projects into tasks and assign them to pairs.
- Learn to use agile ceremonies to organise your work and improve your processes.
- Learn to use the developer workflow to plan, implement and peer-review features.

<h3>Monday 23th October</h3>

Today we met in our project groups, and discussed the project requirements. Our project is to create a BnB website that allows a user to register, book a space, and list a space. This will put into practise everything we have learned in the course so far. We took the time to create user stories based on the project specification, break down the stories into smaller, actionable tickets and divided ourselves into pairs to work on the specific tickets during one sprint to achieve a minimal viable product. 

My pair and I agreed to work on creating a page that displays all the existing listings. In order to achieve this, we needed to create a database and create a way to retrieve the relevant information from the database and display it on the page. We pair programmed the database and table with me being the driver and my team member the navigator. 

The biggest challenge today was using git. We made a mistake where we all edited the main branch of the repository we were working on. This caused a lot of issues as it meant we all had a slightly different initial repository. It took us some time to learn about rebasing so that everyone had the same main branch. 

<h3>Tuesday 24th October</h3>

Today we had a stand up and discussed the progress we made in each pair. We had trouble understanding how to make sure we don't have any issues when we merge to the main branch after working off a side branch to implement some changes. We tested our understanding by pushing the changes my pair and I made to the remote and then making a pull request to merge to the main branch. Then the other pair, reviewed our code and we were able to merge to the main branch. The other pair had to pull the changes so that they were working with the latest changes.

I continued working towards completing the user story with my pair. I was navigating the driver to test-drive creating a httml page that could be rendered that contained static listings first. We then test-drove a model and repository class that connected to the database and retrieved the listings. We then test-drove the app.py to retrieve all the listings. We used ginja tags in the httml page to loop through all the listings. 

One of the challenges we came across is that the data we retrieved from the table, did not match our test. The class object that was created was wrong. To identify where this error was occuring, I asked to gain visibility by printing out the class object as a string, and it looked identical to our test. This implied the properties of something may not be matching. We tested whether the price of the listing matched against our test and what was returned from the database, and it did. We then tested whether the date the listing is available from matched, and it didn't. This showed us that we incorrectly tested the date component. We checked the syntax and fixed our test and it worked. This systematic approach to breaking down the issue really helped identify what was happening and fix it. 

The other issue we had was that when we were running a test to see whether all the listings were being displayed on the page, it worked, but when we rendered the page, it did not work. We carefully looked at the error message and it stated the table did not exist. To gain visibility, we used TablePlus which is a software that visually displays the content of a table. It turned out that our test table had information but the table that was being used to display pages was empty. This was a quick fix as we populated the table and this allowed us to render the page and see this worked. 

We checked in with the other pair to make sure they were also on track. They were in charge of creating the registering and login page. They were not sure how to test-drive navigating from the login page to the registering page. I offered to help with this as this is something I have covered before and was more familiar with the concepts. 

This marked the end of sprint 1 and we completed the retro in our team. We had positive reflections as we learned a lot about how to use git to make changes and merge them to the main branch. We practised pair programming more which is very valuable as it means there are two sets of eyes on a piece of work and issues can be spotted and fixed quicker. 

<h3>Wednesday 25th October</h3>

Today we started with a stand up where we reviewed our user stories and agreed what needs to be completed next. For my pair and I, it was to add the ability for a user to add a listing and for a user to displayed listings by date. We needed each listing to belong to a user in order to implement later features. This is not something we realised when planning and it meant we had to adjust our listing model and repository class to include a user as a property. As the other pair created the user table, we had to figure out how to link them together. We tested everything worked and that a user can add a listing on the page. We put a placeholder of user one for any listings that were added as we did not implement the ability to retrieve the user who was logged in on the page. 

<h3>Thursday 26th October</h3>

Today we focused on creating a date filter on the listings page. This would allow a user to select dates and only listings that are available during those dates would be displayed. My pair and I thought about this challenge independently as it was a difficult to visualise what needed to happen. My pair came up with an idea to splice the dates that are needed and use that to display dates. This sounded more complicated to the idea I came up with so we tried my idea to see if it would work. I figured out that the dates requested have to be greater than the first date the listing is available and less than the last date the listing is available. As simple as it sounds, we tested this using a terminal to make sure this was working as intended. Once we tested this, we were able to implement it into our code.

The next challenge came when we needed to match the date input to the date output from the database. As we came across a similar problem earlier, we were quickly able to resolve it. This problem was slightly different as the date input we used was slightly different to earlier and as a result the format of the date was different. This required slight change to code to make it work. 

<h3>Friday 27th October</h3>

The last day was spent polishing off our code such as making styling changes and making sure everything is working smoothly. We needed to change the page that a user was directed to after they logged in. We wanted them to be directed to the listings page and to include their username at the top of the page. This proved to be more challenging than expected as it was difficult to save the username and display it on the page. We researched how to save the username and fixed this issue. We then realised when a post request is sent, the username information is lost and we needed to find a new one way to save this information. We found a way to pass a hidden post request that would save the username and display it again. 

I was really happy with how everything came together on the final day. This was a really good opportunity to put into practise everything I learned throughout the course. I learned a lot about how to use git when working on a project with other people. Despite initial challenges of everyone trying to push their code to the main branch, I learned good practises of creating a new branch and merging to the main branch. It was also a really good opportunity to use agile methodology to achieve our goal. It helped us to keep on track and reflect on our progress. We worked really well collaboratively and asked for support from each other when we were stuck. Some changes we decided on were swapping who we were paired with when we identified that there were gaps in knowledge of specific topics in one pair but not the other; we also were better at breaking down the user story into tasks by creating diagrams and thinking about the problem on a deeper level.

