l=input('请输入一个列表：（元素间用空格分割）')
l=l.split(' ')
for x in range(len(l)-1,-1,-1):
    if l[x].isdigit():
        l[x]=int(l[x])
    else:
        l.pop(x)
l.sort()
print(l)