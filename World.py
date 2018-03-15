###
#
# Simple base for RL Enviorments in Terminal
#
# (Made for 2 agents with turn based movements, but can be extended for multiple agents)
# For Open Acess and Use
#
# Made by Willie McClinton at University of South Florida
#
###

import os

###
### Tools
###
from Body import Body

def make(state_array):
    state = ""
    for row in state_array:
        for block in row:
            state = state + block + " "
        state = state + "\n"
    return state

def demake(state):
    state_array = []
    rows = state.replace(" ","").split("\n")
    for row in rows:
        state_array.append(list(row))
    return state_array
###
###
###

SIZE_HEIGHT = 17
SIZE_WIDTH = 17
BLANK_STATE = "# "*SIZE_WIDTH + "\n" + ("# " + "_ "*(SIZE_WIDTH - 2) + "# " + "\n")*(SIZE_HEIGHT - 2) + "# "*SIZE_WIDTH

class World:
    ### GAME ADVANCED (need to be updated based on game type) ###
    def setup(self,reset=0):
        self.start_state = demake(BLANK_STATE)

        ## Assiging Objects Start Positions

        # Agents
        a1x, a1y = 5, 3
        if(not reset):
            self.agent1 = Body("agent1","A",[a1x,a1y])
        self.start_state[a1x][a1y] = self.agent1.symbol
        self.agent1.location = [a1x,a1y]

        a2x, a2y = 7, 8
        if(not reset):
            self.agent2 = Body("agent2","B",[a2x,a2y])
        self.start_state[a2x][a2y] = self.agent2.symbol
        self.agent2.location = [a2x,a2y]

        # Non Agents
        self.start_state[5][8] = "0"
        self.start_state[10][3] = "*"
        self.start_state[3][10] = "*"

        ##

        self.state = self.start_state

    def stats(self):
        # Render Condtions
        print("STATE " + self.agent1.symbol + " = " + self.agent1.conditon + "\n")
        print("STATE " + self.agent2.symbol + " = " + self.agent2.conditon + "\n")

    def wstep(self,name):
        done = 0
        # Logic of simple agent interaction
        if(name == self.agent1.name):
            if(abs(self.agent1.location[0] - self.agent2.location[0]) <= 1 and abs(self.agent1.location[1] - self.agent2.location[1]) <= 1):
                if(self.agent1.conditon == "+"):
                    self.agent2.conditon = "-"
        
        if(name == self.agent2.name):
            if(abs(self.agent1.location[0] - self.agent2.location[0]) <= 1 and abs(self.agent1.location[1] - self.agent2.location[1]) <= 1):
                if(self.agent2.conditon == "+"):
                    self.agent1.conditon = "-"

        # Logic of finishing game
        done = 1
        for row in self.state:
            for block in row:
                if(block == "*"):
                    done = 0
        return done

    def move(self,name,action):
        reward = 0
        # Assing Agent Movement
        if(name == self.agent1.name):
            self.state, reward = self.agent1.movement(self.state, action)
        if(name == self.agent2.name):
            self.state, reward = self.agent2.movement(self.state, action)

        # World step
        done = self.wstep(name)

        return reward, done

    ### GAME BASICS ###
    def __init__(self, name):
        self.name = name
        self.setup()
        
    def reset(self):
        self.setup(1)
    
    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(make(self.state))
        self.stats()

    def step(self,action,name):
        last_state = self.state
        reward, done = self.move(name, action)

        return self.state, reward, done