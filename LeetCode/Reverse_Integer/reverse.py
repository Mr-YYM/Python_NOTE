class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        old=0
        result = []
        fu = False
        if x<0:
            fu = True
            x=-x
        for i in range(1, 7):
            r = x%10**i
            if old == r and i!=1:
                break
            f = (r-old)/10**(i-1)
            result.append(int(f))
            old = r
        
        try:
            if result[0] == 0:
                result = result[1:]
        except:
                return 0
        str_int = ''.join(map(str, result))

        try:
            xxxx = int(str_int)
        except:
            return 0
        
        if fu:
            return -xxxx
        return xxxx

s = Solution()
print(s.reverse(120))
