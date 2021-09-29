class Solution:
    #1.去除多余空格
    def trim_spaces(self,s):
        n = len(s)
        left = 0 
        right = n-1 
        while(left<n-1 and s[left]==' '):
            left = left + 1
        while(right>left and s[right]== ' '): 
            right = right - 1
        tmp=[]
        while left<=right:                                    #去除单词中间多余的空格
            if s[left]!=' ':
                tmp.append(s[left])
            elif tmp[-1]!=' ':                                #当前位置是空格，但是相邻的上一个位置不是空格，则该空格是合理的
                tmp.append(s[left])
            left+=1
        return tmp
#2.翻转字符数组
    def reverse_string(self,nums,left,right):
        while(left<right):
            nums[left],nums[right] = nums[right],nums[left]
            left +=1
            right -=1
#3.翻转每个单词
    def reverse_each_word(self, nums):
        start=0
        end=0
        n=len(nums)
        while start<n:
            while end<n and nums[end]!=' ':
                end+=1
            self.reverse_string(nums,start,end-1)
            start=end+1
            end+=1
        return None
    def reverseWords(self, s):
        """
        给你一个字符串 s ，逐个翻转字符串中的所有 单词 。
        单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
        请你返回一个翻转 s 中单词顺序并用单个空格相连的字符串。
        说明：
        输入字符串 s 可以在前面、后面或者单词间包含多余的空格。
        翻转后单词间应当仅用一个空格分隔。
        翻转后的字符串中不应包含额外的空格。
        """
        # s = s.split()
        # s.reverse()
        # st = ""
        # for i in s:
        #     st +=i
        #     st +=" "
        # return st[:-1]
#4.翻转字符串里的单词
        l = self.trim_spaces(s)                     #输出：['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e'
        self.reverse_string( l,  0, len(l) - 1)   #输出：['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']
        self.reverse_each_word(l)               #输出：['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
        return ''.join(l)                                 #输出：blue is sky the




if __name__ ==  "__main__":
    a = Solution()
    s = "the sky is blue"
    print(a.reverseWords(s))