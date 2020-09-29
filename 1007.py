import math
def isPrime(num):
    #判断num是不是质数
    if num==1:
        return False
    elif num==2:
        return True
    else:
        for i in range(2,int(math.sqrt(num))+1,2):
            if num % i == 0:
                return False;
        return True

if __name__=='__main__':
    n = int(input())
    flags = [False]*2 + [True]*(n-1)
    result = 0
    
    prime_old = 2
    for i in range(1,n+1,2):
        if not flags[i]:
            continue
        elif isPrime(i):
            for j in range(2*i,n+1,i):
                flags[j] = False
            if i-prime_old == 2:
                result += 1
            prime_old = i
    print(result) 
