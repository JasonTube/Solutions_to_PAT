if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        a,b,c = [int(tmp) for tmp in input().split(" ")]
        if a+b > c:
            print(f"Case #{i+1}: true")
        else:
            print(f"Case #{i+1}: false")
