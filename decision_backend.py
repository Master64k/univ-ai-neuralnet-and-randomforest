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

    RF = 0
    NN = 1


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

                    if index == 0 or self.validate_training_data(line) == False:

                        continue # skip the labels

                    else:

                        # is necessary to replace commas with periods for correct type conversion

                        line = self.format_float_data(line)

                        attributes = line[1: (len(line) - 1)]

                        labels = int(line[(len(line) - 1):][0])

                        self.trainning_data['data'].append(attributes)

                        self.trainning_data['labels'].append(labels)

        except FileNotFoundError :

            raise FileNotFoundError

    def make_prediction(self, algorithm: int, data):

        if algorithm != self.NN and algorithm != self.RF:

            return

        if algorithm == self.NN:

            if not self.trained_nn:

                self.neural_net.fit(self.trainning_data['data'],
                                    self.trainning_data['labels'])

                self.trained_nn = True

            return self.neural_net.predict(data)[0]

        elif algorithm == self.RF:

            if not self.trained_rf:

                self.rnd_forest.fit(self.trainning_data['data'],
                                    self.trainning_data['labels'])

                self.trained_rf = True

            return self.rnd_forest.predict(data)[0]


    def format_float_data(self, line: list) -> list:

        new_list = []

        for i in line:

            new_list.append(float(i.replace(',', '.')))

        return new_list

    def validate_training_data(self, line: list):

        if len(line) < 5:

            return False

        for i in line:

            if i == '': return False

            else:

                i = i.replace(',','.')

                if float(i) < 0:

                    return False

