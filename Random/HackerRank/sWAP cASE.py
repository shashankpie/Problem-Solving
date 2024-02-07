def swap_case(s):
    ans = ''
    for ele in s:
        if ele.islower():
            ans += ele.upper()
        elif ele.isupper():
            ans += ele.lower()
        else:
            ans += ele
    return ans

if __name__ == '__main__':
