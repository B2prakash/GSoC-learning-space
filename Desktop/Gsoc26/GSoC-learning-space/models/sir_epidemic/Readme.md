# SIR Epidemic Model

## What the Model Does

This is an agent-based simulation of an SIR (Susceptible-Infected-Recovered) epidemic spreading through a population. In the SIR model:

- **Susceptible** agents can become infected
- **Infected** agents spread the disease to nearby susceptible agents and eventually recover
- **Recovered** agents are immune and cannot be reinfected

The model demonstrates how infectious diseases spread through a population over time, showing the classic epidemic curve with an initial outbreak, peak infection rate, and eventual decline as immunity builds.

## Why I Chose This Model

I chose the SIR model because it's a fundamental epidemiological model that's widely used in public health and has clear, interpretable dynamics. It's simple enough to implement as a first Mesa model but complex enough to demonstrate key agent-based modeling concepts like agent states, spatial interactions, and stochastic processes. The SIR model also has real-world relevance, especially in the context of understanding disease spread patterns.

## Mesa Features Used

This model uses several key Mesa features:

- **Discrete Space**: Uses `OrthogonalMooreGrid` for spatial movement and neighbor interactions
- **Cell Agents**: Agents live in grid cells and interact with neighboring cells
- **Data Collection**: `DataCollector` tracks the number of agents in each state over time
- **Random Movement**: Agents move randomly to adjacent cells each step
- **Stochastic Processes**: Infection and movement use random number generation

## How to Run the Model

```bash
cd models/sir_epidemic
python model.py
```

This will run the simulation for 50 steps and print a table showing the count of Susceptible, Infected, and Recovered agents at each step.

## Model Parameters

- `num_agents` (default 100): Total number of agents in the simulation
- `width`, `height` (default 20x20): Grid dimensions
- `infection_rate` (default 0.3): Probability of infection when an infected agent encounters a susceptible one
- `recovery_time` (default 10): Number of steps an infected agent takes to recover
- `initial_infected` (default 1): Number of agents that start infected

## What I Learned Building It

The biggest thing I learned was that Mesa 4.0 is very different from the tutorials online — most resources still use MultiGrid and RandomActivation which are deprecated. I had to figure out OrthogonalMooreGrid and CellAgent by exploring the actual module with dir(). The cell-based movement was confusing at first but it's actually cleaner once you get it. I also got a much better understanding of how agent states work in practice, and how data collection can turn agent behaviors into meaningful time series data.

## What Was Hard

The most challenging aspects were:

- **API Migration**: Adapting from Mesa 2.x style (MultiGrid, Agent) to Mesa 4.0 (OrthogonalMooreGrid, CellAgent)
- **Cell-Based Movement**: Understanding how agents move between cells in the discrete space system
- **Neighbor Interactions**: Figuring out how to access neighboring agents through the cell neighborhood system

## What Surprised Me

I was surprised by how quickly the epidemic dynamics emerged from simple rules. Even with basic random movement and infection rules, the model produced realistic epidemic curves with clear phases of outbreak, peak, and resolution. The spatial aspect also added interesting patterns - the disease spread in waves through the grid.