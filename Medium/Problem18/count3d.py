import torch


def solve(input: torch.Tensor, output: torch.Tensor, N: int, M: int, K: int, P: int):
    mask = input == P

    count = mask.sum()

    output[0] = count
