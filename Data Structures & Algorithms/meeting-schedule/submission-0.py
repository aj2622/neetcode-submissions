"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x : [x.start, x.end])
        end = 0
        for interval in intervals:
            i, j = interval.start, interval.end
            if end > i:
                return False
            end = j
        return True