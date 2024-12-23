import mesa

from FuctionsRep import compute_gini


class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def _init_(self, unique_id, model):
        super()._init_(unique_id, model)
        self.wealth = 1

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def give_money(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            while True:
                other = self.random.choice(cellmates)
                if other.unique_id != self.unique_id:
                    break
            other.wealth += 1
            self.wealth -= 1
            print("Hi, I am agent "+str(self.unique_id)+" and I am giving my money to agent " + str(other.unique_id))


    def step(self):
        # The agent's step will go here.
        # For demonstration purposes we will print the agent's unique_id

        #no movement if there is no coin
        if self.wealth == 0:
            return

        self.move()
        if self.wealth > 0:
            self.give_money()


class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def _init_(self, N, width, height):
        self.num_agents = N
        self.grid = mesa.space.MultiGrid(width, height, True)
        self.schedule = mesa.time.RandomActivation(self)
        self.running = True

        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

            #a = agent (line 34)
            print("Hi, I am agent " + str(a.unique_id) + "." + " I am in cell " + (str(x)+":"+str(y)))

        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        )

    def step(self):
        """Advance the model by one step."""
        self.datacollector.collect(self)
        self.schedule.step()