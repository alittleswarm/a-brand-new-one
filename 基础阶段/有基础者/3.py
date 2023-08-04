# 写一个列表推导式，生成一个5*10的矩阵，矩阵内的所有值为1，再写一个列表推导式，把这个矩阵转置
list = [([1]*5) for x in range(10)]
list_reverse =[[1]*10 for x in range(5)]
print(list,'\n',list_reverse)