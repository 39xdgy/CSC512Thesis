import numpy as np

class NeuronLayers():

    def __init__(self, number_of_neurons, number_of_inputs):
        self.weight = 2 * np.random.random((number_of_inputs, number_of_neurons)) - 1


class NeuralNetwork():

    def __init__(self, layer1, layer2):
        self.layer1 = layer1
        self.layer2 = layer2



    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))




    def __sigmoid_derivative(self, x):
        return x * (1 - x)


    def __step_function(self, x):
        out = 0
        if(x[0] >= 0.5):
            out = 1

        return out


    def think(self, inputs):
        output_from_layer1 = self.__sigmoid(np.dot(inputs, self.layer1.weight))
        output_from_layer2 = self.__sigmoid(np.dot(output_from_layer1, self.layer2.weight))
        integer_out = self.__step_function(output_from_layer2)
        return output_from_layer1, output_from_layer2, integer_out



    
    def train(self, training_set_inputs, training_set_outputs, e_poch):
        for i in range(e_poch):

            output_from_layer1, output_from_layer2, integer_out = self.think(training_set_inputs)

            layer2_error = training_set_outputs - output_from_layer2
            layer2_delta = layer2_error * self.__sigmoid_derivative(output_from_layer2)

            layer1_error = layer2_delta.dot(self.layer2.weight.T)
            layer1_delta = layer1_error * self.__sigmoid_derivative(output_from_layer1)

            layer1_ajustment = training_set_inputs.T.dot(layer1_delta)
            layer2_ajustment = output_from_layer1.T.dot(layer2_delta)

            self.layer1.weight += layer1_ajustment
            self.layer2.weight += layer2_ajustment


    def print_weights(self):
        print("layer 1")
        print(self.layer1.weight)
        print("layer 2")
        print(self.layer2.weight)




if __name__ == "__main__":
    np.random.seed(1)

    layer1 = NeuronLayers(4, 3)
    layer2 = NeuronLayers(1, 4)

    network = NeuralNetwork(layer1, layer2)

    print("The start up weight in the network")
    network.print_weights()

    train_set_inputs = np.array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
    train_set_outputs = np.array([[1, 1, 1, 1, 1, 1, 0]]).T
    
    network.train(train_set_inputs, train_set_outputs, 100)

    print("The weight after the training")
    network.print_weights()

    print("Test to see if the model are good enough by inputing [1, 1, 0]")
    hidden_state, org_out, integer_out = network.think(np.array([1, 1, 0]))
    print(integer_out)
