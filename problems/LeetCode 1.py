#naive solution
#time complexity - O(n^2)
def twoSum(nums, target):
    res = []
    
    l = len(nums)
    
    for i in range(0,l):
        for j in range(i+1, l):
            if nums[i] + nums[j] == target:
                res.append(i)
                res.append(j)
                return res


# faster solution
# timecomplexity ideally should be less than O(n)
def twoSumHash(nums, target):
    
    res = []
    hashMap = dict()
    l = len(nums)
    for i in range(0, l):
        diff = target - nums[i]
        if diff in hashMap:
            res.append(hashMap[diff])
            res.append(i)
            return res
        else:
            hashMap[nums[i]] = i 