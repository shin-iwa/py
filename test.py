class Student:
  def avg(self,math,english):
      print((math + english)/2)

  def __init__(self):
    self.name = ""

a001 = Student()
a001.name = "sato"
print(a001.name)

a002 = Student()
a002.name = "tanaka"
print(a002.name)