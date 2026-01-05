import torch


def solve(
    input: torch.Tensor,
    gamma: torch.Tensor,
    beta: torch.Tensor,
    output: torch.Tensor,
    N: int,
    C: int,
    eps: float,
):

    mean = input.mean(dim=0)

    var = input.var(dim=0, unbiased=False)

    normalized = (input - mean) / torch.sqrt(var + eps)

    output.copy_(gamma * normalized + beta)
