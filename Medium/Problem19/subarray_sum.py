import torch


def solve(input: torch.Tensor, output: torch.Tensor, N: int, S: int, E: int):
    sum = input[S : E + 1].sum()

    output[0] = sum
