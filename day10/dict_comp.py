nomalpopcorn = {
    'name': '일반팝콘',
    'price':2500,

}

coffee = ['아메리카노','라떼','비닐라']
price = [2500,3000,3500]
caffeine = [120,130,140]

#zipper
zipped = zip(coffee,price)
print(list(zipped)) # [('아메리카노', 2500), ('라떼', 3000), ('비닐라', 3500)]

result = [{'name':x,'price':y} for x,y in zip(coffee,price)]
print(result)
# [{'name': '아메리카노', 'price': 2500}, {'name': '라떼', 'price': 3000}, {'name': '비닐라', 'price': 3500}]

zipped = zip(coffee,price,caffeine)
print(list(zipped))
# [('아메리카노', 2500, 120), ('라떼', 3000, 130), ('비닐라', 3500, 140)]

result = [{'name':x,'price':y,'caffeine':z} for x,y,z in zip(coffee,price,caffeine)]
print(result)
# [{'name': '아메리카노', 'price': 2500, 'caffeine': 120}, {'name': '라떼', 'price': 3000, 'caffeine': 130}, {'name': '비닐라', 'price': 3500, 'caffeine': 140}]

# 어떤것이 몇번째에 있는지 알고 싶으면 enumerate()사용
for index,item in enumerate(coffee):
    print({f"{index}.{item}"})  # {'0.아메리카노'} {'1.라떼'} {'2.비닐라'}

a = {index:{'이름':coffee,'가격':price} for index,(coffee,price) in enumerate(zip(coffee,price))}
print(a)








