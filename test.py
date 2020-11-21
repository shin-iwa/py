class Student:
  def avg(self,math,english):
      print((math + english)/2)

  def __init__(self,name):
    self.name = name

a001 = Student("sato")
print(a001.name)

a002 = Student("tanaka")
print(a002.name)