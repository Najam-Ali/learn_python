# Create a class "programer" for storing information about a programmer.
class Programmer:
    def __init__(self, programmer_name, programming_language, experiense_years):
        self.programmer_name = programmer_name
        self.programming_language = programming_language
        self.experiense_years = experiense_years
    def get_info(self):
        return f"Programmer Name: {self.programmer_name}, Programming Language: {self.programming_language}, Experience Years: {self.experiense_years}"
p1 = Programmer("Alice", "python", 5)
p2 = Programmer("Bob", "JavaScript", 3)
print(p1.get_info())
print(p2.get_info())