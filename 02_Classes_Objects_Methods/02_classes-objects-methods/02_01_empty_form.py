# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.


class Doctor:

    def __init__(self, name, age, malady) -> None:
        self.name = name
        self.age = age
        self.malady = malady
        applicant_name = self.name
    
    def __str__(self) -> str:
        return f"\nName: {self.name}\nAge: {self.age}\nMalady: {self.malady}\n"
    
    def name_prompt(self):
        answer = input("\nHello there. Let's get started.\nWhat's your name?\n > ")
        self.name = answer.capitalize()
        return print(f"Thanks, {self.name}!\n")

    def age_prompt(self):
        applicant_name = self.name
        answer = input(f"\nHow old are you, {applicant_name}?\n > ")
        self.age = int(answer)
        return print(f"Thanks, {self.name}!\n")
    
    def malady_prompt(self):
        answer = input(f"\nWhat is your malady?\n > ")
        self.malady = answer
        return print(f"Yikes, {self.name}! Well, we'll see what we can do...\n")
    

# List of Prompts:
# from <file.py> import Doctor
        # (Original lab file name "02_01_empty_form.py"
        # cannot be imported from. Must rename file
        # for import, and with it, replace "<file.py>")

applicant = Doctor(name="J. Doe", age=0, malady="condition")
applicant.name_prompt()
applicant.age_prompt()
applicant.malady_prompt()
print(f"\nAlright. Here's what we've recorded:\n{applicant}")

