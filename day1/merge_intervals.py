#ask the interviewer: given input is sorted or not if not mentioned

n = int(input())
intervals = [[int(input()) for _ in range(2)] for _ in range(n)]

#if not sorted => 
#brute force approach - nlogn + n2 time complexity
#first sort the array and iterate through the array to check



#Optimal Approach - Linear solution (O(n))
#space comeplexity will be O(n) at the worst case
n = len(intervals)
if n == 1:
    print(intervals)
# Sort the intervals based on start time.
intervals.sort(key=lambda x:x[0])
i = 1
while i < n:
    # if the start time of current interval is less that or equal to the end time of previous event then merge these two events.
    if intervals[i][0] <= intervals[i-1][1]:
        # Merge
        intervals[i-1] = [intervals[i-1][0], max(intervals[i][1], intervals[i-1][1])]
        intervals.pop(i)
        n -= 1
    else:
        i += 1
print(intervals)

