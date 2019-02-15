#Answer to Text Editor - https://py.checkio.org/en/mission/text-editor/

class Text:
    value = ""
    font = ""
    def write(self,text):
        self.value+=text
    def show(self):
        return self.font+self.value+self.font
    def set_font(self,font):
        self.font = '['+font+']'
    def restore(self,text):
        if '['+self.font+']' not in text:
            self.font = ""
        elif '[' in text and ']' in text:
            text1 = text.split(']')
            self.set_font(text1[0].split('[')[1])
            text = text1[1].split('[')[0]
        self.value = text
            

class SavedText:
    s_text = []
    def __init__(self):
        self.s_text = []
    def save_text(self,text):
        content = text.font+text.value+text.font
        length = len(self.s_text)
        if length == 10:
            for i in range(9):
                self.s_text[i] = self.s_text[i+1]
            self.s_text[9] = content
        else:
            self.s_text.append(content)
    def get_version(self,value):
        return self.s_text[value]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    text_2 = Text()
    saver_2 = SavedText()
    text_2.write("Tomorrow at 7:15 PM.")
    saver_2.save_text(text_2)
    text_2.set_font("ComicSans")
    text_2.write(" Sorry. 7:15 AM.")
    saver_2.save_text(text_2)
    text_2.write(" Near the stadium.")
    text_2.restore(saver_2.get_version(1))
    print(text_2.show())

    print("Coding complete? Let's try tests!")