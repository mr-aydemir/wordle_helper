from helpers.file_helper import getLines, writeList

def getFiveWords(list:list[str])->list[str]:
    return [line for line in list if len(line)==5]
# this function helps to create a 5-letter word file from the word file you specify.
# I used this function to create my native language 5 words file.
def createFiveWordsFile(allwords_path:str, output_path:str):
    lines = getLines(allwords_path)
    fiveWords = getFiveWords(lines)
    writeList(output_path,fiveWords)



""" 
all_words_txt_path= "Birleştirilmiş_Sözlük_Kelime_Listesi.txt"
output_path = "5words_turkish.txt" """