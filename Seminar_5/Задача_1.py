# Задача 1.  В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

file = open("file1.txt", 'r')
li = [int(i) for i in file.read().split()]

for i in range(1, len(li)):
    if li[i]-1 != li[i-1]:
        print(li[i]- 1)






