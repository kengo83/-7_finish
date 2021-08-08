from googletrans import Translator
import eel
# translator = Translator()
# print(translator.translate('I like animal', dest='ja'))

def translate(en_content:str,src,dest):
    translator = Translator()
    a = translator.translate(en_content, src=src,dest=dest)
    print(a.text)
    eel.view_result_js(a.text)


