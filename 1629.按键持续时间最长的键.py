#
# @lc app=leetcode.cn id=1629 lang=python3
#
# [1629] 按键持续时间最长的键
#

# @lc code=start
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        maxT = 0
        maxi = keysPressed[0]
        for i in range(len(releaseTimes)):
            if(i == 0):
                maxT = releaseTimes[i]
            else:
                print(releaseTimes[i],releaseTimes[i-1])
                if(releaseTimes[i]-releaseTimes[i-1] == maxT):
                    if(keysPressed[i]>maxi):
                        maxi = keysPressed[i]
                elif(releaseTimes[i]-releaseTimes[i-1] > maxT):
                    maxT = releaseTimes[i]-releaseTimes[i-1]
                    maxi =keysPressed[i]
        return maxi

# @lc code=end

