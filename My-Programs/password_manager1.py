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
#   3. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#   4. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# We recommend that you store the passwords in a dictionary, where the keys are
# the service names and the values are the passwords.
#
# Example usage:
#   > password_manager = PasswordManager()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.get_for_service('not_real')
#   None
#   > password_manager.get_for_service('twitter')
#   None
#   > password_manager.list_services()
#   ['gmail', 'facebook']
#

# == YOUR CODE ==

def are_special_chars_included(password):
    symbols = ('!', '@', '#', '$', '%','&')
    if "!" in password or "@" in password or "$" in password or "%" in password or "&" in password:
        return True
    else:
        return False


def is_sufficient_length(password):
    # len(password) > 7 will evaluate to True or False
    return len(password) > 7


def is_valid(password):
    return is_sufficient_length(password) and are_special_chars_included(password)

dict = {}
class PasswordManager():
    def __init__(self):
        pass

    def add(self, service_name, password):
        if is_valid(password):
            dict[service_name] = password
        else:
            pass


    def get_for_service(self, service_name):
        if dict.get(service_name):
            return dict.get(service_name)
        

    def list_services(self):
        return dict.keys()

password_manager = PasswordManager()
password_manager.add('gmail', '12ab5!678')
password_manager.add('facebook', '$abc1234')
password_manager.add('twitter', '12345678') 
print(password_manager.get_for_service('gmail'))
print(password_manager.list_services())
