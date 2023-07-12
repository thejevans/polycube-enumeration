"""
Docstring
"""

from collections import namedtuple
from enum import Enum
import sys
from typing import Optional

from numba import njit
import numpy as np
import scipy


Polycube = namedtuple('Polycube', ['x', 'y', 'z', 'run_encoding'])
PolycubeProjection = namedtuple('PolycubeProjection', ['area', 'sides'])
Degeneracy = Enum(
    'Degeneracy',
    ['NO_DEGENERACY', 'SINGLE_DEGENERACY', 'DOUBLE_DEGENERACY'],
)


def main() -> None:
    """
    Docstring
    """
    n_cubes = int(sys.argv[1])
    polycubes = get_polycubes(n_cubes)
    print(f'there are {len(polycubes)} of size {n_cubes}')


def get_polycubes(n_cubes: int) -> dict[Polycube, np.ndarray]:
    """
    Docstring
    """
    i_cube_polycubes = {Polycube(1, 1, 1, [1]): np.ones((1,1,1))}

    if n_cubes <= 1:
        return i_cube_polycubes

    for _ in range(1, n_cubes + 1):
        i_cube_polycubes = get_i_polycubes(i_cube_polycubes)

    return i_cube_polycubes


def get_i_polycubes(
    prev_polycubes: dict[Polycube, np.ndarray],
) -> dict[Polycube, np.ndarray]:
    """
    Docstring
    """
    computed_polycubes: dict[Polycube, np.ndarray] = {}

    for _, prev_polycube_arr in prev_polycubes.items():
        computed_polycubes.update(
            polycubes_from_prev_polycube(
                prev_polycube_arr,
                computed_polycubes,
            )
        )

    return computed_polycubes


def polycubes_from_prev_polycube(
    prev_polycube_arr: np.ndarray,
    computed_polycubes: dict[Polycube, np.ndarray],
) -> dict[Polycube, np.ndarray]:
    """
    Docstring
    """
    expanded_prev_polycube_arr = expand_polycube_arr(prev_polycube_arr)
    possible_cube_locations = get_next_cube_locations(expanded_prev_polycube_arr)

    for i, j, k in possible_cube_locations:
        possible_polycube_arr = expanded_prev_polycube_arr.copy()
        possible_polycube_arr[i, j, k] = 1

        polycube, rotated_trimmed_polycube_arr, degeneracy = new_polycube_from_arr(
                possible_polycube_arr)

        if polycube in computed_polycubes:
            continue

        new_polycubes = new_polycubes_given_degeneracy(
                rotated_trimmed_polycube_arr, degeneracy)

        for new_polycube in new_polycubes:
            computed_polycubes[new_polycube] = rotated_trimmed_polycube_arr

    return computed_polycubes


def expand_polycube_arr(
        polycube_arr: np.ndarray) -> np.ndarray:
    """
    Docstring
    """


def get_next_cube_locations(
        polycube_arr: np.ndarray) -> list[tuple[int, int, int]]:
    """
    Docstring
    """


def new_polycube_from_arr(
        polycube_arr: np.ndarray) -> tuple[Polycube, np.ndarray, Degeneracy]:
    """
    Docstring
    """


def new_polycubes_given_degeneracy(
    rotated_trimmed_polycube_arr: np.ndarray,
    degeneracy: Degeneracy,
) -> list[Polycube]:
    """
    Docstring
    """


def trim_polycube_arr(orient_polycube_arr: np.ndarray) -> np.ndarray:
    """
    Docstring
    """


if __name__ == '__main__':
    main()
