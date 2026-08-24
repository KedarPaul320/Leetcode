class Solution:
    def merge(self,nums,left,mid,right):
        a = []
        b = []

        for i in range(left,mid+1):
            a.append(nums[i])
        for i in range(mid+1,right+1):
            b.append(nums[i])

        i,j,k = 0 , 0, left
        while k<=right :
            if j == len(b):
                nums[k] = a[i]
                i+=1
                k+=1
            elif i == len(a):
                nums[k] = b[j]
                j+=1
                k+=1
            elif a[i]<b[j]:
                nums[k] = a[i]
                i+=1
                k+=1
            else :
                nums[k] = b[j]
                j+=1
                k+=1

    def mergesort(self,nums,left,right):
        if left >= right :
            return 
        
        mid = (left + right)//2
        
        self.mergesort(nums,left,mid)
        self.mergesort(nums,mid+1,right)

        self.merge(nums,left,mid,right)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums,0,len(nums)-1)
        return nums