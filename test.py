def avr(a, b, c):
  return (a + b + c)/3

def unit(a, b, c):
  return (a + b + c)

print(avr(9, 10, 2))

print(unit("hana", "mizu", "ki"))

class Student:
  def __init__(self,name,greeting):
    self.name = name
    self.greeting = greeting

  def avg(self, math, english):
    print((math + english)/2)

a001 = Student("sato", "hello!")
print(a001.name + " " + a001.greeting)

a002 = Student("tanaka", "good mornig!")
print(a002.name + " " + a002.greeting)

