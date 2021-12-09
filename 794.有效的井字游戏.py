#
# @lc app=leetcode.cn id=794 lang=python3
#
# [794] 有效的井字游戏
#

# @lc code=start
class Solution(object):
    def validTicTacToe(self, board):
        # 暴力模拟
        # 有效游戏的条件：
        # （1）X的数量只能和O一样，或者比O多一个
        # （2）如果X的数量比O多一个，则O不可能获胜（因为X先攻多走一步）
        # （3）如果X的数量和O相同，则X不可能获胜

        # 计算XO数量
        countx, counto = 0, 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    countx += 1
                elif board[i][j] == "O":
                    counto += 1
        if countx > counto+1: return False
        if countx < counto: return False

        # 判断胜方
        def isWin(winType):
            # 横线获胜
            for i in range(3):
                if board[i] == winType:
                    return True
            # 竖线获胜
            for j in range(3):
                if board[0][j]+board[1][j]+board[2][j] == winType:
                    return True
            # 左右斜线获胜
            if board[0][0]+board[1][1]+board[2][2] == winType: return True
            if board[0][2]+board[1][1]+board[2][0] == winType: return True
            return False
        
        winx, wino = isWin("XXX"), isWin("OOO")
        if countx > counto and wino: return False
        if countx == counto and winx: return False

        return True
# @lc code=end

