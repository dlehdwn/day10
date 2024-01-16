#함수:코드를 모아놓은 묶음
#파이썬 커스터마이즈 함수
def add(x,y):
    result = x+y
    return result
b = int(input("x를 입력해 주세요:"))
c = int(input("y를 입력해 주세요:"))
a = add(b,c)
print(a)

def min(x,y):
    result = x-y
    return result
a = min(4,3)
print(a)

def mul(x,y):
    result = x*y
    return result
a = mul(4,3)
print(a)

q = int(input("정수를 입력하세요:"))
def a(x):
    b = x%2
    if b == 0:
        return "짝수 입니다"
    if b == 1:
        return "홀수 입니다"
c = a(q)
print(c)


def makelistdict(xlist,ylist,xkey,ykey):
    return [{xkey:x,ykey:y} for x,y in zip(xlist,ylist)]

coffee = ['아메리카노','라떼','비닐라']
price = [2500,3000,3500]

a = makelistdict(coffee,price,'커피','가격')
print(a)
#[{'커피': '아메리카노', '가격': 2500}, {'커피': '라떼', '가격': 3000}, {'커피': '비닐라', '가격': 3500}]


def makelistdict(xlist,ylist,xkey='item',ykey='price'):
    return [{xkey:x,ykey:y} for x,y in zip(xlist,ylist)]

coffee = ['아메리카노','라떼','비닐라']
price = [2500,3000,3500]

a = makelistdict(coffee,price)
print(a)
# [{'item': '아메리카노', 'price': 2500}, {'item': '라떼', 'price': 3000}, {'item': '비닐라', 'price': 3500}]



