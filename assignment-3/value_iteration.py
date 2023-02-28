class ValueIteration:
    def __init__(self, mdp, discount=0.9, iterations=100):
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = {}

    def run_value_iteration(self):
        for i in range(self.iterations):
            updated_values = {}
            for state in self.mdp.get_all_states():
                if self.mdp.is_terminal(state):
                    updated_values[state] = self.mdp.get_reward(state)
                else:
                    updated_values[state] = max(
                        [
                            self.compute_qvalue_from_values(state, action)
                            for action in self.mdp.get_possible_actions(state)
                        ]
                    )
            self.values = updated_values

    def get_value(self, state):
        if state in self.values:
            return self.values[state]
        else:
            return 0

    def compute_qvalue_from_values(self, state, action):
        q_value = 0
        for next_state, probability in self.mdp.get_next_states(state, action).items():
            q_value += probability * (
                self.mdp.get_reward(state, action, next_state)
                + self.discount * self.get_value(next_state)
            )
        return q_value

    def compute_action_from_values(self, state):
        if self.mdp.is_terminal(state):
            return None
        else:
            actions = self.mdp.get_possible_actions(state)
            best_value, best_action = max(
                [
                    (self.compute_qvalue_from_values(state, action), action)
                    for action in actions
                ]
            )
            return best_action

    def get_action(self, state):
        return self.compute_action_from_values(state)

    def get_qvalue(self, state, action):
        return self.compute_qvalue_from_values(state, action)

    def get_policy(self, state):
        if self.mdp.is_terminal(state):
            return None
        else:
            return self.get_action(state)
