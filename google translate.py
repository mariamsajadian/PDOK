from googletrans import Translator
import nltk
from google_trans_new import google_translator
from OpenDutchWordnet import Wn_grid_parser
from nltk import word_tokenize, pos_tag


with open("question.txt") as English:
    question = English.read()
translator = google_translator()
translate_text = translator.translate(question,lang_tgt='nl')
print(translate_text)
# nounsDutch = [token for token, pos in pos_tag(word_tokenize(question)) if pos.startswith('N')]
tokenizationEng = words = nltk.word_tokenize(translate_text)
print(tokenizationEng)



