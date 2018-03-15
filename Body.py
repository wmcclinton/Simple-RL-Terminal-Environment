###
#
# Simple base for Agent in world
#
# For Open Acess and Use
#
# Made by Willie McClinton at University of South Florida
#
###

# Basic model of agent with 2-D moverment, attack, and harm
class Body:
    def __init__(self, name, symbol, location):
        self.name = name
        self.symbol = symbol
        self.location = location
        self.conditon = "0"

    # Logic for allowed movement
    def movement(self, state, action):
        reward = 0
        # Logic of simple agent interaction reaction
        harm = 1
        if(self.conditon == "-"):
            reward = reward - harm
            self.conditon = "0"

        if(action == "ATTACK"):
            self.conditon = "+"
            return state, reward

        # Logic of basic movement
        if(action == "RIGHT" and state[self.location[0]][self.location[1] + 1] == "_"):
            state[self.location[0]][self.location[1]] = "_"
            state[self.location[0]][self.location[1] + 1] = self.symbol
            self.location[1] = self.location[1] + 1

            self.conditon = "0"
            return state, reward

        if(action == "LEFT" and state[self.location[0]][self.location[1] - 1] == "_"):
            state[self.location[0]][self.location[1]] = "_"
            state[self.location[0]][self.location[1] - 1] = self.symbol
            self.location[1] = self.location[1] - 1

            self.conditon = "0"
            return state, reward

        if(action == "UP" and state[self.location[0] - 1][self.location[1]] == "_"):
            state[self.location[0]][self.location[1]] = "_"
            state[self.location[0] - 1][self.location[1]] = self.symbol
            self.location[0] = self.location[0] - 1

            self.conditon = "0"
            return state, reward

        if(action == "DOWN" and state[self.location[0] + 1][self.location[1]] == "_"):
            state[self.location[0]][self.location[1]] = "_"
            state[self.location[0] + 1][self.location[1]] = self.symbol
            self.location[0] = self.location[0] + 1

            self.conditon = "0"
            return state, reward

        # Logic of conditional movement
        star_reward = 1
        if(action == "RIGHT" and state[self.location[0]][self.location[1] + 1] == "*"):
            state[self.location[0]][self.location[1]] = "_"
            state[self.location[0]][self.location[1] + 1] = self.symbol
            self.location[1] = self.location[1] + 1

            self.conditon = "*"
            return state, reward + star_reward

        if(action == "LEFT" and state[self.location[0]][self.location[1] - 1] == "*"):
            state[self.location[0]][self.location[1]] = "_"
            state[self.location[0]][self.location[1] - 1] = self.symbol
            self.location[1] = self.location[1] - 1

            self.conditon = "*"
            return state, reward + star_reward

        if(action == "UP" and state[self.location[0] - 1][self.location[1]] == "*"):
            state[self.location[0]][self.location[1]] = "_"
            state[self.location[0] - 1][self.location[1]] = self.symbol
            self.location[0] = self.location[0] - 1

            self.conditon = "*"
            return state, reward + star_reward

        if(action == "DOWN" and state[self.location[0] + 1][self.location[1]] == "*"):
            state[self.location[0]][self.location[1]] = "_"
            state[self.location[0] + 1][self.location[1]] = self.symbol
            self.location[0] = self.location[0] + 1

            self.conditon = "*"
            return state, reward + star_reward
        
        #self.conditon = "s"
        return state, 0