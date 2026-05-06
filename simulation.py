import random
import time
import multiprocessing as mp


def calculate_damage(player):
    damage = random.randint(player["min_attack"], player["max_attack"])

    if random.random() < player["crit_rate"]:
        damage *= 2

    return damage


def simulate_one_battle(player_a, player_b):
    hp_a = player_a["hp"]
    hp_b = player_b["hp"]

    while hp_a > 0 and hp_b > 0:
        damage_a = calculate_damage(player_a)
        hp_b -= damage_a

        if hp_b <= 0:
            return "A"

        damage_b = calculate_damage(player_b)
        hp_a -= damage_b

        if hp_a <= 0:
            return "B"

    return "A" if hp_a > 0 else "B"


def run_sequential(total_simulations, player_a, player_b):
    start_time = time.perf_counter()

    win_a = 0
    win_b = 0

    for _ in range(total_simulations):
        winner = simulate_one_battle(player_a, player_b)

        if winner == "A":
            win_a += 1
        else:
            win_b += 1

    end_time = time.perf_counter()

    return {
        "win_a": win_a,
        "win_b": win_b,
        "execution_time": end_time - start_time,
    }


def worker_simulation(args):
    simulation_count, player_a, player_b = args

    win_a = 0
    win_b = 0

    for _ in range(simulation_count):
        winner = simulate_one_battle(player_a, player_b)

        if winner == "A":
            win_a += 1
        else:
            win_b += 1

    return win_a, win_b


def run_parallel(total_simulations, process_count, player_a, player_b):
    start_time = time.perf_counter()

    base_count = total_simulations // process_count
    remainder = total_simulations % process_count

    tasks = []

    for i in range(process_count):
        count = base_count + (1 if i < remainder else 0)
        tasks.append((count, player_a, player_b))

    with mp.Pool(processes=process_count) as pool:
        results = pool.map(worker_simulation, tasks)

    win_a = sum(result[0] for result in results)
    win_b = sum(result[1] for result in results)

    end_time = time.perf_counter()

    return {
        "win_a": win_a,
        "win_b": win_b,
        "execution_time": end_time - start_time,
    }