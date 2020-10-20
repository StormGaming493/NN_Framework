import random, math

__all__ = ['InPerceptron', 'MidPerceptron', 'OutPerceptron']

def sigmoid(x):
    return 1 / (1 + math.exp(-x)) # 1/(1+e**-x)

def sigmoid_derivative(x):
    return math.exp(-x) / (1 + math.exp(-x))**2 # e**-x / (1 + e**-x)**2

def loss_function(given, expected):
    return (given-expected)**2

class InPerceptron():
    def __init__(self, outputs=None):
        self.outputs = [] if outputs is None else outputs
        self.value = None

    def link(self, output, receiving_input=False, repeat=True):
        assert not receiving_input, 'This is an input perceptron and cannot link to a further input'
        if output not in self.outputs:
            self.outputs.append(output)
            if repeat and self not in output.inputs:
                output.link(self, receiving_input=True, repeat=False)

    def learn(self, value):
        #print(self.value, ':', value)
        return

class MidPerceptron():
    def __init__(self, inputs=None, outputs=None):
        self.inputs = [] if inputs is None else inputs
        self.outputs = [] if outputs is None else outputs
        self.weights = [random.random()*2-1 for _ in self.inputs]
        self.value = None

    def link(self, other, receiving_input, repeat=True):
        if receiving_input:
            if other not in self.inputs:
                self.inputs.append(other)
                self.weights.append(random.random()*2-1)
                if repeat and self not in other.outputs:
                    other.link(self, receiving_input=False, repeat=False)
        else:
            if other not in self.outputs:
                self.outputs.append(other)
                if repeat and self not in other.inputs:
                    other.link(self, receiving_input=True, repeat=False)

    def calculate(self):
        input_value = sum([input_.value * weight for input_, weight in zip(self.inputs, self.weights)])
        self.value = sigmoid(input_value)

    def learn(self, expected_answer, learn_rate=0.3):
        error = self.value - expected_answer
##        for idx, input_ in enumerate(self.inputs):
##            expected = self.weights[idx]*(self.value - expected_answer)*sigmoid_derivative(self.value)
##            self.weights[idx] += input_.value * expected
##            input_.learn(expected)

class OutPerceptron():
    def __init__(self, inputs=None, action=None, threshold=0.6):
        self.inputs = [] if inputs is None else inputs
        self.action = lambda:print(self, 'fires') if action is None else action
        self.weights = [random.random()*2-1 for _ in self.inputs]
        self.threshold = threshold

    def link(self, input_, receiving_input=True, repeat=True):
        assert receiving_input, 'This is an output perceptron and cannot link to a further output'
        if input_ not in self.inputs:
            self.inputs.append(input_)
            self.weights.append(random.random()*2-1)
            if self not in input_.outputs:
                input_.link(self, receiving_input=False)

    def calculate(self):
        input_value = sum([input_.value * weight for input_, weight in zip(self.inputs, self.weights)])
        self.value = sigmoid(input_value)
##        if self.value > self.threshold:
##            self.action()

    def learn(self, expected_answer, learn_rate=0.3):
        error = self.value - expected_answer
        for idx, input_ in enumerate(self.inputs):
            val = learn_rate * error * input_.value
            self.weights[idx] += val
            self.input_
        
##        for idx, input_ in enumerate(self.inputs):
##            expected = 2*(self.value - expected_answer)*sigmoid_derivative(self.value)
##            self.weights[idx] += input_.value * expected
##            input_.learn(expected)
