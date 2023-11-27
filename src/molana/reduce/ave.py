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
    assert Nrepeat * Nevery < Nfreq, "Nrepeat*Nevery must be less than Nfreq"

    x = np.array(x)[Nstart:Nend]
    x = x[len(x) % Nfreq :]
    x = x.reshape(-1, Nfreq)
    x = x[..., len(x) - Nevery * Nrepeat - 1 : None : Nevery]
    assert x.shape[-1] == Nrepeat, "x.shape[-1] must be equal to Nrepeat, or it;s a bug"
    x = x.mean(axis=1)

    return x
