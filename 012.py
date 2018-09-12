class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        tens = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        hundreds=['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        thousands=['','M','MM','MMM']
        return thousands[num//1000%10] +hundreds[num//100%10]+tens[nums//10%10]+ones[num%10]