class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, x, n, d):
        resultOfPower = self.powerCalc(x,n)
        return resultOfPower % d
    
    def powerCalc(self,x,y):
        if(y == 0): 
            return 1
        temp = self.powerCalc(x, int(y / 2))  
      
        if (y % 2 == 0): 
            return temp * temp 
        else: 
            if(y > 0): 
                return x * temp * temp 
            else: 
                return (temp * temp) / x  
        
result = Solution()
print(result.pow(-33,33,-22))