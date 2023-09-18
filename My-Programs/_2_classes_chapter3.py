# == INSTRUCTIONS ==
#
# In these exercises you will build small classes.
#
# The first ones will be familiar, do them without looking at your previous
# work. The later ones will be more complex.
#
# Here is an example of some exercise instructions and a solution.
#
# Class name: ExampleGreeter
# Purpose: say hello and goodbye to a user with a given name


# Methods:
#   1. Name: __init__
#      Arguments: one, a string representing a name
#   2. Name: say_hello
#      Arguments: none
#      Returns: a string like 'Hello, NAME!'
#   3. Name: say_goodbye
#      Arguments: none
#      Returns: a string like 'Goodbye, NAME!'
# Example usage:
#   > greeter = ExampleGreeter('Bobby')
#   > greeter.say_hello()
#   'Hello, Bobby!'
#   > greeter.say_goodbye()
#   'Goodbye, Bobby!'
#
# Example solution:
# class ExampleGreeter():
#     def __init__(self, name):
#         self.name = name
#     def say_hello(self):
#         return 'Hello, ' + self.name + '!'
#     def say_goodbye(self):
#         return 'Goodbye, ' + self.name + '!'



# == EXERCISES ==

class Greeter():
    def hello(self,name):
        return f"Hello, {name}!"

    def goodbye(self, name):
        return f"Goodbye, {name}!"

    def good_night(self, name):
        return f"Good night, {name}!"
    
    def good_morning(self, name):
        return f"Good morning, {name}!"
    


# Class name: Greeter
# Purpose: say various greetings to a user with a given name
# Methods:
#   1. Name: hello
#      Arguments: one, a string representing a name
#      Returns: a string like 'Hello, NAME!'
#   2. Name: goodbye
#      Arguments: one, a string representing a name
#      Returns: a string like 'Goodbye, NAME!'
#   3. Name: good_night
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good night, NAME!'
#   4. Name: good_morning
#      Arguments: one, a string representing a name
#      Returns: a string like 'Good morning, NAME!'
# Example usage:
#   > greeter = Greeter()
#   > greeter.hello('Bobby')
#   'Hello, Bobby!'
#   > greeter.goodbye('Bobby')
#   'Goodbye, Bobby!'
#   > greeter.good_night('Bobby')
#   'Good night, Bobby!'
#   > greeter.good_morning('Bobby')
#   'Good morning, Bobby!'


class Basket():
    def __init__(self):
        self.list_of_items = []

    def add(self, item):
        self.list_of_items.append(item)

    def list_items(self):
        return self.list_of_items

# Class name: Basket
# Purpose: store a list of items
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: one item of any type
#      Returns: nothing
#   3. Name: list_items
#      Arguments: none
#      Returns: a list of all the items that have been added
# Example usage:
#   > basket = Basket()
#   > basket.add('apple')
#   > basket.add('banana')
#   > basket.add('orange')
#   > basket.list_items()
#   ['apple', 'banana', 'orange']



# Class name: Calculator
# Purpose: perform simple calculations and track the history

class Calculator():

    def __init__(self):
        self.calculations = []

    def add(self, number1, number2):
        self.calculations.append(number1+number2)
        return number1 + number2
    
    def multiply(self, number1, number2):
        self.calculations.append(number1*number2)
        return number1 * number2
    
    def subtract(self, number1, number2):
        self.calculations.append(number1-number2)
        return number1 - number2
    
    def divide(self, number1, number2):
        self.calculations.append(number1/number2)
        return number1 / number2
    
    def list_history(self):
        return self.calculations
    


# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Arguments: two numbers
#      Returns: the result of adding the two numbers
#   3. Name: multiply
#      Arguments: two numbers
#      Returns: the result of multiplying the first by the second
#   4. Name: subtract
#      Arguments: two numbers
#      Returns: the result of subtracting the second from the first
#   5. Name: divide
#      Arguments: two numbers
#      Returns: the result of dividing the first by the second
#   6. Name: list_history
#      Arguments: none
#      Returns: a list of all the previous results calculations
# Example usage:
#   > calculator = Calculator()
#   > calculator.add(1, 2)
#   3
#   > calculator.multiply(3, 4)
#   12
#   > calculator.subtract(5, 6)
#   -1
#   > calculator.divide(7, 8)
#   0.875
#   > calculator.list_history()
#   [3, 12, -1, 0.875]



