class Solution:
    def specialArray(self, nums):
        range_number = (len(nums))
        for num in range(range_number):
            value = nums[num]
            new_list = []
            for i in range(range_number):
                if i == num:
                    continue
                if nums[i] >= value:
                    new_list.append(nums[i])
            if len(new_list) >= value:
                special = new_list
                return(special)
        return(-1)
c = Solution()
# nums = [3,5]
nums = [3,9,7,8,3,8,6,6]
out = c.specialArray(nums)
print(out)