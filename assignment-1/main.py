import random

class Bandit:
    def __init__(self, num_arms=10):
        self.arms = [random.uniform(-3,3) for i in range(num_arms)]
        self.reward = 0
        self.occurrences = [0] * num_arms
        self.cumulative_rewards = [0] * num_arms
        
    def choose_arm(self):
        arm = random.randint(0, len(self.arms)-1)
        self.occurrences[arm] += 1
        self.cumulative_rewards[arm] += self.arms[arm]
        Qta = self.cumulative_rewards[arm]/self.occurrences[arm]
        self.reward += Qta
        return Qta
        
    def run(self):
        expected_reward = []
        bandit = Bandit()
        for _ in range(1000):
            expected_reward.append(bandit.choose_arm())
        return expected_reward

if __name__ == "__main__":
    bandit_greedy = Bandit()
    print(bandit_greedy.run())
