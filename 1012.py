if __name__ == "__main__":
    nums = [int(tmp) for tmp in input().split(" ")]
    A = [0] * 5 # A[0:4]: A1~A5
    flags = [False] * 5
    
    count = 0 #
    sgn = 1 # A2
    for i in range(1,nums[0]+1):
        tmp = nums[i] % 5
        if tmp == 0:
            if nums[i] % 2 == 0:
                A[0] += nums[i]
                flags[0] = True
        elif tmp == 1:
            A[1] += (nums[i] * sgn)
            sgn *= -1
            flags[1] = True
        elif tmp == 2:
            A[2] += 1
            flags[2] = True
        elif tmp == 3:
            A[3] += nums[i]
            count += 1
            flags[3] = True
        else:
            if nums[i] > A[4]:
                A[4] = nums[i]
            flags[4] = True
    if count > 0:
        A[3] = round(A[3]/count, 1)
        
    A = [tmp if flag else 'N' for tmp,flag in zip(A,flags)]
    print(" ".join(str(tmp) for tmp in A))
