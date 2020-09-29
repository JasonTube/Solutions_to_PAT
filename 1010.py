if __name__ == "__main__":
    func = [int(tmp) for tmp in input().split()]
    dfunc = []
    k = len(func) // 2
    for i in range(k):
        tmp = func[2*i]*func[2*i+1]
        if tmp != 0:
            dfunc.extend([tmp, func[2*i+1]-1])
    if len(dfunc) == 0:
        dfunc.extend([0,0])
        
    print(" ".join(str(tmp) for tmp in dfunc))
