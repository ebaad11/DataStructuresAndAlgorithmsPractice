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
    @return: the minimum number of conference rooms required
    """
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end =  sorted([i.end for i in intervals])
      
        s,e = 0,0
        rooms = 0
        maxRooms = float("-inf")
        while s < len(intervals):
            
            
            aMeetingIsStartingBeforeTheFirstOneEnded = start[s] < end[e]

            if aMeetingIsStartingBeforeTheFirstOneEnded:
                rooms+=1
                s+=1
            else:
                rooms-=1
                e+=1

            maxRooms =max(maxRooms,rooms)

        return maxRooms
