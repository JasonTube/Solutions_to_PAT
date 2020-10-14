if __name__ == '__main__':
    keys = set(input())
    input_string = list(input())

    output_string = [tmp for tmp in input_string if not tmp.upper() in keys]
    if '+' in keys:
        output_string = [tmp for tmp in output_string if ord(tmp)<65 or ord(tmp)>90]

    print("".join(str(tmp) for tmp in output_string))
