# 写一个正则表达式，用于验证用户密码，长度在6~18 之间，只能包含英文和数字
import re
while True:
    passwd =input('请输入密码:')
    flag =re.match(r"^[0-9a-zA-Z]{6,18}$",passwd)
    if flag:
        break
    print("格式错误，请重新输入")

print("OK")