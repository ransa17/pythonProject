def findpair(nums,target):
    nums.sort()
    (low,high)=(0,len(nums)-1)
    while low<high:
        if nums[low]+nums[high]== target:
            print("pair found",(nums[low],nums[high]))
        if nums[low]+nums[high]<target:
            low=low+1
        else:
            high = high-1
    print("pair not found")
nums = [5,2,9,3,8,7,1,6,5,4,]
target= 10
findpair(nums,target)