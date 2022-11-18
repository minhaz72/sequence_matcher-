from difflib import SequenceMatcher 
def sequence_matcher(txt1: str , txt2 : str) : 
    secqunce= SequenceMatcher(None, txt1 , txt2 ).ratio()
    print(f'Both are {secqunce * 100} percent similar ')

txt1=str(input('enter a text : '))
txt2= str(input('enter another text : '))
sequence_matcher(txt1 , txt2)
