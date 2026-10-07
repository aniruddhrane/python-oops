class Employee:
  #__init__ is like java /C__ constructor
  def __init__(self,name,role):
    self.name=name
    self.role=role

  def get_details(self):
      return f"{self.name} works as a {self.role}"

  emp1=Employee("Aniruddha","Backend Developer")
  print(emp1.get_details())
