import torch
import torch.nn.functional as F


def solve(
    input: torch.Tensor,
    kernel: torch.Tensor,
    output: torch.Tensor,
    input_depth: int,
    input_rows: int,
    input_cols: int,
    kernel_depth: int,
    kernel_rows: int,
    kernel_cols: int,
):

    I = input.view(1, 1, input_depth, input_rows, input_cols)

    K = kernel.view(1, 1, kernel_depth, kernel_rows, kernel_cols)

    result = F.conv3d(I, K)

    output.copy_(result.view_as(output))
