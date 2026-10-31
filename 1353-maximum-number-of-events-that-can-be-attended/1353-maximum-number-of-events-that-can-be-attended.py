import heapq

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()                 # by start day
        heap = []                     # end days of talks open right now
        i = 0                         # next talk not yet added
        day = 0
        count = 0

        while heap or i < len(events):
            if not heap:              # nothing open: jump to the next start
                day = events[i][0]

            # 1. open every talk that starts today
            while i < len(events) and events[i][0] == day:
                heapq.heappush(heap, events[i][1])
                i += 1

            # 2. drop talks that have already ended
            while heap and heap[0] < day:
                heapq.heappop(heap)

            # 3. attend the one ending soonest
            if heap:
                heapq.heappop(heap)
                count += 1

            day += 1

        return count