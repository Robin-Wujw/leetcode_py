#
# @lc app=leetcode.cn id=1185 lang=python3
#
# [1185] 一周中的第几天
#

# @lc code=start
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = 0
        months = [31,0,31,30,31,30,31,31,30,31,30,31]
        week = ['Friday','Saturday','Sunday', 'Monday','Tuesday','Wednesday','Thursday']
        for i in range(1971,year):
            if(self.isLeapYear(i)):
                days += 366
            else:
                days += 365
        for i in range(1,month):
            if(i==2):
                if(self.isLeapYear(year)):
                    days += 29
                else:
                    days += 28
                continue
            days += months[i-1]
        days += day - 1 
        days = days % 7
        return week[days]
    def isLeapYear(self,year):
        return (year % 100 !=0 and year % 4 == 0)  or (year %100 ==0 and year%400 ==0)
# @lc code=end

