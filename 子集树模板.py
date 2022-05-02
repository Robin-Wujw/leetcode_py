'''求集合{1, 2, 3, 4}的所有子集'''
class SubSetTree:
    def __init__(self, a):
        self.a = a      # 数据列表
        self.n = len(a) # 数据长度
        self.x = []     # 一个解
        self.X = []     # 一组解


    def conflict(self, k):    # 冲突检测：无
        return False
    # 子集树递归模板
    def backtrack(self, k): # 到达第k个元素
        if k >= self.n:  # 超出最尾的元素
            self.X.append(self.x[:]) # 保存（一个解）
        else:
            for i in [1, 0]: # 遍历元素 a[k] 的两种选择状态:1-选择，0-不选
                if i==1:
                    self.x.append(self.a[k])
                if not self.conflict(k): # 剪枝
                    self.backtrack(k+1)
                if i==1:
                    self.x.pop()              # 回溯
    def SovleSubSet(self):
        self.backtrack(0)
        return self.X



if __name__ == '__main__':
    test = SubSetTree([1, 2, 3, 4])

    res = test.SovleSubSet()

    print(res)   # [[1, 2, 3, 4], [1, 2, 3], [1, 2, 4], [1, 2], [1, 3, 4], [1, 3], [1, 4], [1], [2, 3, 4], [2, 3], [2, 4], [2], [3, 4], [3], [4], []]
