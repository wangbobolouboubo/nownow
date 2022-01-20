# 1.添加
# $ git config --global user.name "yourName"
# $ git config --global user.email "your@email.com"
#
# 2.删除
# git config --global --unset user.name "yourName"
# git config --global --unset user.name "yourName"
#
# 看添加或删除是否成功，有两种方式：
# 【1】是控制台回车后没有报错，即成功。
# 【2】C盘 --> use(或用户) --> 电脑用户 --> .gitconfig;就可以查看。
# 是因为那个中文吗

def add(a, b):
    if a >= 0 and b >= 0:
        c = a + b
        return a + b


def mun(a, b):
    c = a - b
    return c


def chen_fa(a, b):
    c = a * b
    return c


print(add(11, 12))
print(mun(11, 5))
print(chen_fa(6, 5))


