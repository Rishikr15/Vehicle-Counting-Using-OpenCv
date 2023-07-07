def even_odd(num):
    if num%2==0:
         return "the number {0} is even".format(num)
    else:
         return "the number {0} is odd".format(num)

even_odd(2)
l1=[1,2,3,4,5,6,7,8,9,10]
map(even_odd,l1)

list(map(even_odd,l1))

def addition(a,b):
    d=a+b
    return d
print("Enter the first value..")

a=int(input())

print("Enter the second value..")
b=int(input())
print("Enter the additon of a[0] and b[1] is d{2}").__format__(addition)










