from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

from examples import custom_style_3

print("Hi, welcome to Python Class")
print("Select an exercise and hit Enter to begin")

modules = [
    {
        'type': 'list',
        'name': 'option_selected',
        'message': "",
        'choices': ['Introduction to Python'
                    'Comment your Python code',
                    'Variable and Data Types', 
                    'Working with Numbers', 
                    'Getting input from users', 
                    'Lists', 
                    'Tuples',
                    #'Functions,
                    'If Else',
                    'Dictionary', 
                    'Loops', 
                    'Nested Lists',
                    'Try/Except', 
                    'Reading/Writing Files', 
                    'Modules and pip', 
                    'Classes and Objects', 
                    'Inheritence',
                    "\n",
                    'HELP',
                    'CHOOSE LANGUAGE',
                    'CREDITS',
                    'CHECK FOR UPDATE',
                    'EXIT'],
        'filter': lambda val: val.lower()
    }
]
def selection :
    module_selection = prompt(modules, style=custom_style_3)
    return module_selection