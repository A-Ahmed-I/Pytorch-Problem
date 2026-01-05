# Batch Normalization (Medium)

This problem requires you to implement the **batch normalization forward pass** for 2D input tensors, **without using any external libraries**.

## Problem Statement

Given:

- `input`: A 2D tensor of shape `[N, C]` where `N` is the batch size and `C` is the number of features
- `gamma`: A 1D tensor of shape `[C]` (learnable scale parameter)
- `beta`: A 1D tensor of shape `[C]` (learnable shift parameter)
- `eps`: A small constant for numerical stability (typically `1e-5`)

For each feature channel `j`, batch normalization computes:

```
output[i, j] = gamma[j] * (input[i, j] - mean[j]) / sqrt(var[j] + eps) + beta[j]
```

where `mean[j]` and `var[j]` are the mean and variance of the `j`-th feature across the batch.

The final result must be stored in the `output` tensor.

## Example

**Example 1:**

- Input:
  `input = [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]`  (N=3, C=2)
  `gamma = [1.0, 1.0]`
  `beta = [0.0, 0.0]`
  `eps = 1e-5`
- Output:
  `output = [[-1.224, -1.224], [0.0, 0.0], [1.224, 1.224]]`

**Example 2:**

- Input:
  `input = [[0.0, 1.0], [2.0, 3.0]]`  (N=2, C=2)
  `gamma = [2.0, 0.5]`
  `beta = [1.0, -1.0]`
  `eps = 1e-5`
- Output:
  `output = [[-1.0, -1.5], [3.0, -0.5]]`

## Constraints

- 1 ≤ N ≤ 10,000
- 1 ≤ C ≤ 1,024
- eps = 1e-5
- -100.0 ≤ input values ≤ 100.0
- 0.1 ≤ gamma values ≤ 10.0
- -10.0 ≤ beta values ≤ 10.0
- No external libraries are allowed.
- The final result must be stored in the output tensor.

## Solution

See [batch_normalization.py](./batch_normalization.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Batch Normalization](https://leetgpu.com/challenges/batch-normalization)
