import random


def monty_hall_game(switch_doors: bool) -> bool:
    """Simulates a single play of the Monty Hall game.

    :param switch_doors: Whether the player decides to switch doors after Monty reveals a goat.
    :return: True if the player wins, False otherwise.
    """
    doors = ['goat', 'car',  'goat']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    if switch_doors == True:
        revealed_doors = [i for i in range(3) if i != initial_choice and doors[i] != 'car']
        revealed_door = random.choice(revealed_doors)
        final_choice = [i for i in range(3) if i != initial_choice and i != revealed_door][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == 'car'

def simulate_game(num_plays: int) -> tuple[float, float]:
    """Simulates multiple plays of the Monty Hall game.

    :param num_plays: The number of times to simulate the game.
    :return: A tuple containing the win rates with and without switching doors.
    """
    num_wins_without_switch = sum([monty_hall_game(False) for _ in range(num_plays)])
    num_wins_with_switch = sum([monty_hall_game(True) for _ in range(num_plays)])
    return num_wins_with_switch, num_wins_without_switch


# Test the simulation with 1000 plays
if __name__ == "__main__":
    switch_win_rate, no_switch_win_rate = simulate_game(1000)
    print(f"Win rate with switching: {switch_win_rate / 1000:.2%}")
    print(f"Win rate without switching: {no_switch_win_rate / 1000:.2%}")
