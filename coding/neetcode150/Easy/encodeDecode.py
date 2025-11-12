
# My Implementation
def encode(decoded_str_arr : list[str]) -> str:
    result = ""

    if not decoded_str_arr:
        return ""
    for word in decoded_str_arr:
        result += str(word + "#")
    return result

def decode(encoded_str : str) -> list[str]:
    combination  = encoded_str.split("#")
    combination.pop()

    return combination

#Optimal Implementation
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res

# x = encode(["hello", "How", "Are", "You"])

# print(x)

# print(decode(x))

