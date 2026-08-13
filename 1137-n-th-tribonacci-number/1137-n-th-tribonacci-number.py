class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n==1 or n== 2:
            return 1
        arr = [0]*(n+1)
        arr[0],arr[1],arr[2]=0,1,1
        # print (arr)
        i = 0 
        while i <n-2 :
            arr[i+3] = arr[i]+arr[i+1]+arr[i+2]
            i+=1
        # print(arr)
        return arr[n]
