class Solution:
    def merge(self, intervals):
        '''
        以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
        输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
        输出：[[1,6],[8,10],[15,18]]
        解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

        '''
        if (len(intervals)==0): return intervals
        result = []
        intervals.sort(key = lambda x: x[0])
        result.append(intervals[0])
        for i in range(1,len(intervals)):
            last = result[-1]
            if(last[1] >= intervals[i][0]):
                result[-1] = [last[0],max(last[1],intervals[i][1])]
            else:
                result.append(intervals[i])
        return result

if __name__ ==  "__main__":
    s = Solution()
    intervals = [[1,4],[0,4]]
    print(s.merge(intervals))
