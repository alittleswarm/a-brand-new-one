# 输入三个整数x,y,z，请尝试用多种方式把这三个数由大到小输出
s = input('请输入三个整数')
s = s.split(" ")
for i in range(len(s) - 1, -1, -1):
    if s[i] == '':
        s.pop(i)
# 冒泡排序（只会这个


# for x in range(len(s)):
#     for y in range(len(s)):
#         if s[x] > s[y]:
#             t = s[y]
#             s[y] = s[x]
#             s[x] = t

# 牛马穷举
if s[0] < s[1]:
    t = s[0]
    s[0] = s[1]
    s[1] = t
    if s[1]<s[2]:
        t =s[1]
        s[1]=s[2]
        s[2]=t
        if s[0] < s[1]:
            t = s[0]
            s[0] = s[1]
            s[1] = t
else:
    if s[1]<s[2]:
        t =s[1]
        s[1]=s[2]
        s[2]=t
        if s[0] < s[1]:
            t = s[0]
            s[0] = s[1]
            s[1] = t


print(s)
