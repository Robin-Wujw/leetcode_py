class Solution(object):
	def convert(self,s,numRows):
		"""
		:type s:str
		:type numRows:int
		:rtype: str
		"""

		result = ""
		length = len(s)
		n 	   = numRows
		cycle  = 2*n-2
		if   n == 1:
			return s
		i      = 0
		x      = 0
		while len(result) < length:
			if cycle * x + i > length - 1:
				i +=1
				x = 0
			zig = cycle * x + i
			zag = cycle * (x+1) -i
			if i == 0 or i == n-1:
				result += s[zig]
			else:
				if zag > length - 1:
					result +=s[zig]
				else:
					result +=s[zig] + s[zag]
			x +=1
		return result
def main():
    a = Solution
    b="PAYPALISHIRING"
    print(a.convert(a,b,3))
main()