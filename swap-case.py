def swap_case(s):
    ss = []
    for element in s:
        if element.isupper():
            ss.append(element.lower())
        elif element.islower():
            ss.append(element.upper())
        else:
            ss.append(element)
    s = "".join(ss)
    return ss,s
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
