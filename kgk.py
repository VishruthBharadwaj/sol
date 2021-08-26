class Solution(object):
    def findMissingRanges(self, nums, lower, upper):

        def getRange(lower, upper):
            if lower == upper:
                #print(lower)
                return "{}".format(lower)
            else:
                #print(lower,upper)
                return "{}->{}".format(lower, upper)
        ranges = []
        pre = lower - 1
        
        for i in range(len(nums) + 1):
            # print(i)
            if i == len(nums):
                cur = upper + 1
                # print(cur)
            else:
                cur = nums[i]
                # print(cur)
            if cur - pre >= 2:
                ranges.append(getRange(pre + 1, cur - 1))
                
            pre = cur
            
        return ranges


if __name__ == "__main__":
    print (Solution().findMissingRanges([0, 1, 3, 50, 75], 0, 99))