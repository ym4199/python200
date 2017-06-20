# f = lambda x: x * x
# args = [1, 2, 3, 4, 5]
#
# ret = map(f, args)
# print(list(ret))


# map 은 f 함수를 받아 args 를 이용 하여 반복수행한다.
# 반환되는 값은 map 객체로 리턴되고 list 를 이용하여 list 객체로 변환할 수 있다.



ff = lambda x,y : x*x+y
x=[1,2,3,4,5]
y=[10,9,8,7,6]

ret1 = map(ff,x,y)
print(list(ret1))