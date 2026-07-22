# sum of numbers from a to b

class Solution:
    def parameter_sum(self,a,b,sum):
        if a>b:
            print(sum)
            return 
        self.parameter_sum(a+1,b,sum+a)

    def non_parameter_sum(self,a,b) -> int:
        if a>b:
            return 0
        return a + self.non_parameter_sum(a+1,b)

    def non_parameter_fact(self,num):
        if num==0:
            return 1
        return num*self.non_parameter_fact(num-1)

    def reverse_array(self,i,arr):
        if i>=len(arr)//2:
            return arr
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]
        return self.reverse_array(i+1,arr)

    def pallindrome(self,mystr,i,n) ->bool:
        if i>=n:
            return True
        return mystr[i]==mystr[n] and self.pallindrome(mystr,i+1,n-1)

    def fibo(self,k):   # assuming 1 indexed    
        if k==1:
            return 0
        if k==2:
            return 1
        return self.fibo(k-2)+self.fibo(k-1)


obj = Solution()
# obj.parameter_sum(2,9,0)
# print(obj.non_parameter_sum(2,9))
# print(obj.non_parameter_fact(6))
# print(obj.reverse_array(0,[2,9,0,1,4,6]))
# print(obj.pallindrome("annaddanna",0,9))
print(obj.fibo(7))
