class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        lookup = {} # Key:Value::Value_in_list:index
        for i in range(len(nums)):
            cur = nums[i]
            need = target - cur
            if need in lookup.keys():
                break
            else:
                lookup.update({nums[i]:i})
                i+=1
        return i, lookup.get(need)
