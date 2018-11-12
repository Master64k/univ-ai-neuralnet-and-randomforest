
from PySide import QtCore, QtGui
import sys

from ui.gui import Ui_Dialog

from decision_backend import DecisionBackend

__author__ = "Nícolas Costa - Master64k"
__credits__ = ["Nícolas Costa - Master64k"]
__version__ = "0.1"
__license__ = "WTFPL"
__maintainer__ = "Nícolas Costa"
__email__ = "notyour@business.com"


class FA_Plus(QtGui.QMainWindow):

    main_ui = None

    decision = None

    def __init__(self):

        QtGui.QMainWindow.__init__(self, None)

        try:

            self.decision = DecisionBackend()

        except FileNotFoundError:

            mb = QtGui.QMessageBox()

            mb.setWindowTitle('Erro')
            mb.setText('O arquivo com dados de treinamento do agente inteligente não foi encontrado.')
            mb.setInformativeText('A aplicação será encerrada, certifique-se de ter um arquivo \n'
               'no formato CSV chamado \'credit_data\' na pasta do software\n'
               'contendo os dados de treinamento antes de tentar novamente.')

            mb.setIcon(QtGui.QMessageBox.Critical)

            mb.exec_()

            QtCore.QCoreApplication.exit(0)

            return

        self.main_ui = Ui_Dialog()

        self.main_ui.setupUi(self)

        self.init_controls()

        self.show()

        self.start()

    def init_controls(self):

        self.main_ui.cbAlg.addItems(('Random Forest', 'Neural Network'))

        self.main_ui.btnExit.clicked.connect(lambda : QtCore.QCoreApplication.exit(0))

    def make_prediction(self):

        pass

    def start(self):
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            QtGui.QApplication.instance().exec_()

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)

    ui = FA_Plus()