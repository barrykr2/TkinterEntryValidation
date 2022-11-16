import string, sys

class string_format:
    def __init__(self):
        pass
    
    
    def title(self, text):
        returnText = ''
        
        for x in range(len(text)):
            if x == 0:
                returnText = str(text[x]).upper()
            elif str(text[x - 1]) == ' ':
                returnText += str(text[x]).upper()
            else:
                returnText += str(text[x])
                
        return returnText    

    def sentence(self, text):
        returnText = ''
        
        for x in range(len(text)):
            if x == 0:
                returnText = str(text[x]).upper()
            elif x > 3 and (str(text[x - 2:x]) == '. ' or str(text[x - 3:x]) == '.  '):
                returnText += str(text[x]).upper()
            else:
                returnText += str(text[x])
                
        return returnText    

    def camelCase(self, text):
        returnText = ''
        
        for x in range(len(text)):
            if x == 0:
                returnText = str(text[x]).upper()
            elif str(text[x - 1]) == ' ':
                returnText += str(text[x]).upper()
            elif str(text[x]).isalnum():
                returnText += str(text[x])
                
        return returnText    

    def snake(self, text):
        returnText = text.replace(' ', '_').replace("'", '_').replace('.', '').replace(',', '').lower()
        
        return returnText    

if __name__ == "__main__":
    myFormat = string_format()
    print(myFormat.title("they're over at bill's house. and, BTW, we are not going. okay?"))    
    print(myFormat.sentence("they're over at bill's house. and, BTW, we are not going. okay?"))    
    print(myFormat.camelCase("they're over at bill's house. and, BTW, we are not going. okay?"))    
    print(myFormat.snake("they're over at bill's house. and, BTW, we are not going. okay?"))    
    print(myFormat.sentence("This group is dedicated to Python Developers & Programmers which discusses all aspects of the server.  python is great."))
    