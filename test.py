class Student:

  def __init__(self, name):
    self.name = name

  def calculate_avg(self, date):
    sum = 0

    for num in date:
      sum += num

      avg = sum/len(date)
      return avg

  def judge(self, avg):

    if(avg >= 60):
      result = "passed"
    else:
      result = "faled"
    return result

a001 = Student("sato")
