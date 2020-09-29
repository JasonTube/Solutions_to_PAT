def pat(string):
    string = list(string)
    p_index = -1
    t_index = -1
    
    for index,value in enumerate(string):
        if value == 'P' and p_index == -1:
            p_index = index
            continue
        elif value == 'T' and t_index == -1:
            t_index = index
            continue
        elif value == 'A':
            continue
        else:
            return "NO"

    a = p_index
    b = t_index - p_index - 1
    c = len(string) - t_index -1

    if b == 1:
        return "YES"
    elif b == 0:
        return "NO"
    elif c == a*b:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        string = input()
        print(pat(string))
