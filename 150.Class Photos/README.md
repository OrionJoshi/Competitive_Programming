### Class Photos

Understanding the problem

I am given two non-empty arrays of positive integers. The first array is going to represent the heights of students wearing red shirts and the second array is going to represent the heights of students wearing blue shirts. The two arrays will always have the same length. I am asked to write a function that is going to find out if we can take a photo of these students that adheres to the following constraints:

    All the students that are wearing red shirts must be in the same row;
    All of the students that are wearing blue shirts must be in the same row;
    The photo must have exactly two rows and the two rows must have the same number of students in them.
    Every student in the front row must be shorter than the student directly behind them in the back row.

The function is going to arrange the students and return true if we can take a photo that follows these constraints; otherwise return false.

Example-1

    redShirtHeights = [4, 6, 2, 7]
    blueShirtHeights = [3, 5, 8, 9]
    Output = True
