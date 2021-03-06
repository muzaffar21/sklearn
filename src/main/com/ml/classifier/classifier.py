__author__ = "Shah Muzaffar"

from sklearn.naive_bayes import MultinomialNB
import pickle


class Train:
    def __init__(self):
        pass

    clf = MultinomialNB()

    def create_model(self, training_matrix, labels, model_path):
        self.clf.fit(training_matrix, labels)
        print "training complete going to save model..."
        pickle.dump(self.clf, open(model_path, 'wb'))
        print "model saved at path + " + model_path


def load(model):
    model = pickle.load(open(model, 'rb'))
    print "model loaded successfully , ready to predict unseen data"
    return model


def predict_label(model, vec):
    l = model.predict(vec)
    return l
