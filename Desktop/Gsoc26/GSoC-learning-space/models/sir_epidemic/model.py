import mesa
import numpy as np
from mesa.discrete_space import OrthogonalMooreGrid, CellAgent


class Person(CellAgent):
    """An agent representing a person in the SIR model."""

    def __init__(self, model, initial_state):
        super().__init__(model)
        self.state = initial_state
        self.infection_timer = 0
        self.recovery_time = model.recovery_time

    def step(self):
        # Move randomly
        neighborhood = self.cell.neighborhood
        self.cell = neighborhood.select_random_cell()
        
        # If infected, try to spread
        if self.state == "Infected":
            neighbors = self.cell.neighborhood.agents
            for neighbor in neighbors:
                if neighbor.state == "Susceptible" and self.random.random() < self.model.infection_rate:
                    neighbor.state = "Infected"
        
        # Check recovery
        if self.state == "Infected":
            self.infection_timer += 1
            if self.infection_timer >= self.recovery_time:
                self.state = "Recovered"


class SIRModel(mesa.Model):
    """A simple SIR epidemic model."""

    def __init__(self, num_agents=100, width=20, height=20,
                infection_rate=0.3, recovery_time=10, initial_infected=1):
        super().__init__()
        self.infection_rate = infection_rate
        self.recovery_time = recovery_time
        # Create grid
        self.grid = OrthogonalMooreGrid((width, height), torus=True)
        # Create DataCollector to count S, I, R
        self.datacollector = mesa.DataCollector(
            model_reporters={
                "Susceptible": lambda m: sum(1 for a in m.agents if a.state == "Susceptible"),
                "Infected": lambda m: sum(1 for a in m.agents if a.state == "Infected"),
                "Recovered": lambda m: sum(1 for a in m.agents if a.state == "Recovered"),
            }
        )
        # Create agents and place on grid
        for i in range(num_agents):
            state = "Susceptible"
            cell = self.grid.all_cells.select_random_cell()
            agent = Person(self, state)
            agent.cell = cell
        # Start with a few infected agents
        infected_cells = self.random.sample(list(self.grid.all_cells), initial_infected)
        for cell in infected_cells:
            agent = Person(self, "Infected")
            agent.cell = cell

    def step(self):
        # Advance all agents by one step
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)


if __name__ == "__main__":
    model = SIRModel()
    for i in range(50):
        model.step()
    data = model.datacollector.get_model_vars_dataframe()
    print(data)