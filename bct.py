# # print("Hello students")
# # s='PYTHON'
# # print(s[0:4])
# # print(s[-1:-4]) #empty string
# # print(s[::-1]) #reverse string
# # print(s[0:6:2]) #alternate characters
# # x =s[-3:-1]
# # y=x[::-1]
# # print(y)
# # # s[3]='z' #string is immutable
# # #how to do concatanation
# # s1='hello'
# # s2='world'
# # s3=s1+s2
# # print(s3)
# # s4=s1*3
# # print(s4)
# #x=s[0:6] + 'Z' + s[5:]
# #print(x)
# #list of n python
# # list 
# #x=[6,1,23,45,67,90,12]
# # is ls similar to array?
# # ls is mutable
# # ls is heteregenous
# # ls is dynamic and ordered
# # where as array in python is
# # array is homogenous
# # array has fixes size
# # array is static and ordered
# # print(x) 
# # type (x)
# # print(x[2:5])
# # x[3]
# # print(x)
# # x[3]=200
# # print(x)
# # x.append(500) #add element at the end
# # print(x) 
# # x.insert(2,90) #insert element at the given index
# # print(x)
# # x.pop()
# # 500
# # print(x)
# # x.pop(2)
# # print(x)
# # del(x)
# # print(x) 
# # tuple
# # what is tuple?
# # tuple is unmutable
# #tuple is ordered
# #tuple is heterogenous
# #tuple is static
# #tuple is faster than list
# #we can do only splicing and indexing in tuple
# #we can not do any operation in tuple
# #we can not add or delete or update in tuple
# #we can not sort or reverse in tuple
# #s = (4,4,4,2,7,9,9,9,0,1)
# #example to implement set in python?
# # dict ={'name':'rishi','age':21,'city':'kolkata','college':'bct'}
# # print(dict['name'])
# # print(dict['age'])
# # print(dict['city'])
# # print(dict['college'])
# # print(dict)
# # type(dict)
# # a = ('Amit','Rishi','Rahul')
# # b = ('name1','name2','name3')
# # res = {}
# # for k in a:
# #     for v in b:
# #         res[k] = v
# #         b.remove(v)
# #         break
# #print(res)    
# a = ('Amit','Rishi','Rahul')
# b = ('name1','name2','name3')
# d= {k:v for k,v in zip(a,b)}
# # print(d)  
# # type(d)    
# # d = dict(zip(b,a))
# # print(d)
# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")
# a = 20
# b = 20
# if b > a:   
#     print("b is greater than a")    
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")
# a= int(input("enter the value of a"))
# print(a)
# for i in range(10):
# #     print(i);
# for i in range(2,10):
#     print(i);
# d.values()
# number = 9
# s = eval('number*number')
# print(s)
number_list = [1,2,3,4,5,6,7,8,9,10]
str_list=['one','two','three','four','five','six','seven','eight','nine','ten']
result=zip()
result_list=list(result)
print(result_list)
result=zip(number_list,str_list)
result_set = set(result)
print(result_set)
#unzippin
c=['z','y','x']
v=[3,4,5]
result = zip(c,v)
x=list(result)
print(x)
c,v=zip(*x)
print(c)
print(v)
for( )

