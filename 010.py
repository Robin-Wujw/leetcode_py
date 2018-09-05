class Solution():
	def isMatch(self,s,p):
		"""
		:type s: str
		:type p: str
		:rtype:  bool
		"""
		x = len(s) + 1
		y = len(p) + 1
		if y == 1:
			return x ==1
		matrix = [[False] * x for i in range(y)]
		matrix[0][0] = True
		for i in range(y-1):
			if p[i] == "*":
				matrix[i+1][0] = matrix[i-1][0]
		for i in range(1,y):
			for j in range(1,x):
				if p[i-1] == ".":
					matrix[i][j] = matrix[i-1][j-1]
				elif p[i-1] =="*":
					if p[i-2] != s[j-1] and p[i-2] !=".":
						matrix[i][j] = matrix[i-2][j]
					else:
						matrix[i][j] = matrix[i-2][j] or matrix[i-1][j]or matrix[i][j-1]
				else:
					matrix[i][j] = matrix[i-1][j-1] and p[i-1]==s[j-1]
		return matrix[-1][-1]