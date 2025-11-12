
def isPalindrome(s: str) -> bool:
    output = True

    left = 0
    right = len(s) - 1

    while left < right:

        print(f'{s[left]} {s[right]}')

        if s[left] != s[right]:
            output = False
            break

        left += 1
        right -= 1
        
    return output

print(isPalindrome("aba"))

        