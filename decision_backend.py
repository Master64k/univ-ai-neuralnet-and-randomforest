from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier
import csv

__author__ = "Nícolas Costa - Master64k"
__credits__ = ["Nícolas Costa - Master64k"]
__version__ = "0.1"
__license__ = "WTFPL"
__maintainer__ = "Nícolas Costa"
__email__ = "notyour@business.com"


class DecisionBackend():


    trainning_data = {'data':[],
                      'labels':[]}

    NN = 0
    RF = 1

    trained_rf = False
    trained_nn = False

    neural_net = None
    rnd_forest = None

    def __init__(self):

        self.load_csv()

        self.neural_net = MLPClassifier()

        self.rnd_forest = RandomForestClassifier()

    def load_csv(self):

        try:

            with open('credit_data.csv') as csv_file:

                csv_data = csv.reader(csv_file, delimiter=',', quotechar='"')

                for index, line in enumerate(csv_data):

                    if index == 0: continue # skip the labels

                    else:

                        # TODO: validate each line to make sure the data in in the correct format

                        self.trainning_data['data'].append(line[1: (len(line) - 1)])

                        self.trainning_data['labels'].append(line[(len(line) - 1):])

        except FileNotFoundError :

            raise FileNotFoundError

    def make_prediction(self, algorithm: int, data):

        if algorithm != self.NN and algorithm != self.RF:

            return

        if algorithm == self.NN:

            if not self.trained_nn:

                self.neural_net.fit(self.trainning_data['data'],
                                    self.trainning_data['labels'])

            return self.neural_net.predict(data)

        elif algorithm == self.RF:

            if not self.trained_rf:

                self.rnd_forest.fit(self.trainning_data['data'],
                                    self.trainning_data['labels'])

            return self.rnd_forest.predict(data)