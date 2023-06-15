For Question 1 

Reflex Agent Evaluation Function:
 
This code provides an evaluation function for Pac-Man game agents. The function takes in the current game state and an action, and returns a score indicating the desirability of taking that action in the current state. The score is based on several factors, including the distance to the nearest food pellet, the distance to the nearest power capsule, and the proximity of any ghosts.

Factors considered in the evaluation function:
Distance to nearest food pellet: The function calculates the Manhattan distance between Pac-Man's position and each remaining food pellet on the game board. It then returns the minimum distance among those calculated distances. This factor incentivizes Pac-Man to move towards the nearest food pellet.

Distance to nearest power capsule: The function also considers the distance to the nearest power capsule, which Pac-Man can consume to temporarily turn the tables on the ghosts. If there are no power capsules remaining, the distance to the nearest food pellet is used instead. This factor incentivizes Pac-Man to collect power capsules when they are nearby.

Proximity of ghosts: If any ghosts are nearby, the function considers their proximity and whether they are currently scared or not. If a non-scared ghost is too close to Pac-Man, the function returns a negative infinity score, incentivizing Pac-Man to move away. If a scared ghost is nearby, the function returns a positive infinity score, incentivizing Pac-Man to move towards and eat the ghost.

Current state of the game: The function also checks whether Pac-Man is currently at a stop, in which case it returns a negative infinity score to prevent Pac-Man from stopping indefinitely. If Pac-Man has eaten a food pellet in this turn, it returns a positive infinity score to incentivize Pac-Man to keep moving and collect more pellets.

Why we return -1 * min_distance
The evaluation function calculates the distance to the nearest food pellet or power capsule, and returns the negative of that distance. This means that the closer the nearest pellet or capsule, the more positive the score returned by the function. The reason for negating the distance is to ensure that the function returns a higher score for closer distances, as higher scores indicate better actions for Pac-Man to take.

############################################################################################################################################################################

For Question 2

Minimax:

since I have already written as a comment for almost every line what the function does, I will just explain the idea of ​​the code here


The MinimaxAgent's getAction method returns the optimal action for the current state of the game, using the minimax algorithm. The minimax algorithm is a recursive function, calcMinimaxValue, that computes the minimax value of the current state, given the current depth and the current agent.

The calcMinimaxValue function returns a tuple with the minimax value and the optimal action for the current state. The algorithm is designed to work for any number of agents, but in the case of the Pacman game, there is only one Pacman agent and multiple ghost agents.

If the current agent is the Pacman agent, the function returns the maximum of the minimax values of the successor states. If the current agent is a ghost agent, the function returns the minimum of the minimax values of the successor states.

If the depth limit is reached or the game is over, the function returns the evaluation value of the current state and None for the action.

The algorithm works by recursively exploring the game tree of all possible actions and their outcomes until it reaches a terminal state or the maximum depth. It then backtracks to compute the minimax value of each state and return the optimal action.

#############################################################################################################################################################################

For Question 3

AlphaBetaAgent: 


The maxLevel function takes as input the current game state, the current depth of the tree, alpha and beta, which are the values for alpha-beta pruning, and returns the maximum possible score for the current player from the given game state. If the maximum depth is reached, or if the state is a final state (win/loss), the function returns the evaluation value of the given state. Otherwise, it generates the successor states of the given state and calls the minLevel function for each successor state. It returns the maximum score among the scores returned by the calls to minLevel.

The minLevel function is similar to maxLevel, but it computes the minimum possible score for the current player from the given game state.

The actions variable contains the list of legal actions for the Pacman agent in the current game state.

The currentScore variable is initialized to -inf, because we want to find the best possible action to maximize the score.

The returnAction variable is initialized to an empty string, because it will be filled with the best possible action.

The alpha and beta variables are initialized to -inf and +inf, respectively, because we start by assuming that the best possible value is in the interval [-inf, +inf].

Updating alpha value at root.
When exploring the tree, we update the value of alpha if we find a better value than the currently stored one. If we find a value greater than beta, it means that the opponent player has a better option available and we can stop searching and return the best action found so far. If no value greater than beta is found, we continue exploring the tree and updating the value of alpha until all legal actions have been explored. Finally, we return the best action found.

#############################################################################################################################################################################

For Question 4

Expectimax:

I will detail precisely the different implementations of this section of the code

minimaxes: This is a list of tuples, where each tuple represents the minimax value of a new state generated by taking one of the legal actions for the current agent in the current state, and the action taken to reach that state.

minimaxes_vals: This is a list of the minimax values of the new states generated by the current agent in the current state.

avg: This is the average of the minimax values of the new states generated by the current agent in the current state.

None: This value is passed along with the average minimax value in the tuple returned by the calcMinimaxValue function to indicate that the best action cannot be determined from the current state. The direction from which we came to 

this state is lost, so we cannot return the action that leads to this state.
The calcMinimaxValue function returns a tuple containing the minimax value and the action that leads to the state that has the minimax value. If the current state is a terminal state or if the maximum depth is reached, the function returns the evaluation score of the current state and None. If it is Pacman's turn, the function returns the maximum minimax value and the action that leads to that state. If it is a ghost's turn, the function returns the average minimax value of the new states generated by that ghost and None.

#############################################################################################################################################################################

For Question 5

Better Evaluation Function:

This function is an evaluation function for the Pacman game. The evaluation function takes the current state of the game as an input and calculates a score that represents how desirable the state is. The function calculates the score based on the following factors:

The current score of the game.
The distance to the food pellets from the current position of Pacman.
The number of remaining food pellets in the game.
The distance to each ghost from the current position of Pacman.
The number of power pellets left in the game.
The time left for each ghost to remain in the scared state.
The function calculates the Manhattan distance to each food pellet from the current position of Pacman and adds up the distances. It also calculates the Manhattan distance to each ghost from the current position of Pacman and adds up the distances. If there are any power pellets left, it subtracts their number from the total score. If the ghosts are currently in the scared state, it adds up their remaining time in the scared state and subtracts the sum of the distances to the ghosts from the score. Otherwise, it adds up the distances to the ghosts and the number of power pellets left in the game to the score.

The function returns the final score, which is used by the game to determine the best move for Pacman.

##############################################################################################################################################################################


