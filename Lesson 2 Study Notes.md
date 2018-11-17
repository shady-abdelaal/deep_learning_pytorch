# Perceptron Algorithm 

Perceptron algorithm is the introduction to NN, so we just have the inputs, weights and bias. Then they are processed by the activation function (here: it is a normal step function). Which will assign either 1 or 0 depending on the value resulting from the weights & biases:
'W1 x1 + W2 x2 + b =  (+ve)? : 1 else 0 '

That's the idea, so to minimize the error for perceptron algroithm: 
`y' = W1 x1 + W2 x2 +b`
Which means in other words, that each misclassified point would tell the line to come closer.


For gradient descent:
y' = σ(Wx+b)
