# Script: merge_intervals.py
"""
Question: Merge Intervals
Given an array of intervals where `intervals[i] = [start_i, end_i]`, 
merge all overlapping intervals and return an array of 
the non-overlapping intervals that cover all the intervals in the input.
Example:
    Input: intervals = [[1,3], [2,6], [8,10], [15,18]]
    Output: [[1,6], [8,10], [15,18]]
"""

def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort the intervals by their starting point.
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        # If the current interval overlaps with the last merged interval, merge them.
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # Otherwise, add the current interval as is.
            merged.append(current)
    
    return merged

if __name__ == "__main__":
    intervals = [[1,3], [2,6], [8,10], [15,18]]
    merged = merge_intervals(intervals)
    print("Merged intervals:", merged)
