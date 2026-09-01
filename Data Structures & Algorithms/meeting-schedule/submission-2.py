"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        # if next start time < prev end time >> conflict
        prev_end = 0

        for i in intervals:
            # start time = i[0], end time = i[1]
            #update the end time if it's bigger/equal than the prev_end
            if i.start >= prev_end:
                prev_end = i.end
            else:
                return False
        return True