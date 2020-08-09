from aux_functions import normalize

class Classifier:
    def __init__(self, features, weights):
        self.features = features
        self.weights = weights

    def update_weights(self, new_weights):
        self.weights = new_weights

    def get_weights(self):
        return self.weights

    def calculate_score(self, string):
        score = 0
        for i in range(len(self.features)-1):
            score = score + (self.features[i](string) * self.weights[i])
        return score

    def is_relevant(self, string):
        normalized_string = normalize (string)
        return (self.calculate_score(normalized_string) > self.weights[len(self.features) - 1])
