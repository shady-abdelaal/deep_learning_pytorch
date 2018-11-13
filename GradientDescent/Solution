# Implement the following functions

# Activation (sigmoid) function
def sigmoid(x):
    return (1/(1+np.exp(-x)))
    

# Output (prediction) formula
def output_formula(features, weights, bias):
    
    return sigmoid(np.dot(features,weights)+bias)
    
    
    

# Error (log-loss) formula
def error_formula(y, output):
    error_value = -y * np.log(output) - (1-y)*np.log(1-output)
    return error_value

# Gradient descent step
def update_weights(x, y, weights, bias, learnrate):
    
    output = output_formula(x,weights,bias)
    d_error = -(y- output)
    weights = weights - learnrate*x*d_error
        
    bias = bias - learnrate*d_error
    return weights,bias
