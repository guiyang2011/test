# https://leetcode.com/problems/string-to-integer-atoi/#/description
# '123' to 123
class Solution:
    def Atoi(self, inStr):
        result = 0
        for i in list(inStr):
            result = result*10 + (ord(i) -ord('0')) # chr(int)
        return result

def main():
    solution = Solution()
    result = solution.Atoi("123")
    print(result)

if __name__ == "__main__":
    main()
