# Fast Fourier Transform (FFT) (Hard)

This problem requires you to implement the **Fast Fourier Transform (FFT)** for a complex-valued 1-D signal on the GPU, **without using any external libraries** (such as cuFFT).

## Problem Statement

Given:

- `signal`: An input array of length `2 × N` containing `N` complex numbers, stored as interleaved real/imaginary pairs: `[real₀, imag₀, real₁, imag₁, ...]`
- `N`: The number of complex values

Compute the discrete Fourier transform (DFT) of the input using the FFT algorithm and store the result in the `spectrum` array (also interleaved real/imaginary pairs).

The FFT reduces the computational complexity from O(N²) to O(N log N) by exploiting symmetries in the twiddle factors.

**Both input and output arrays use interleaved real/imaginary layout.**

## Example

**Example 1:**

- Input:
  `N = 4`
  `signal = [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]`
  (represents: [1+0j, 0+0j, 0+0j, 0+0j])
- Output:
  `spectrum = [1.0, 0.0, 1.0, 0.0, 1.0, 0.0, 1.0, 0.0]`
  (represents: [1+0j, 1+0j, 1+0j, 1+0j])

**Example 2:**

- Input:
  `N = 2`
  `signal = [1.0, 0.0, 1.0, 0.0]`
  (represents: [1+0j, 1+0j])
- Output:
  `spectrum = [2.0, 0.0, 0.0, 0.0]`
  (represents: [2+0j, 0+0j])

## Constraints

- 1 ≤ N ≤ 262,144
- All values are 32-bit floating point numbers
- Absolute error ≤ 1e-3 and relative error ≤ 1e-3
- Input and output arrays have length `2 × N`
- No external libraries (cuFFT etc.) are permitted
- The kernel must be entirely GPU-resident—no host-side FFT calls

## Solution

See [fft.py](./fft.py) for a python implementation.

## Additional Information

For more details and to try the problem online, visit:
[Fast Fourier Transform](https://leetgpu.com/challenges/fast-fourier-transform)
