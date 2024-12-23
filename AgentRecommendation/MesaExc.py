import matplotlib.pyplot as plt
import numpy as np

from money_model import *

import pandas as pd

nagents = 50
nsteps = 10

model = MoneyModel(nagents, 10, 10)
model.step()

agent_wealth = [a.wealth for a in model.schedule.agents]
plt.hist(agent_wealth)

plt.title("Coin Distribution")
plt.xlabel('Coins')
plt.ylabel('Agents')
plt.show()

all_wealth = []
# This runs the model nagent*10 (l26).
for j in range(nagents):
    # Run the model

    for i in range(nsteps):
        model.step()

    # Store the results
for agent in model.schedule.agents:
    all_wealth.append(agent.wealth)


plt.hist(all_wealth, bins=range(max(all_wealth) + 1))

plt.title("Final Coin Distribution")
plt.xlabel('Coins')
plt.ylabel('Agents')
plt.show()

agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation="nearest")
plt.colorbar()
plt.show()

gini = model.datacollector.get_model_vars_dataframe()
gini.plot()
plt.show()

agent_wealth = model.datacollector.get_agent_vars_dataframe()
agent_wealth.head()

end_wealth = agent_wealth.xs(1, level="Step")["Wealth"]
end_wealth.hist(bins=range(agent_wealth.Wealth.max() + 1))

plt.show()


end_wealth = agent_wealth.xs(500, level="Step")["Wealth"]
end_wealth.hist(bins=range(agent_wealth.Wealth.max() + 1))

plt.show()


one_agent_wealth = agent_wealth.xs(49, level="AgentID")
one_agent_wealth.Wealth.plot()

plt.show()

params = {"width": 10, "height": 10, "N": range(10, 500, 10)}

#Batch
results = mesa.batch_run(
    MoneyModel,
    parameters=params,
    iterations=5,
    max_steps=10,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)

results_df = pd.DataFrame(results)
print(results_df.keys())

results_filtered = results_df[(results_df.AgentID == 0) & (results_df.Step == 10)]
N_values = results_filtered.N.values
gini_values = results_filtered.Gini.values
plt.scatter(N_values, gini_values)

plt.show()