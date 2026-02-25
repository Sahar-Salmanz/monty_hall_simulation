# Monty Hall Simulation
An interactive simulation of the classic Monty Hall Problem, built with Python and Streamlit.


## What is the Monty Hall Problem?
The Monty Hall Problem is a famous probability puzzle based on a game show scenario:  

1. You are shown 3 doors. Behind one is a car, behind the other two are goats.
2. You pick a door.
3. The host (Monty Hall), who knows what's behind each door, opens one of the remaining doors to reveal a goat.
4. You are given a choice: 
    - stick with your original door or 
    - switch to the other unopened door.  


__Should you switch?__  
Counterintuitively, yes!  
Switching wins 2/3 of the time, while staying wins only 1/3 of the time.  


## Project Structure
```
├── src/
│   └── monty_hall.py     # Core simulation logic
│   └── dashboard.py      # Streamlit dashboard
└── README.md
```

## How It Works
```src/monty_hall.py```  
Contains two functions:  
* `monty_hall_game(switch_doors: bool) -> bool` 
Simulates a single round of the Monty Hall game. Returns True if the player wins.
* `simulate_game(num_plays: int) -> tuple[float, float]`
Runs multiple rounds and returns the number of wins with and without switching.  


```src/dashboard.py```  
A Streamlit app that:

* Accepts a user-defined number of games to simulate (1–10,000).
* Runs the simulation game-by-game in real time.
* Displays two live line charts side by side, one for the win rate with switching and one without, updating as each game is played.


## Requirements
Python 3.10+  
pip