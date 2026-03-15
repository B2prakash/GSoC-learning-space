import mesa
from mesa.discrete_space import OrthogonalMooreGrid, CellAgent


class WealthAgent(CellAgent):
    """An agent with a fixed amount of wealth."""

    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1

    def step(self):
        if self.wealth > 0:
            # Pick a random neighbor
            neighbors = list(self.cell.neighborhood.agents)
            if neighbors:
                other = self.random.choice(neighbors)
                # Give 1 wealth to neighbor
                other.wealth += 1
                self.wealth -= 1


class WealthModel(mesa.Model):
    """Simple model of wealth distribution."""

    def __init__(self, num_agents=50, width=10, height=10):
        super().__init__()
        self.grid = OrthogonalMooreGrid(
            (width, height), torus=True, random=self.random
        )
        self.datacollector = mesa.DataCollector(
            agent_reporters={"Wealth": "wealth"}
        )

        # Create agents on random cells
        for _ in range(num_agents):
            cell = self.grid.all_cells.select_random_cell()
            agent = WealthAgent(self)
            agent.cell = cell

        self.datacollector.collect(self)

    def step(self):
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)


if __name__ == "__main__":
    model = WealthModel()
    for i in range(50):
        model.step()

    data = model.datacollector.get_agent_vars_dataframe()
    print("\nWealth distribution after 50 steps:")
    print(data.groupby("Step")["Wealth"].describe().tail(10))
