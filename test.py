def avr(a, b, c):
  return (a + b + c)/3

def unit(a, b, c):
  return (a + b + c)

print(avr(9, 10, 2))

print(unit("hana", "mizu", "ki"))

class Student:
  def __init__(self):
    self.name = ""

  def avg(self, math, english):
    print((math + english)/2)

a001 = Student()
a001.name = "sato"
print(a001.name)

a002 = Student()
print(a002.name)

