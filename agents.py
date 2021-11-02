# Include your imports here, if any are used.

student_name = "Jingyi Lu"

# 1. Value Iteration
class ValueIterationAgent:
    """Implement Value Iteration Agent using Bellman Equations."""

    def __init__(self, game, discount):
        """Store game object and discount value into the agent object,
        initialize values if needed.
        """
        self.game = game
        self.discount = discount #gamma
        d = dict.fromkeys(game.states, 0) #initialize
        #terminal states
        d[(0,3)] = 0
        d[(1,3)] = 0
        self.values = d 

    def get_value(self, state):
        """Return value V*(s) correspond to state.
        State values should be stored directly for quick retrieval.
        """
        return self.values.get(state)
        #return self.values[state] # TODO

    def get_q_value(self, state, action):
        """Return Q*(s,a) correspond to state and action.
        Q-state values should be computed using Bellman equation:
        Q*(s,a) = Σ_s' T(s,a,s') [R(s,a,s') + γ V*(s')]
        """ 
        q_value = 0
        trans = self.game.get_transitions(state, action)
        for (sp, prob) in trans.items(): #it returns a dic
            if self.get_value(sp) is None:
                self.values[sp] = 0
            q_value = q_value + prob*(self.game.get_reward(state, action, sp)  + self.discount*self.get_value(sp) )
        return q_value
   
        

    def get_best_policy(self, state):
        """Return policy π*(s) correspond to state.
        Policy should be extracted from Q-state values using policy extraction:
        π*(s) = argmax_a Q*(s,a)
        """
        max_action = None
        max_value = float('-inf')
        for action in self.game.get_actions(state):
            value = self.get_q_value(state, action)
            if value > max_value:
                max_value = value
                max_action = action
        return max_action


    def iterate(self):
        """Run single value iteration using Bellman equation:
        V_{k+1}(s) = max_a Q*(s,a)
        Then update values: V*(s) = V_{k+1}(s)
        """
        
        new_values = dict.fromkeys(self.game.states, 0)
        for state in self.game.states:
            max_current_state_value = float('-inf')
            for action in self.game.get_actions(state):
                value = self.get_q_value(state, action)
                if value > max_current_state_value:
                    max_current_state_value = value
            new_values[state] = max_current_state_value
        self.values = new_values
        
        #pass

# 2. Policy Iteration
class PolicyIterationAgent(ValueIterationAgent):
    """Implement Policy Iteration Agent.

    The only difference between policy iteration and value iteration is at
    their iteration method. However, if you need to implement helper function or
    override ValueIterationAgent's methods, you can add them as well.
    """
  
    

    def iterate(self):
        """Run single policy iteration.
        Fix current policy, iterate state values V(s) until |V_{k+1}(s) - V_k(s)| < ε
        """
        epsilon = 1e-6
 #       policy = {game.states -> self.get_best_policy(states)}
 #       policy = dict.fromkeys(self.game.states,0)
        policy = {}
        for state in self.game.states:
            policy[state] = self.get_best_policy(state)
        
        while True:
            max_delta = 0
            for s in self.game.states:
                action = policy[s]
                value_before = self.get_value(s)
                value_after = self.get_q_value(s, action)
                self.values[s] = value_after
                diff = abs(value_before-value_after)
                max_delta = max(max_delta, diff)
            if(max_delta < epsilon):
                return


# 3. Bridge Crossing Analysis
def question_3():
    discount = 0.9
    noise = 0.001
    return discount, noise

# 4. Policies
def question_4a():
    discount = 0.3
    noise = 0.01
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4b():
    discount = 0.3
    noise = 0.2
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4c():
    discount = 0.9
    noise = 0.01
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4d():
    discount = 0.9
    noise = 0.2
    living_reward = 0.0
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'


def question_4e():
    discount = 0.01
    noise = 0.2
    living_reward = 12
    return discount, noise, living_reward
    # If not possible, return 'NOT POSSIBLE'

# 5. Feedback
# Just an approximation is fine.
feedback_question_1 = 6

feedback_question_2 = """
It's good.
"""

feedback_question_3 = """
This one is very fun. And the TA is very clear about the process.
"""
