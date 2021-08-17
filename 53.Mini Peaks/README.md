Write a function that returns all the elements in an array that are strictly greater than their adjacent left and right neighbors.

Example 1:

    Input: nums = [4, 5, 2, 1, 4, 9, 7, 2]

    Output: [5, 9]

    Output:  Because nums[1] > nums[0] && nums[1] > nums[2] ,  nums[5] > nums[4] && nums[5] > nums[6]

    so, return [num[1], num[5]] => [5, 9]

Example 2:

    Input:  [1, 2, 1, 1, 3, 2, 5, 4, 4]

    Output:  [2, 3, 5]

Example 3:

    Input:  [1, 2, 3, 4, 5, 6]

    Output:  []
