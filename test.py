def avr(a, b, c):
  return (a + b + c)/3

def unit(a, b, c):
  return (a + b + c)

print(avr(9, 10, 2))

print(unit("hana", "mizu", "ki"))

class Student:
  def avg(self, math, english):
    print((math + english)/2)

a001 = Student()
a001.avg(80, 60)