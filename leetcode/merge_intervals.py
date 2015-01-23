# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, cmp=self.compare)
        last = 1
        for i in range(1, len(intervals)):
            if intervals[i].start != intervals[i-1].start:
                intervals[last] = intervals[i]
                last += 1

        result = []
        start, end = intervals[0].start, intervals[0].end
        for i in range(1, last):
            if end < intervals[i].start:
                result.append(Interval(start, end))
                start, end = intervals[i].start, intervals[i].end
            elif end < intervals[i].end:
                end = intervals[i].end
        
        result.append(Interval(start, end))
        return result


    def compare(self, left, right):
        if left.start < right.start:
            return -1
        elif left.start > right.start:
            return 1
        else:
            return right.end - left.end


intervals = []
intervals.append(Interval(1, 3))
intervals.append(Interval(2, 6))
intervals.append(Interval(8, 10))
intervals.append(Interval(15, 18))
s = Solution()
result = s.merge(intervals)
for i in result:
    print i.start, i.end