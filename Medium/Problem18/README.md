# Count 3D Array Element (Medium)

This problem requires you to count the number of elements equal to a given integer `p` in a 3D array of 32-bit integers, **without using any external libraries**.

## Problem Statement

Given:

- An input 3D array `input` of size `N × M × K` containing 32-bit integers
- An integer `p`

Count how many times the value `p` appears in the 3D array. The result must be stored in the variable `output`.

---

## Example

**Example 1:**

- Input:

  ```
  input = [
    [[1, 2, 3],
     [4, 5, 1]],
    [[1, 1, 1],
     [2, 2, 2]]
  ]
  N = 2, M = 2, K = 3
  p = 1
  ```

- Output:
  `output = 5`

**Example 2:**

- Input:

  ```
  input = [
    [[5, 10],
     [5, 2],
     [2, 2]]
  ]
  N = 1, M = 3, K = 2
  p = 1
  ```

- Output:
  `output = 0`

## Constraints

- 1 ≤ N, M, K ≤ 1,000
- 1 ≤ input[i], p ≤ 100
- No external libraries are allowed.
- The final result must be stored in the variable `output`.

## Solution

See [count3d.py](./count3d.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Count 3D Array Element](https://leetgpu.com/challenges/count-3d-array-element)
