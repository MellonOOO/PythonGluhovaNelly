 # 1
a = float(input())
b = float(input())
print(a + b)
print(a - b)
print(a/b)

# 2
age = int(input())
if age >= 18:
    print("Да")
else:
    print("Нет")

# 3
name = input("ИМЯ")
surname = input("ФАМИЛИЯ")
print("меня завут " + name + " " + surname)

#4
a = float(input())
b = float(input())
c = float(input())

D = b ** 2 - 4 * a * c
if D < 0 :
    print("корней нет")
elif D == 0 :
    print((-1 * b + D ** 0.5)/2/a)
else:
    print((-1 * b + D ** 0.5)/2/a)
    print((-1 * b - D ** 0.5)/2/a)



