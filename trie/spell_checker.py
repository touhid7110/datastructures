#note: pip install nltk
import nltk
from trie_implementation import Trie
nltk.download('gutenberg')
from nltk.corpus import gutenberg

corpora = gutenberg.raw(r'C:\Users\touhi\OneDrive\Documents\python_programs\trie\bane_dialogues.txt')
spell_checker = Trie()
for word in corpora.split():
    word = word.lower()
    spell_checker.insert(word)




def check_spelling(sentence, trie=spell_checker):
    """Method checks the presence in the trie and returns the misspelled words"""
    sentence = sentence.split()
    misspelled_words=[]
    for i ,word in enumerate(sentence):
        if trie.search(word.lower())==False:
            misspelled_words.append((i+1,word))

    return misspelled_words

if __name__=="__main__":
    list_of_misspelled_words=check_spelling("You merly adopted the dark. I was bon in it, molded by it. I didn't see the light untl I was already a man, by then it was nohing to me but blinding!")
    print(list_of_misspelled_words)