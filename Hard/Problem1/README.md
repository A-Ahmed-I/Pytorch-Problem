# 3D Convolution (Hard)

This problem requires you to implement a **3D convolution operation** on a 3D input volume using a 3D kernel (filter), **without using any external libraries**.

## Problem Statement

Given:

- `input`: A 3D volume of 32-bit floats, represented as a 1D array (row-major, then depth)
- `kernel`: A 3D kernel of 32-bit floats, also as a 1D array (row-major, then depth)
- `input_depth`, `input_rows`, `input_cols`: Dimensions of the input volume
- `kernel_depth`, `kernel_rows`, `kernel_cols`: Dimensions of the kernel

Compute the "valid" 3D convolution (no padding).
The output is a 1D array (row-major, then depth) with dimensions:

- `output_depth = input_depth - kernel_depth + 1`
- `output_rows = input_rows - kernel_rows + 1`
- `output_cols = input_cols - kernel_cols + 1`

For each output position `(d, i, j)`, the value is:

```
output[d, i, j] = sum_{kd=0}^{kernel_depth-1} sum_{kr=0}^{kernel_rows-1} sum_{kc=0}^{kernel_cols-1}
    input[(d+kd)*input_rows*input_cols + (i+kr)*input_cols + (j+kc)] *
    kernel[kd*kernel_rows*kernel_cols + kr*kernel_cols + kc]
```

The final result must be stored in the `output` array.

## Example

*Note: Specific example values are not provided in the original problem statement.*

## Constraints

- 1 ≤ input_depth, input_rows, input_cols ≤ 256
- 1 ≤ kernel_depth, kernel_rows, kernel_cols ≤ 5
- kernel_depth ≤ input_depth
- kernel_rows ≤ input_rows
- kernel_cols ≤ input_cols
- No external libraries are allowed.
- The final result must be stored in `output`.

## Solution

See [convolution_3d.py](./convolution_3d.py) for a Python implementation.

## Additional Information

For more details and to try the problem online, visit:
[3D Convolution](https://leetgpu.com/challenges/3d-convolution)
