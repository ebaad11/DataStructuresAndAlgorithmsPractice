from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        if len(intervals) == 0:
            return True

        intervals.sort(key=lambda val :val.start)

        prevStart,prevEnd = intervals[0].start, intervals[0].end

        for i in range(1,len(intervals)):
            start = intervals[i].start
            end = intervals[i].end

            if prevEnd > start:
                return False
            prevStart,prevEnd = intervals[i].start, intervals[i].end

        return True 

