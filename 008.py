class Solution(object):
    def myAtoi(self,str):
        """

        :type str: str
        :rtype: int
        """

        result = 0
        sign   = 1
        str    = str.strip()
        if len(str) == 0:
            return 0
        start  = 0
        end    = len(str)
        if str[0] == '+':
            sign  = 1
            start = 1
        if str[0] == '-':
            sign  = -1
            start = 1
        for i in range(start,end):
            value = str[i]
            if value.isdigit():
                result = result *10 +int(value)
            else:
                break
        result = result * sign
        if result >2147483647:
            result = 2147483647
        elif result <-2147483648:
            result = -2147483648
        return result


