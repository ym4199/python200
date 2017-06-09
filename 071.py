# def getPrime(x):
#     for i in range(2,x-1):
#         if x % i ==0:
#             break
#
#     else:
#         return x
#
# listdata = [117,119,1113,11113,11119]
# ret = filter(getPrime,listdata)
# print(list(ret))


# 소수만 걸러내는 필터

def getPrime(n):
    ret = [2,3]
    if n <= 3:
        return ret

    for i in range(4,n+1):
        for k in range(2,i-1):
            a = i%k
            if a == 0:
                isPrime = False
                break

    else:
        ret.append(i)
    return ret

print(getPrime(15))