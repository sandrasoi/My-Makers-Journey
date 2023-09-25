<h1>Week3</h1>

<h2>Goals:</h2>

- Learning to test-drive programs with multiple classes.
- Learn to break programs up into classes.
- Learn to debug your programs.
- Learn to build software as a pair.
- Learn to explain why test-driving, object-oriented design, debugging, and pairing are powerful practices for software engineers.


<h3>Monday 18th September</h3>

Today is the beginning of a new module where I will learn about the golden squares of programming:
- Test-driving
- Object Oriented Design
- Debugging
- Pairing

Today I revised my understanding of git by cloning a repository from GitHub and setting up a git repository on my computer. I learned how to write tests for simple programs and how to write a test when an 'Exception' is used in the program. I learned about the differences between freerunning development and test-driven approach. The test-driven approach consists of a red phase, green phase and then refactoring phase. I created simple programs using this test-driven approach. 

<h3>Tuesday 19th September</h3>

I worked in a pair today to complete a test [driven challenge](https://github.com/sandrasoi/Phase_Two_Challenge_3). The requirement was for the user to know how long it will take them to read a text based on their reading time and the length of the text. Together we created a plan that contained the what the problem was, designed the function signature such as the name, paramenters and return values, created example tests and then finally implemented this changes. We created a new repository to allow us to take turns working on the code, by pushing them to GitHub and pulling them from GitHub. Collaborating with others is a very useful tool as it allows me to see different ways of working and helps me become a better coder. 

<h3>Wednesday 20th September</h3>

I learned about two types of debugging: change and discovery debugging. Change debugging consists of making changes to the program and seeing what effect it has. This can work well in simple programs but when a program is complex, this is not a good method. Instead it is important to do discovery debugging which consists of understanding how the code executes, flow of control, which ifs and loops run and how many times, values of variables and how they change. A powerful tool to gain insight into the code is to gain visibility by running 'print' statements. I successfully debugged an [encoder_decoder program](https://github.com/sandrasoi/My-Makers-Journey/blob/main/My-Programs/Golden_Squares_Module/encoder_decoder.py) which I have never seen before by using this methodical approach. Firstly, I was getting an error that 'a' does not exist in the list. I printed the 'alphabet' variable and noticed that the alphabet starts at c not a, therefore, I fixed the code so that the list would start from a. Secondly, the decoder function was not decoding correctly. I understood how the encoder function works and based on that I discovered where the error was in the decoder function and fixed it.

I also did pair programming where I created a [program with a single class](https://github.com/sandrasoi/my_project_golden_square/blob/main/lib/diary_entry.py) using test-driven development. This class calculated how long it would take to read a diary entry, how much can be read in a certain amount of time given a certain reading speed and show the next reading chunk once the previous was read. The value of working in a pair was evident when I did not know how to save and loop through the next section of the diary entry. My pair found a really good solution of adding read content to a list and I figured out how to slice the whole reading material to start from the first unread word to the next word that could be read within the specified time. This joined up work enabled us to push each other to complete the exercise fasterby and within the end of the day.

<h3>Thursday 21st September</h3>

I solidified my test driven development by designing two programs containing single classes. I followed a design recipe to design the class interface and examples of tests. Using this approach I programmed a [single Tasks class](https://github.com/sandrasoi/my_project_golden_square/blob/main/lib/task.py) that enabled user to add tasks, view tasks and mark them as complete. I also created a similar program that contained a [single Playlist class](https://github.com/sandrasoi/my_project_golden_square/blob/main/lib/playlist.py) which allowed user to add songs and view songs. 

I learned another technique for discovery debugging using an interactive debugger in VSCode. This is a really useful tool as it shows the current variables and their values and stops at each line to give visibility into what is happening at each stage of the code. This enabled me to debug a vowel remover program as it was iterating over a modified list and as a result skipping over some strings in the text. I also debugged another program which calculated the most common letter in a string. The interactive debugger was quickly able to show me that the program was initialising the first instance of a letter to 2 instead of 1. 

<h3>Friday 22nd September</h3>

I began [test driving](https://github.com/sandrasoi/my_project_golden_square/blob/main/tests/test_todo_integration.py) a multi-class program containing a [todo class](https://github.com/sandrasoi/my_project_golden_square/blob/main/lib/todo.py) and a [todo_list class](https://github.com/sandrasoi/my_project_golden_square/blob/main/lib/todo_list.py). This is very similar to test driving a single class program but it's important to consider how the multiple classes interact with each other and to test that they behave in the correct way. The program enabled users to add to-dos, mark them as complete and view all the complete and incoplete to-dos. I pair-programmed this program which I found really useful. For one of the tests, we could not get it to pass so we printed different parts of the code and they were all printing the correct outcome. I suggested that we assign a variable to the intended return outcome and return that variable. This worked because the calculation had to be completed first before returning it. 
