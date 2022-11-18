from difflib import SequenceMatcher 

txt1= str(input('enter   a text : '))
txt2= str(input('enter   another  text : '))
sequenc= SequenceMatcher(None, txt1 , txt2 ).ratio()
print(f'Both are {sequenc  * 100 } percent matched :  ')
#close  