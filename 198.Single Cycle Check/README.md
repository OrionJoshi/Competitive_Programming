You’re given an array of integers where each integer represents a jump of its value in an array.
For instance, the integer 2 represents a jump of two indices forward in the array; the integer -3
represents a jump of three indices backward in the array.

If a jump spills past the array’s bounds, it wraps over to the other side.
For instance, a jump of -1 at index 0 brings us to the last index in the array.
Similarly, a jump of 1 at the past index in the array brings us to index 0.

Write a function that returns a boolean representing whether the jumps in the array form a single cycle.
A single cycle occurs if, starting at any index in the array and following the jumps,
every element is visited exactly once before landing back on the starting index
