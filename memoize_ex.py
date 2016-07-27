"""
장식자를 만드는데
1) 숫자만 인자로
2) 인자는 무제한
3) 인자들을 절댓값 처리
4) mysum1(x, y, z) = |x| + |y| + |z| 되게 하기
"""

def absolute(fn):
    def wrap(*args):
        mylist = [abs(x) for x in args]
        return fn(*mylist)
    return wrap

@absolute
def mysum(*args):
    return sum(args)

print(mysum(-10, 1, 3, -3, 4, 101))