# Class name: Cohort
# Purpose: store a list of students

class Cohort():
    def __init__(self):
        self.dictionary_of_all_students = []

    def add_student(self, dictionary_per_student):
        self.dictionary_of_all_students.append(dictionary_per_student)

    def list_students(self):
        return self.dictionary_of_all_students
    
    def list_employed_by(self, name_of_employer):
        return [dictionary for dictionary in self.dictionary_of_all_students if dictionary['employer']== name_of_employer]


# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add_student
#      Arguments: one dictionary representing a student
#      Returns: nothing
#   3. Name: list_students
#      Arguments: none
#      Returns: a list of all the students that have been added
#   4. Name: list_employed_by
#      Arguments: one string, the name of an employer
#      Returns: a list of all the students who work for that employer
# Example usage:
#   > cohort = Cohort()
#   > cohort.add_student({'name' : 'Jo', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Alex', 'employer' : 'NASA'})
#   > cohort.add_student({'name' : 'Bobby', 'employer' : 'Google'})
#   > cohort.list_students()
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}, {'name' : 'Bobby', 'employer' : 'Google'}]
#   > cohort.list_employed_by('NASA')
#   [{'name' : 'Jo', 'employer' : 'NASA'}, {'name' : 'Alex', 'employer' : 'NASA'}]





class Person():
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get_work_address(self):
        address_dictionary =  self.dictionary['addresses']
        work_address = [dictionary for dictionary in address_dictionary if dictionary['name']== "work"][0]
        return f"{work_address['building']} {work_address['street']}"
        #return [dictionary for dictionary in address_dictionary if dictionary['']]
        #return type(work_address)

    def get_home_address(self):
        address_dictionary =  self.dictionary['addresses']
        home_address = [dictionary for dictionary in address_dictionary if dictionary['name']== "home"][0]
        return f"{home_address['building']} {home_address['street']}"
    
    def get_pets(self):
        name =  self.dictionary['name']
        types_of_animal = ""
        pets =  self.dictionary['pets'] 
        #return [pets[element] for element in range(len(pets))]
        for i in range(len(pets)):
            animal = pets[i]
            types_of_animal += f"a {animal['animal']} called {animal['name']}"
            print (len(pets))
            if i < (len(pets)-1):
                print(i)
                types_of_animal += ", "             

        return f"{name} has {len(pets)} pets: {types_of_animal}"
    
person = Person({
        'name' : 'Alex',

        'pets' : 
        [   {'name' : 'Arthur', 'animal' : 'cat'},
            {'name' : 'Judith', 'animal' : 'dog'},
            {'name' : 'Gwen', 'animal' : 'goldfish'}],

        'addresses' : 
        [   {'name' : 'work', 'building' : '50', 'street' : 'Commercial Street'},
            {'name' : 'home', 'building' : '10', 'street' : 'South Street'}]
        })

#print(person)
#print(person.get_work_address())
#print(person.get_home_address())
print(person.get_pets())

# Class name: Person
# Purpose: store a person's name, pets and addresses
# Methods:
#   1. Name: __init__
#      Arguments: one complex dictionary, see below for structure.
#   2. Name: get_work_address
#      Arguments: none
#      Returns: the work address in a nice format
#   3. Name: get_home_address
#      Arguments: none
#      Returns: the home address in a nice format
#   4. Name: get_pets
#      Arguments: none
#      Returns: a nice summary of the person's pets
# Example usage:
#   > person = Person({
#       'name' : 'Alex',
#       'pets' : [
#         {'name' : 'Arthur', 'animal' : 'cat'},
#         {'name' : 'Judith', 'animal' : 'dog'},
#         {'name' : 'Gwen', 'animal' : 'goldfish'}
#       ],
#       'addresses' : [
#         {'name' : 'work', 'building' : '50', 'street' : 'Commercial Street'},
#         {'name' : 'home', 'building' : '10', 'street' : 'South Street'}
#       ]
#     })
#   > person.get_work_address()
#   '50 Commercial Street'
#   > person.get_home_address()
#   '10 South Street'
#   > person.get_pets()
#   'Alex has 3 pets: a cat called Arthur, a dog called Judith, a goldfish called Gwen'


