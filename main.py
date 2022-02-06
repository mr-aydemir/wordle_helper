from unittest.main import main
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from helpers.word_finder import FinderModel, Suitable, WordFinder
from helpers.Interface import Ui_MainWindow
from functools import partial
import sys

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # required valuables
        self.typedWords:list[str]=[] #typed word list
        self.gridButtons:list[list[QPushButton]]=[] # 5x6 grid buttons
        self.gridButtonsValues:list[list[int]]=[] # 5x6 grid buttons values
        self.colors:list[str]= ["","orange", "green"] # states, colors

        # Click functions connections
        self.type_button.clicked.connect(self.typeWord)
        self.restart_button.clicked.connect(self.restart)
        self.word_list.doubleClicked.connect(self.word_list_item_double_clicked)
        
        # before start
        self.createWordGrid()
        self.showWordHints()

    # double-click list item set current word
    def word_list_item_double_clicked(self, item):
        word:str= self.word_list.currentItem().text()
        self.addWord(word)

    # restart
    def restart(self):
        self.clearGrid()
        self.typedWords.clear()
        self.word_input.clear()
        self.showWordHints()

    # set current word
    def addWord(self, word:str):
        self.word_input.clear()
        if(len(word)!=5 or len(self.typedWords)>= len(self.gridButtons)): return
        self.typedWords.append(word.lower())
        self.setGridButtonTexts(word.upper())
        self.showWordHints()

    # Type button function
    def typeWord(self):
        word:str = self.word_input.text()
        self.addWord(word)

    # creating 5x6 grid buttons, and lists
    def createWordGrid(self):
        for x in range(6):
            self.gridButtons.append([])
            self.gridButtonsValues.append([])
            for y in range(5):
                button = QPushButton("")
                self.wordgrid.addWidget(button, x, y)
                button.clicked.connect(partial(self.wordGridButtonClick,x, y))
                button.setFixedSize(70, 70)
                self.gridButtons[x].append(button)
                self.gridButtonsValues[x].append(0)
                button.setStyleSheet("background-color : "+self.colors[0])
        self.setLayout(self.wordgrid)

    # on grid button click 
    def wordGridButtonClick(self, x:int, y:int, isLeft:bool=True):
        if len(self.typedWords)-1!=x:return
        count=-1
        if not isLeft: 
            count=1
        current = (self.gridButtonsValues[x][y]+count)%len(self.colors)
        self.gridButtonsValues[x][y]=current
        self.gridButtons[x][y].setStyleSheet("background-color : "+self.colors[current])
        self.showWordHints()
    
    # set text of current word buttons
    def setGridButtonTexts(self, word:str):
        for index, char in enumerate(word):
            button = self.gridButtons[len(self.typedWords)-1][index]
            button.setText(char)
            self.gridButtonsValues[len(self.typedWords)-1][index]=1
            button.setStyleSheet("background-color : "+self.colors[1])
    
    # create a finder model for using create hints
    def createFinderModel(self)->FinderModel:
        contains: list[str]=[]
        notContains: list[str]=[]
        suitable: list[Suitable]=[]
        nonSuitable: list[Suitable]=[]
        for idx, word in enumerate(self.typedWords):
            for idj, state in enumerate(self.gridButtonsValues[idx]):
                if state == 1: # Yellow state, contains but not suitable to index
                    nonSuitable.append(Suitable(idj, word[idj]))
                    contains.append(word[idj])
                elif state == 2: # Green state, contains and suitable to index
                    suitable.append(Suitable(idj, word[idj]))
                    contains.append(word[idj])
                else: # Gray state, not Contains
                    notContains.append(word[idj])
        return FinderModel(contains, notContains, suitable, nonSuitable)

    # create hints and show
    def showWordHints(self):
        finderModel = self.createFinderModel()
        hints= WordFinder(finderModel).find()
        self.word_list.clear()
        for hint in hints:
            self.word_list.addItem(hint)
    
    # clear grid
    def clearGrid(self):
        for x in range(6):
            for y in range(5):
                self.gridButtonsValues[x][y]=0
                button = self.gridButtons[x][y]
                button.setStyleSheet("background-color : "+self.colors[0])
                button.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())