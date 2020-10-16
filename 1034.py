def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def simplify(num_str):
    # simplify a/b, b != 0
    a,b = [int(tmp) for tmp in num_str.split("/")]
    if a == 0:
        return str(a)

    sign = a // abs(a)      # 存符号
    a = abs(a)              # a的绝对值
    c = 0                   # 存整数部分
    # 取整数部分
    if abs(a) > b:
        c = a // b
        a = a - c*b
    # 化简真分数部分
    if a != 0:
        common_factor = gcd(a,b)
        a = a // common_factor
        b = b // common_factor
                    
    result = ""
    if a != 0:
        result = result + str(a)
        if b != 1:
            result = result + "/" + str(b)
    if c != 0 and a != 0:
        result = str(c) + " " + result
    elif c != 0 and a == 0:
        result = str(c) + result
    if sign == -1:
        result = "(-" + result + ")"
    return result

def analysis(num1,num2):
    a,b = [int(tmp) for tmp in num1.split("/")]
    c,d = [int(tmp) for tmp in num2.split("/")]
    return a,b,c,d

def plus(num1,num2):
    a,b,c,d = analysis(num1,num2)
    e = a*d + b*c
    f = b*d
    num3 = str(e) + "/" + str(f)
    return simplify(num3)

def minus(num1,num2):
    a,b,c,d = analysis(num1,num2)
    e = a*d - b*c
    f = b*d
    num3 = str(e) + "/" + str(f)
    return simplify(num3)

def multiply(num1,num2):
    a,b,c,d = analysis(num1,num2)
    e = a*c
    f = b*d
    num3 = str(e) + "/" + str(f)
    return simplify(num3)

def divide(num1,num2):
    a,b,c,d = analysis(num1,num2)
    e = a*d
    f = b*c
    if f != 0:
        if f < 0:
            e = -e
            f = -f
        num3 = str(e) + "/" + str(f)
        return simplify(num3)
    else:
        return "Inf"

if __name__ == '__main__':
    num1,num2 = input().split(" ")
    simplified_num1 = simplify(num1)
    simplified_num2 = simplify(num2)
    print(simplified_num1 + " + " + simplified_num2 + " = " + plus(num1,num2))
    print(simplified_num1 + " - " + simplified_num2 + " = " + minus(num1,num2))
    print(simplified_num1 + " * " + simplified_num2 + " = " + multiply(num1,num2))
    print(simplified_num1 + " / " + simplified_num2 + " = " + divide(num1,num2))
