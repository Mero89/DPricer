# coding=utf-8
__author__ = 'F.Marouane'

### App Library modules
from DPricer.lib.User import User
from DPricer.data import Excel
from DPricer.lib.YieldManager import YieldManager
### Library modules
import sys
from PyQt4.QtGui import *
from PyQt4 import QtCore
### Import App Screens and Dialogs ###
from DPricer.presentation.PyuicFiles.MDI import Ui_MDIApp
from GisementScreen import GisementScreen, AddAsset, UpdateAsset
from LoginDialog import LoginDialog
from MonPortefeuille import Portefeuilles, GererPortefeuille
from CourbeTauxScreen import CourbeTaux
from ParametresScreen import Parametre
from outils import Calculette


class MyClass(QMainWindow, Ui_MDIApp):
    def __init__(self):
        super(Ui_MDIApp, self).__init__()
        QMainWindow.__init__(self)
        self.ui = Ui_MDIApp()
        self.ui.setupUi(self)
        # log = LoginDialog()
        # log.accepted.connect(self.stats)
        # log.exec_()
        self.user = User('uname', 'password')
        self.user.uid = 1
        # self.user = log.user
        nom = 'FAKIR'
        prenom = 'Marouane'
        self.ui.labelUser.setText(nom + ' ' + prenom)
        cur_day = QtCore.QDate().currentDate().toString()
        self.ui.labelDates.setText(cur_day)
        self.connect_actions()

    def connect_actions(self):
        self.ui.actionMonPortefeuille.triggered.connect(self.open_portefeuille_screen)
        self.ui.actionGererPortefeuille.triggered.connect(self.open_portefeuille_dialog)
        self.ui.actionVisualiser.triggered.connect(self.open_courbe_screen)
        self.ui.actionGisement.triggered.connect(self.open_gisement_screen)
        self.ui.actionAjoutObligation.triggered.connect(self.open_add_asset_screen)
        self.ui.actionOnglets.triggered.connect(self.set_tabview_mode)
        self.ui.actionSousFenetres.triggered.connect(self.set_windowview_mode)
        self.ui.actionExcelCourbe.triggered.connect(self.import_courbe_taux)
        self.ui.actionImporterActifExcel.triggered.connect(self.import_obligations)
        self.ui.actionGeneral.triggered.connect(self.open_parametres)
        self.ui.actionCalculette.triggered.connect(self.open_tools)

    def load_screen(self, screen):
        ct = screen(parent=self)
        if ct.title not in self.title_list():
            self.ui.mdiArea.addSubWindow(ct)
            ct.show()
        else:
            del ct

    # Ouvre la calculette
    def open_tools(self):
        self.load_screen(Calculette)

    # Met à jour la courbe de taux
    def update_courbe(self):
        YM = YieldManager()
        YM.import_auto()

    # Ouvre l'écran des paramètres
    def open_parametres(self):
        self.load_screen(Parametre)

    # Ouvre l'écran d'ajout d'un actif
    @QtCore.pyqtSlot()
    def open_add_asset_screen(self):
        self.load_screen(AddAsset)

    @QtCore.pyqtSlot(dict)
    def update_asset_screen(self, data):
        ct = UpdateAsset(data=data, parent=self)
        if ct.title not in self.title_list():
            self.ui.mdiArea.addSubWindow(ct)
            ct.show()
        else:
            del ct

    # Ouvre l'écran des actifs
    @QtCore.pyqtSlot()
    def open_gisement_screen(self):
        self.load_screen(GisementScreen)

    # Ouvre l'écran de la courbe de taux
    @QtCore.pyqtSlot()
    def open_courbe_screen(self):
        self.load_screen(CourbeTaux)

    # Ouvre le dialogue du portefeuille
    @QtCore.pyqtSlot()
    def open_gerer_portefeuille(self):
        self.load_screen(GererPortefeuille)

    # Ouvre l'écran du portefeuille
    @QtCore.pyqtSlot()
    def open_portefeuille_screen(self):
        pf = Portefeuilles(parent=self)
        if pf.title not in self.title_list():
            self.ui.mdiArea.addSubWindow(pf)
            pf.User = self.user
            pf.show()
            pf.affichePortefeuille()
        else:
            del pf

    def title_list(self):
        """
        retourne la liste des titres des sous-fenêtres
        :return:
        """
        l = [el.windowTitle() for el in self.ui.mdiArea.subWindowList()]
        return l

    def set_windowview_mode(self):
        self.ui.mdiArea.setViewMode(0)

    def set_tabview_mode(self):
        self.ui.mdiArea.setViewMode(1)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_W:
            self.filenew()
            # Comment to commit

    def import_courbe_taux(self):
        filename = self.open_excel()
        # importe Le fichier dans la BDD
        if str(filename):
            rep = Excel.commit_courbe_bam(filename)
            if rep == 1:
                message = u"La courbe a été importée avec succès."
                self.ui.statusbar.showMessage(message, 4000)
            elif rep == 0:
                message = u"La courbe existe déjà."
                self.ui.statusbar.showMessage(message, 4000)
            elif rep == -1:
                message = u"Le fichier ne contient pas les données au format attendu."
                self.ui.statusbar.showMessage(message, 4000)

    def import_obligations(self):
        filename = self.open_excel()
        if str(filename):
            rep = Excel.import_obligation(filename)
            if rep == 1:
                message = u"Le fichier a été importé avec succès."
                self.ui.statusbar.showMessage(message, 4000)
            elif rep == 0:
                message = u"Certains champs sont manquants."
                self.ui.statusbar.showMessage(message, 4000)
            elif rep == -1:
                message = u"Le fichier contient des données incompatibles ou des lignes déjà existantes."
                self.ui.statusbar.showMessage(message, 4000)

    def open_excel(self):
        # lancer le FileDialog
        fDialog = QFileDialog(parent=self)
        fDialog.setFileMode(3)
        filename = fDialog.getOpenFileName(self, "Importer courbe Taux", filter="Fichiers (*.xls *.xlsx)")
        return filename

if __name__ == '__main__':
    ap = QApplication(sys.argv)
    form = MyClass()
    form.show()
    ap.exec_()
