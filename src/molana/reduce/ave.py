# author: Roy Kid
# contact: lijichen365@126.com
# date: 2023-11-27
# version: 0.0.1

from typing import Optional
import numpy as np


def ave(
    x: np.ndarray,
    Nevery: int,
    Nrepeat: int,
    Nfreq: int,
    Nstart: int = 0,
    Nend: Optional[int] = None,
):
    axis = 0
    assert Nrepeat * Nevery <= Nfreq, "Nrepeat*Nevery must be less than Nfreq"

    x = np.array(x)[Nstart:Nend]
    x = x[len(x) % Nfreq :]  # to make len(x) % Nfreq == 0
    x = x.reshape(-1, Nfreq, *x.shape[1:])
    x = x[:, :x.shape[axis+1]-Nevery*Nrepeat-1:-Nevery, ...]
    x = x[:, ::-1, ...]
    x = x.reshape(-1, *x.shape[axis+1:])
    x = x.mean(axis=axis)
    return x.squeeze()
    