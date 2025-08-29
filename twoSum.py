#给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。
#你可以按任意顺序返回答案。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        t=nums.copy()
        t.sort()
        left=0
        right=len(nums)-1
        while left<right:
            ans=t[left]+t[right]
            if ans==target:
                break
            if ans<target:
                left+=1
            else:
                right-=1
        p=nums.index(t[left])
        nums.pop(p)
        k=nums.index(t[right])
        if k>=p:
            k+=1
        return [p,k]
    