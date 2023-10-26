# Talent-Teams
# HackerRank Solution
talentsCount = 3
talent = [1, 2, 3, 2, 1]

There is no way fewer than 3 students can have at least 3 talents. The following subarrays of length 3 or more are possible:

Starting at position 1: [1, 2, 3], [1, 2, 3, 2], [1, 2, 3, 2, 1] 
Starting at position 2: [2, 3, 2], [2, 3, 2, 1]
Starting at position 3: [3, 2, 1] 
No further subarrays of length 3 or more exist.

Starting at the first position, e shortest subarray with one of each talent value has length 3.

Starting at element 2, the shortest has length 4. At position 3, the shortest and only possible subarray has length 3.

It is not possible to form a team with fewer than 3 members, so the subarrays starting at the last two positions will fail.

The highlighted subarrays are selected. The return array is

[3, 4, 3,-1,-1)

## Example 2
There have to be at least 3 elements in any subarray to represent each talent. The following subarrays are possible:

Beginning at the first position: [1, 1, 2], [1, 1, 2, 2], [1, 1, 2, 2, 3], [1, 1, 2, 2, 3, 1], [1, 1, 2, 2, 3, 1, 3], [1, 1,

2, 2, 3, 1, 3, 2]

Second position: [1, 2, 2], [1, 2, 2, 3], [1, 2, 2, 3, 1], [1, 2, 2, 3, 1, 3], [1, 2, 2, 3, 1, 3, 2]

Third position: [2, 2, 3], [2, 2, 3, 11, [2, 2, 3, 1, 3], [2, 2, 3, 1, 3, 2]

Fourth position: [2, 3, 1], [2, 3, 1, 3], [2, 3, 1, 3, 2]

Fifth position: [3, 1, 3], [3, 1, 3, 2]

Sixth position: [1, 3, 2]

No further subarrays will have 3 elements.

The highlighted subarrays are the shytest for each starting position. The return array of subarray lengths is [5, 4, 4, 3, 4, 3, -1, -1]
