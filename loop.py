# -*- coding: utf-8 -*

# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# for x 计算【1~10】和
# 所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# 练习 求和0-100
# Python提供一个range()函数，可以生成一个整数序列

sum = 0
for x in range(101):
    sum = sum + x

print(sum)


