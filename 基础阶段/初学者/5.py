d = {'114514':'先辈suki','123456':'张三','123655':'李四','123648':'秦始皇','112361':'王小美'}
key_move=[x for x in d if int(x)%2==0]
for key in key_move:
    d.pop(key)
print(d)