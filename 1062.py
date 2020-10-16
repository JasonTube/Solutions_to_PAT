def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def simplify(a,b):
    # simplify a/b
    common_factor = gcd(a,b)
    a = a // common_factor
    b = b // common_factor
    return a,b

if __name__ == '__main__':
    num1,num2,factor = input().split(" ")
    a,b = [int(tmp) for tmp in num1.split("/")]
    c,d = [int(tmp) for tmp in num2.split("/")]
    factor = int(factor)
    
    # simplify a/b and c/d
    a,b = simplify(a,b)
    c,d = simplify(c,d)
    
    # in case that a/b > c/d
    if a/b > c/d:
        tmp1,tmp2 = a,b
        a,b = c,d
        c,d = tmp1,tmp2
    
    min_num = (a*factor)//b
    max_num = (c*factor)//d
    
    result = []
    if gcd(min_num,factor) == 1 and min_num/factor > a/b:
        result.append(str(min_num) + '/' + str(factor))
    for i in range(min_num+1,max_num):
        if gcd(i,factor) == 1:
            result.append(str(i) + '/' + str(factor))
    if gcd(max_num,factor) == 1 and (max_num)/factor < c/d:
        result.append(str(max_num) + '/' + str(factor))
    
    print(" ".join(str(tmp) for tmp in result))
