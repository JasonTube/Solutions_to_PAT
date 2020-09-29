if __name__ == "__main__":
    k = int(input())
    nums = [int(tmp) for tmp in input().split(" ")]
    flags = [1]*k
    
    for i in range(k):
        loop_flag = True
        num = nums[i]
        while num != 1 and loop_flag:
            if num % 2 == 0:
                num = num/2
            else:
                num = (3*num+1)/2
            for j in range(k):
                if nums[j] == num:
                    if flags[j] == 0:
                        loop_flag = False
                        break
                    else:
                        flags[j] = 0
                        break

    result = [num*flag for num,flag in zip(nums,flags)]
    result.sort(reverse = True)
    print(" ".join(str(tmp) for tmp in result if tmp != 0))
