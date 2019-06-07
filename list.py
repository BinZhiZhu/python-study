# -*- coding: utf-8 -*


# 列表
list=[1,2,3,4,4]
print(list)
print(list[2])
print(list[0:2])

# 追加
list.append(5)
print(list)

# 删除最后一个
list.pop()
print(list)

# 长度
print(len(list))

# 插入指定位置
list.insert(1,9)
print(list)
print(list[1])

# 直接赋值
list[0]=[1,2]
print(list)

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

classmates = ('A','B','C','D')
print(classmates)


