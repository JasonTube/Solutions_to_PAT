if __name__ == "__main__":
    num = int(input())
    result = []
    result.extend(["B"]*(num//100))
    result.extend(["S"]*(num//10 %10))
    result.extend(list(range(1,num % 10 + 1)))
    print("".join(str(tmp) for tmp in result))
