if __name__ == "__main__":
    n = int(input())
    n_spell = {1:"yi",2:"er",3:"san",4:"si",5:"wu",6:"liu",7:"qi",8:"ba",9:"jiu",0:"ling"}
    sum_n = 0
    while n != 0:
        sum_n += n % 10
        n = n // 10
    sum_n_spell = []
    while sum_n != 0:
        sum_n_spell.insert(0, n_spell[sum_n % 10] + " ")
        sum_n = sum_n // 10
    result = "".join(sum_n_spell)
    result = result[:-1]
    print(result)
