class Student:
  def __init__(self,name):
      self.name = name

  def calculate_avg(self,data):
    sum = 0
    for num in data:
      sum += num

    avg =sum/len(data)
    return avg

  def jedge(self,avg):

    if(avg >= 60):
      result = "passed"
    else:
      result = "failed"
    return result

a001 = Student("sato")
data = [70, 65, 50, 90, 30]
avg = a001.calculate_avg(data)
result = a001.jedge(avg)

print(avg)
print(a001.name+" "+result)

print('I\'m a Aameican')
print(3* 'hello ' + 'world')

li1 = [1,2,3,5]
li2 = [4,6,7]
print(li1 + li2)
print(li1[0])
print(li1[0:4])
print(li1[-3:])
print(li1[::-2])
print(li1[::-1])
print(li1[:])
t = 123, 555, 150, "hello"
print(t[0])

t = 123, 456, 'hello'
print(t[1])
t2 = t, (1,2,3)
print(t2)
t3 = "hello",
print(t3)
print(type(t3))

profile = {'name':'takahashi', 'phone': '080-2222-4444'}
print(profile)
print(profile['name'])