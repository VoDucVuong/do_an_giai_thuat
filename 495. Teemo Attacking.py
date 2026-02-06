class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries:
            return 0
        n = len(timeSeries)
        total_duration = 0
        for i in range(n - 1):
            start_time = timeSeries[i]
            next_time = timeSeries[i+1]
            distance = next_time - start_time
            duration_of_effect = min(duration, distance)
            total_duration += duration_of_effect
        total_duration += duration
        return total_duration