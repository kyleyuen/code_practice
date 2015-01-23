# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
    	# 1. no merge happens
    	n = len(intervals)
        if newInterval.end < intervals[0].start:
        	intervals.insert(0, newInterval)
        for i in range(1, n):
        	if (intervals[i-1].end<newInterval.start) and (newInterval.end<intervals[i].start):
        		intervals.insert(i, newInterval)
        		break
        if newInterval.start > intervals[n-1].end:
        	intervals.insert(n, newInterval)
        return intervals

        # 2. need to merge intervals
        merge_left, merge_right = False, False
		for i in reversed(range(n)):
			if intervals[i].start <= newInterval.start:
				left = i
				if intervals[i].end >= newInterval.start:
					merge_left = True
				break
		for i in range(left, n):
			if intervals[i].end >= newInterval.end:
				right = i
				if intervals[i].
				break
		