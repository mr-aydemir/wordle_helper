# This is Wordle Solver, 
You can get hints from this application to solve the Wordle word.
Just type a word and select your typed word's letters colors.

# How does it work?
Enter the word that you entered in Wordle
and than select word letters colors.

## lets understand colors means.
Orange state means, the word contains this letter, but not suitable for this index. (index: position of the letter in the word) 
Green state means, word contains this letter, and suitable for this index.
Grey means, word doesn't contains this letter.

Then, Application filters Word List based your choices.

# Setup
pip install pyqt5

# Before use
You can change application for your language.
Just change /data/current_word_list/5words.txt file with your language 5 letters words file.
You can create this file from your languge all words' file using helpers/create_five_words functions.
Or you can find your language 5 letters words file on the internet ocean.

# Run
python main.py



#Screenshot
![image](https://user-images.githubusercontent.com/55704722/152703611-6f081adf-0c29-4efc-b648-103b39ca777c.png)
