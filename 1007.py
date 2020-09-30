import math
def isPrime(num,prime_list):
    #判断num是不是质数
    if num <= 3:
        prime_list.append(num)
        return True
    if num % 6 != 1 and num % 6 != 5:
        return False
    tmp = int(math.sqrt(num))
    for i in prime_list:
        if i > tmp:
            break
        elif num % i == 0:
            return False
    prime_list.append(num)
    return True

if __name__=='__main__':
    prime_list = []
    n = int(input())
    flags = [False]*2 + [True]*(n-1)
    result = 0
    
    prime_old = 2
    for i in range(1,n+1,2):
        if not flags[i]:
            continue
        elif isPrime(i,prime_list):
            for j in range(2*i,n+1,i):
                flags[j] = False
            if i-prime_old == 2:
                result += 1
            prime_old = i
    print(result) 
