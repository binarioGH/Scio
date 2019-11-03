#-*-coding: utf-8-*-
from tkinter import *
from json import loads
from codecs import open as copen
from random import choice
from pyperclip import copy

WIDTH = 700
HEIGHT= 400 
GREEN = "#2ECC71"
SILVER = "#ECF0F1"

class Worder:
	def __init__(self,root, file="", open_file=True, fnt=("Courier", 15)):
		self.label = Label(root, bg=GREEN, font=fnt, fg="black", justify="left")
		self.file = file
		self.content = 0
		if open_file:
			self.load_file()
			if self.content:
				self.wordlist = list(self.content)
				self.newWord()
	def load_file(self):
		try:
			with copen(self.file, "r", encoding="utf-8") as f:
				content = loads(f.read())
		except Exception as e:
			return -1
		else:
			self.content = content
	def check_translation(self,answare):
		if self.content != 0:
			if answare.lower() in self.content[self.label["text"]]:
				self.newWord()
				return 1
			else:
				#print(":(")
				return 0
		else:
			#print("bruh!")
			return -1

	def newWord(self):
		current = self.label["text"]
		newword = choice(self.wordlist)
		#print("owo")
		while current == newword:
		    newword = choice(self.wordlist)
		#print("uwu")
		self.label.config(text=newword)		

def main():
	root = Tk()
	root.title("Scio")
	root.geometry("{}x{}".format(WIDTH, HEIGHT))
	mainpage = Frame(root, bg=GREEN)
	mainpage.place(relx=0, rely=0, relwidth=1, relheight=1)
	questions = Canvas(mainpage, bg=SILVER)
	questions.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
	wordquestion = Worder(questions, "source\\esperanto-english.json")
	wordquestion.label.place(relx=0, rely=0, relwidth=1, relheight=0.05)
	console = Canvas(mainpage,bg=GREEN)
	console.place(relx=0, rely=0, relwidth=0.4, relheight=1.1)
	answare = Entry(console, font=("Courier", 16))
	answare.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.05)
	send = Button(console, text="Check!", font=("Courier", 16), command=lambda: wordquestion.check_translation(answare.get()))
	send.place(relx=0.1, rely=0.17, relwidth=0.3, relheight=0.05)
	copytext = Button(console, text="Copy!", font=("Courier", 16), command=lambda: copy(wordquestion.label["text"]))
	copytext.place(relx=0.1, rely=0.24, relwidth=0.3, relheight=0.05)
	newwbutton = Button(console, text="NEW WORD", font=("Courier", 11), command=lambda: wordquestion.newWord())
	newwbutton.place(relx=0.5, rely=0.17, relwidth=0.3, relheight=0.05)
	root.mainloop()


if __name__ == '__main__':
	main()