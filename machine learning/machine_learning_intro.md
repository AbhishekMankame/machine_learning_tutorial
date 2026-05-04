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


### Linear Regression
A supervised learning algorithm used to predict a continuous value bu fitting a straight line (or hyperplane) through the data.<br>
Idea: It finds the best line: y=mx+c<br>
Intution:
- It tries to minimize the difference between predicted and actual values
- This difference is called error
- Uses a method called Gradient Descent to reduce error<br>

Use cases:
- House price prediction
- Sales forecasting<br>

Key point:
Simple, fast but struggles with complex/non-linear data

### Logistic Regression
A supervised learning algorithm used for classification problems (despite the name "regression").<br>
Idea: Instead of predicting numbers, it predicts probability using the Sigmoid Function. 0 <= P(y) <= 1<br>

How it works:
- Output is converted into probability
- If probability > 0.5 --> Class 1, else Class 0<br>

Use cases:
- Spam detection
- Disease prediction<br>

Key point: Works well for binary classification, not ideal for very complex boundaries.