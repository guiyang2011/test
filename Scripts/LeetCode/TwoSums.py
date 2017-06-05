class Solution(object):
    def two_sum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

def main():
    nums = (1,2,3,5,6)
    target = 4
    solution = Solution()
    result = solution.two_sum(nums, target)
    print(result)

if __name__ == "__main__":
    main()