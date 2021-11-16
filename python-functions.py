# Challenge 1

def sum_to(n):
  count = 0
  for n in range(1, n + 1):
    count += n
  print(count)

sum_to(6)
sum_to(10)










# Challenge 2
def largest(list):
  max = list[0]
  for n in list:
    if n > max:
      max = n
  print(max)
  

largest([1, 2, 3, 4, 0])
largest([10, 4, 2, 231, 91, 54])










# Challenge 3
def occurances(str1, str2):
  print(str1.count(str2))

occurances('fleep floop', 'e')   # returns 2
occurances('fleep floop', 'p')   # returns 2
occurances('fleep floop', 'ee')  # returns 1
occurances('fleep floop', 'fe')  # returns 0












# Challenge 4
def product(*num):
  sum = 1
  for n in num:
    sum = sum * n
  print(sum)

product(-1, 4) # returns -4
product(2, 5, 5) # returns 50
product(4, 0.5, 5) # returns 10.0