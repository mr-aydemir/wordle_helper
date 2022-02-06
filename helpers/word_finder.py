from helpers.file_helper import getLines

# This for orange and green state
class Suitable:
    def __init__(self, index: int, char: str) -> None:
        self.index = index
        self.char = char


class FinderModel:
    def __init__(self,
                 contains: list[str],
                 notContains: list[str],
                 suitable: list[Suitable],
                 nonSuitable: list[Suitable]) -> None:
        self.contains = contains
        self.notContains = notContains
        self.suitable = suitable
        self.nonSuitable = nonSuitable


class WordFinder:
    def __init__(self, finderModel: FinderModel) -> None:
        self.finderModel = finderModel
        self.words = getLines("/data/5words_english.txt")
        self.findedWords = self.words
        self.clean()

    # cleaning is important to clean somebugs.
    def clean(self):
        self.finderModel.notContains=list(set(self.finderModel.notContains)-set(self.finderModel.contains))
        self.finderModel.contains = list(set(self.finderModel.contains))
        self.finderModel.suitable = list(set(self.finderModel.suitable))
        self.finderModel.nonSuitable = list(set(self.finderModel.nonSuitable))

    # filter and return words
    def find(self)->list[str]:
        self.findedWords = list(filter(lambda x: all(
            char in x for char in self.finderModel.contains), self.findedWords))
        self.findedWords = list(filter(lambda x: all(
            char not in x for char in self.finderModel.notContains), self.findedWords))
        self.findedWords = list(filter(lambda x: all(x[el.index]==el.char for el in self.finderModel.suitable), self.findedWords))
        self.findedWords = list(filter(lambda x: all(x[el.index]!=el.char for el in self.finderModel.nonSuitable), self.findedWords))
        return self.findedWords


"""finderModel = FinderModel(
contains=["e", "i"],
notContains=["a", "h", "z", "d", "b", "ç", "l"], 
nonSuitable=[Suitable(2, "i"), Suitable(4, "e"), Suitable(0, "e"), Suitable(4, "i"),Suitable(1, "e"),Suitable(3, "i"), Suitable(0, "i")],
suitable=[Suitable(4, "k"), Suitable(3, "e")])
wordFinder = WordFinder(finderModel)
findedWords = wordFinder.find()
print(findedWords)"""
