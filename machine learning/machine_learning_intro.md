## Machine Learning

1. Supervised Learning
Supervised learning is a type of machine learning where the model is trained using <b>labeled data.</b> This means each training example has an input and known correct output.<br>
Goal: Learn a mapping from inputs -> outputs so it can predict correctly on new data.<br>
Types:
1. Classification:
- Output is categorical (classes/labels)
- Example, Spam vs Not Spam, Disease vs No Disease
2. Regression:
- Output is continuous (numeric values)
- Example: Predicting house prices, temperature

2. Unsupervised Learning
Defintion: Unsupervised learning uses <b>unlabeled data,</b> meaning the model tries to find hidden patterns or structures in the data without predefined outputs.<br>
Goal: Discover underlying structure in data.<br>
Types:
1. Clustering:
- Group similar data points together
- Example: Customer segmentation

2. Association:
- Find relationships between values
- Example: Market basket analysis ("people who buy X also buy Y")

3. Dimensionality Reduction
- Reduce number of features while preserving important information
- Example: Data visualization, noise reduction

3. Reinforcement Learning (RL)
Defintion: Reinforcement learning is a type of learning where an agent interacts with an environment and learns by receiving rewards or penalties based on its actions.<br>
Goal: Learning a stratergy (policy) that maximizes cumulative reward over time.<br>
Key Components:
- Agent (learner/decision maker)
- Environment (where agent operates)
- Actions (choices made)
- Rewards (feedback signal)

Types:
- Model-Based RL
    - Agent builds a model of the environment before acting
- Model-Free RL
    - Learns directly from experience without building a model
    - Further divide into:
        - Value-Based (e.g., Q-learning)
        - Policy-Based
        - Actor-Critic methods