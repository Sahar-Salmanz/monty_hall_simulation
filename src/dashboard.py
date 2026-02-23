import time
import streamlit as st
from src.monty_hall import simulate_game


st.title(":zap: Monty Hall Simulation")
st.image("https://static.scientificamerican.com/dam/m/7268d6df988be0a/original/saw0924Pars_lead.jpg?m=1720544368.494&w=1200")

num_of_games = st.number_input(
    "Enter number of games to simulate", 
    min_value=1, max_value=10000, 
    value=100
)

col1, col2 = st.columns(2)
col1.subheader("Win Percentage with Switching")
col2.subheader("Win Percentage without Switching")

chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)

wins_switch = 0
wins_no_switch = 0

for i in range(num_of_games):
    num_wins_with_switch, num_wins_without_switch = simulate_game(1)
    wins_switch += num_wins_with_switch
    wins_no_switch += num_wins_without_switch

    chart1.add_rows([wins_switch / (i + 1)])
    chart2.add_rows([wins_no_switch / (i + 1)])

    time.sleep(0.01)