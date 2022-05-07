#
# @lc app=leetcode.cn id=1700 lang=python3
#
# [1700] 无法吃午餐的学生数量
#

# @lc code=start
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        i = 0 
        while(True):
            if(len(students)== 0 and len(sandwiches)==0):
                return 0
            if(students[0]!=sandwiches[0]):
                temp = students.popleft()
                students.append(temp)
                print(students)
                i = i + 1 
                if(i == len(students)):
                    return i 
                    
            if(students[0]==sandwiches[0]):
                students.popleft()
                sandwiches.popleft()
                i = 0
# @lc code=end

