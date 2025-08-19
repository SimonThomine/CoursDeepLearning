# Logistic Regression

Logistic regression is a fundamental algorithm for binary classification problems. It's an excellent introduction to the concepts used in neural networks.

## From Linear to Logistic Regression

### Linear Regression Limitations

Linear regression predicts continuous values, but for classification we need:
- Outputs between 0 and 1 (probabilities)
- A decision boundary
- Non-linear relationships

### The Sigmoid Function

The sigmoid function transforms any real number into a value between 0 and 1:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

Where $z = w_0 + w_1x_1 + w_2x_2 + ... + w_nx_n$

## Logistic Regression Model

### Prediction Formula

$$h_\theta(x) = \sigma(\theta^T x) = \frac{1}{1 + e^{-\theta^T x}}$$

### Decision Rule

- If $h_\theta(x) \geq 0.5$: Predict class 1
- If $h_\theta(x) < 0.5$: Predict class 0

## Cost Function

### Why Not Mean Squared Error?

MSE with sigmoid creates a non-convex function with local minima.

### Log-Likelihood Cost

The logistic regression cost function is:

$$J(\theta) = -\frac{1}{m} \sum_{i=1}^{m} [y^{(i)} \log(h_\theta(x^{(i)})) + (1-y^{(i)}) \log(1-h_\theta(x^{(i)}))]$$

This creates a convex function suitable for gradient descent.

## Gradient Descent for Logistic Regression

### Gradient Computation

The gradient of the cost function is:

$$\frac{\partial J}{\partial \theta_j} = \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) x_j^{(i)}$$

### Update Rule

$$\theta_j := \theta_j - \alpha \frac{\partial J}{\partial \theta_j}$$

## Connection to Neural Networks

Logistic regression is essentially:
- A single neuron
- With sigmoid activation
- Trained with gradient descent

This forms the building block for more complex neural networks!

## Next Steps

In the next section, we'll build our first neural network by combining multiple logistic regression units.

---

*Understanding logistic regression is crucial for grasping how neural networks learn!*