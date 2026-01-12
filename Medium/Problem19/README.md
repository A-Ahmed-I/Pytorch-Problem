# Subarray Sum (Medium)

This problem requires you to compute the sum of a subarray of 32-bit integers, **without using any external libraries**.

## Problem Statement

Given:

- `input`: An array of 32-bit integers of length `N`
- `S`: Start index (inclusive, 0-based)
- `E`: End index (inclusive, 0-based)

Compute the sum of the subarray `input[S..E]`. The result must be stored in the variable `output`.

## Example

**Example 1:**

- Input: `input = [1, 2, 1, 3, 4]`, `S = 1`, `E = 3`
- Output: `output = 6`

**Example 2:**

- Input: `input = [1, 2, 3, 4]`, `S = 0`, `E = 3`
- Output: `output = 10`

## Constraints

- 1 ≤ N ≤ 100,000,000
- 1 ≤ input[i] ≤ 10
- 0 ≤ S ≤ E ≤ N - 1
- No external libraries are allowed.
- The final result must be stored in the variable `output`.

## Solution

See [subarray_sum.py](./subarray_sum.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Subarray Sum](https://leetgpu.com/challenges/subarray-sum)
