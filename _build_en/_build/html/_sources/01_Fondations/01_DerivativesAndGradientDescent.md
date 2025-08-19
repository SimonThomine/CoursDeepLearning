# Derivatives and Gradient Descent

This course aims to present the gradient descent algorithm, which is one of the pillars of deep learning. For this, it is necessary to review some concepts about derivatives.

## Intuitive Understanding of Derivatives

The derivative of a function at a point represents the slope of the tangent line at that point. It tells us how fast the function is changing at that specific location.

### Mathematical Definition

For a function $f(x)$, the derivative at point $x$ is defined as:

$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

### Geometric Interpretation

- **Positive derivative**: The function is increasing
- **Negative derivative**: The function is decreasing  
- **Zero derivative**: The function has a local extremum (minimum or maximum)

## Gradient Descent Algorithm

Gradient descent is an optimization algorithm used to minimize a function by iteratively moving in the direction of steepest descent.

### Algorithm Steps

1. **Initialize** parameters randomly
2. **Compute** the gradient (derivative) of the cost function
3. **Update** parameters in the opposite direction of the gradient
4. **Repeat** until convergence

### Mathematical Formulation

For a parameter $\theta$ and learning rate $\alpha$:

$$\theta_{new} = \theta_{old} - \alpha \cdot \frac{\partial J}{\partial \theta}$$

Where $J$ is the cost function.

## Applications in Deep Learning

Gradient descent is fundamental in training neural networks:

- **Backpropagation**: Computes gradients efficiently
- **Parameter updates**: Adjusts weights and biases
- **Loss minimization**: Reduces prediction errors

## Next Steps

In the next lesson, we'll explore logistic regression and see how gradient descent applies to classification problems.

---

*This is a foundational concept that will be used throughout the entire course!*