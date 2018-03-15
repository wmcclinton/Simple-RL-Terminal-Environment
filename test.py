###
#
# Simple script for using world
#
# (Made for 2 agents with turn based movements, but can be extended for multiple agents)
# For Open Acess and Use
#
# Made by Willie McClinton at University of South Florida
#
###

from World import World
import numpy as np
import time

# Creates new World
test_world = World("Test")

# Display World in Terminal
test_world.render()
done = 0

while(not done):
    test_world.render()
    time.sleep(0.25)

    # Chose random actions
    random_action_agent1 = ["RIGHT","LEFT","UP","DOWN","ATTACK"][np.random.randint(5)]
    random_action_agent2 = ["RIGHT","LEFT","UP","DOWN","ATTACK"][np.random.randint(5)]

    # Take action
    state1, reward1, done = test_world.step(random_action_agent1,test_world.agent1.name)
    state2, reward2, done = test_world.step(random_action_agent2,test_world.agent2.name)

# Resets world just so you know how
test_world.reset()

# Prints Final Values
print(state1)
print(reward1)
print(done)