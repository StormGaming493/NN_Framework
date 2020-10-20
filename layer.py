class Layer():
    def __init__(self, perceptrons):
        self.perceptrons = perceptrons

    def link(self, other_layer, other_is_later):
        for p1 in self.perceptrons:
            for p2 in other_layer.perceptrons:
                p2.link(p1, receiving_input = other_is_later, repeat=False)
                p1.link(p2, receiving_input = not other_is_later, repeat=False)

    def update(self):
        for perceptron in self.perceptrons:
            perceptron.calculate()

    def learn(self, expected_answers):
        for perceptron, expected_answer in zip(self.perceptrons, expected_answers):
            perceptron.learn(expected_answer)



##class MidLayer():
##    pass
##
##class OutLayer():
##    pass
##



##input_ = Layer()
##middle = Layer()
##
##input_.link(middle, other_is_later=True)
