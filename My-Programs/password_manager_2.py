# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password

#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime

def are_special_chars_included(password):
    valid_special_characters = ["!", "@", "$", "%", "&"]
    if any(letter in valid_special_characters for letter in password):
        return True
    
#def is_unique(password):
#    {key: value for (key, value) in self.dictionary_of_services_and_passwords.items() if value not in password}

def is_sufficient_length(password):
    # len(password) > 7 will evaluate to True or False
    return len(password) > 7

def is_valid(password):
    return is_sufficient_length(password) and are_special_chars_included(password)




class PasswordManager2():
    def __init__(self):
        self.dictionary_of_services_and_passwords = {}

    def add(self, service_name, password):
        if is_valid(password) and password not in self.dictionary_of_services_and_passwords.values():
            self.dictionary_of_services_and_passwords[service_name] = password
        else:
            pass
        

    def list_services(self):
        return list(self.dictionary_of_services_and_passwords.keys())
    
    def remove(self,service_name):
        del self.dictionary_of_services_and_passwords[service_name]

    def update(self, service_name, password):
        if is_valid(password) and password not in self.dictionary_of_services_and_passwords.values():
            self.dictionary_of_services_and_passwords.update({service_name: password})

    def sort_services_by(self,order_of_sorting):
        sorted_keys = []
        if order_of_sorting == "service":
            sorted_dictionary = sorted(self.dictionary_of_services_and_passwords.items(), key=lambda element: element[1])
            for dictionary_pair in sorted_dictionary:
                sorted_keys.append(dictionary_pair[0])
        return sorted_keys


        #if order_of_sorting == "added_on"

    def get_for_service(self, service_name):
        if self.dictionary_of_services_and_passwords.get(service_name):
            return self.dictionary_of_services_and_passwords.get(service_name)

            #   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists




password_manager = PasswordManager2()
password_manager.add('gmail', '12ab5!678')   # Valid password
password_manager.add('facebook', '$abc1234') # Valid password
password_manager.add('youtube', '3@245256')  # Valid password
password_manager.add('twitter', '12345678')  # Invalid password, so ignored

print(password_manager.list_services())
print(password_manager.sort_services_by('service'))