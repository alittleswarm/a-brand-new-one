# 输入⼀个列表（list），列表中含有字符串和整数，删除其中的字符串元素，然后把剩下的整数升序排序，输出列表
l=input('请输入一个列表：（元素间用空格分割）')
l=l.split(' ')
for x in range(len(l)-1,-1,-1):
    if l[x].isdigit():
        l[x]=int(l[x])
    else:
        l.pop(x)
l.sort()
print(l)