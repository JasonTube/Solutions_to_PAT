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
    M,N = [int(tmp) for tmp in input().split()]
    count = 0
    num = 2
    prime_list = []
    while True:
        if isPrime(num,prime_list):
            count += 1
            if count >= M and count < N:
                if (count - M + 1) % 10 == 0:
                    print(num)
                else:
                    print(num,end = " ")
            elif count == N:
                print(num)
                break
        if num >= 3:
            num += 2
        else:
            num += 1

