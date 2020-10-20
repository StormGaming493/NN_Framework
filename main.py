import random
import pprint
from perceptron import *
from layer import Layer
from useful_funcs import iter_2D

def func(arr):
    last = None
    for idx, row in enumerate(arr):
        for val in row if idx%2==0 else reversed(row):
            if last is None:
                last = val
            else:
                if last == val:
                    return False
                else:
                    last = val
    return True

#Define NN
layers = [
    Layer([InPerceptron() for _ in range(16+1)]),
    Layer([MidPerceptron() for _ in range(8)]),
    Layer([MidPerceptron() for _ in range(4)]),
    Layer([OutPerceptron() for _ in range(2)])
    ]
for idx, _ in enumerate(layers):
    if idx == 0:
        continue
    layers[idx-1].link(layers[idx], other_is_later=True)
input_layer = layers[0]
output_layer = layers[-1]

#Train NN
for iteration in range(1000):
    print('iteration #', iteration, sep='')
    map_ = [[random.randint(0,1)*2 - 1 for x in range(4)] for y in range(4)]
    for idx, layer in enumerate(layers):
        if idx == 0:
            for idx2, value in enumerate(iter_2D(map_), 1):
                if idx2 == 1:
                    layer.perceptrons[0].value = 1
                layer.perceptrons[idx2].value = 1 if value == 'x' else -1
        else:
            layer.update()
            
    expected_answer = 1 if func(map_) else 0
    for perceptron in output_layer.perceptrons:
        perceptron.learn(expected_answer)
    #answers = [perceptron.value for perceptron in output_layer.perceptrons]

#Test NN
map1 = [['o', 'o', 'x', 'o'],
        ['o', 'x', 'o', 'x'],
        ['x', 'x', 'x', 'o'],
        ['o', 'x', 'x', 'o']]

map2 = [['x', 'o', 'x', 'o'],
        ['x', 'x', 'o', 'o'],
        ['o', 'x', 'o', 'x'],
        ['o', 'o', 'x', 'x']]

map3 = [['x', 'o', 'x', 'o'],
        ['o', 'x', 'o', 'x'],
        ['x', 'o', 'x', 'o'],
        ['o', 'x', 'o', 'x']]

map4 = [['o', 'x', 'o', 'x'],
        ['x', 'o', 'x', 'o'],
        ['o', 'x', 'o', 'x'],
        ['x', 'o', 'x', 'o']]

map5 = [['x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x']]

map6 = [['o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o'],
        ['o', 'o', 'o', 'o']]

for map_ in [map1, map2, map3, map4, map5, map6]:
##    layers[0].perceptrons[0].value = 1
##    for idx, val in enumerate(iter_2D(map_), 1):
##        layers[0].perceptrons[idx].value = val
    for idx, layer in enumerate(layers):
        if idx == 0:
            for idx2, value in enumerate(iter_2D(map_), 1):
                if idx2 == 1:
                    layer.perceptrons[0].value = 1
                layer.perceptrons[idx2].value = 1 if value == 'x' else 0
        else:
            layer.update()
    answers = [perceptron.value for perceptron in output_layer.perceptrons]
    is_checkered = False
    answer = sum(answers)
    for answer in answers:
        if answer > 0.6:
            is_checkered = True
            break
    pprint.pprint(map_)
    print('This map is', 'checkered.' if is_checkered else 'not checkered.', *answers)
    print('func says: "This map is', 'checkered."' if func(map_) else 'not checkered."')
    print()

##for idx, _ in enumerate(layers, 1):
##    print('layer #', idx, ':', sep='')
##    if idx == len(layers):
##        print(*[a.value for a in layers[-1].perceptrons])
##    else:
##        for perceptron in layers[idx].perceptrons:
##            print(*perceptron.weights)
