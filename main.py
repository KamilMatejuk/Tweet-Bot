from neuralNetwork import *
from twitter import *

if __name__ == '__main__':
    # filename = getTwitts('#pwr')
    filename = 'FrankensteinData.txt'
    file = open(filename).read()
    processed_inputs = tokenize_words(file)
    # False dla samego wyniku, True dla trenowania nowych wag
    text = generate(processed_inputs, False, 'weightsFrankenstein.hdf5', 100)
    print(text)
    # IDEAS TO DO TO GET BETTER RESULTS
    # increase the number of training epochs
    # use a deeper neural network (add more layers)
    # use a wider neural network (increase number of neurons / memory units)
    # adjust the batch size
    # one hot-encode the inputs
    # padding the input sequences
