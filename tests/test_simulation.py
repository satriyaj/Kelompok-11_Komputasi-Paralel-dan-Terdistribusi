import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from simulation import (
    calculate_damage,
    simulate_one_battle,
    run_sequential,
    run_parallel
)

from simulation import (
    calculate_damage,
    simulate_one_battle,
    run_sequential,
    run_parallel
)

PLAYER_A = {
    "name":"Reaper",
    "hp":110,
    "min_attack":9,
    "max_attack":20,
    "crit_rate":0.22
}

PLAYER_B = {
    "name":"Cyber Mage",
    "hp":95,
    "min_attack":11,
    "max_attack":22,
    "crit_rate":0.18
}


# TEST 1
# Damage tidak boleh negatif
def test_damage_positive():

    damage=calculate_damage(PLAYER_A)

    assert damage>0


# TEST 2
# Pemenang hanya A atau B
def test_battle_result():

    winner=simulate_one_battle(
        PLAYER_A,
        PLAYER_B
    )

    assert winner in ["A","B"]


# TEST 3
# Sequential jalan
def test_sequential_runs():

    result=run_sequential(
        100,
        PLAYER_A,
        PLAYER_B
    )

    assert result["win_a"]+result["win_b"]==100


# TEST 4
# Parallel jalan
def test_parallel_runs():

    result=run_parallel(
        100,
        2,
        PLAYER_A,
        PLAYER_B
    )

    assert result["win_a"]+result["win_b"]==100


# TEST 5
# Correctness:
# total simulasi harus sama

def test_correctness():

    seq=run_sequential(
        1000,
        PLAYER_A,
        PLAYER_B
    )

    par=run_parallel(
        1000,
        4,
        PLAYER_A,
        PLAYER_B
    )

    seq_total=seq["win_a"]+seq["win_b"]

    par_total=par["win_a"]+par["win_b"]

    assert seq_total==par_total