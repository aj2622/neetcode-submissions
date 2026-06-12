class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        i = 0
        while i < len(intervals):
            if not ans:
                ans.append(intervals[i])
            elif ans[-1][0] <= intervals[i][0] <= ans[-1][1] or ans[-1][0] <= intervals[i][1] <= ans[-1][1]:
                x,y = ans.pop()
                ans.append([min(x,intervals[i][0]), max(y,intervals[i][1])])
            else:
                ans.append(intervals[i])
            i += 1
        return ans