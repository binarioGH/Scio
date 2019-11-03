#-*-coding: utf-8-*-
from tkinter import *
from json import loads
from codecs import open as copen
from random import choice

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
	def check_translation(self, word, answare):
		if self.content:
			if answare in self.content[word]:
				return 1
			return 0
		return -1

	def newWord(self):
		current = self.label["text"]
		newword = choice(self.wordlist)
		while current == newword:
		    newword = choice(self.wordlist)
		self.label["text"] = newword		

def main():
	root = Tk()
	root.title("Scio")
	root.geometry("{}x{}".format(WIDTH, HEIGHT))
	mainpage = Frame(root, bg=GREEN)
	mainpage.place(relx=0, rely=0, relwidth=1, relheight=1)
	console = Canvas(mainpage,bg=GREEN)
	console.place(relx=0, rely=0, relwidth=0.3, relheight=1.1)
	questions = Canvas(mainpage, bg=SILVER)
	questions.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
	wordquestion = Worder(questions, "source\\esperanto-english.json")
	wordquestion.label.place(relx=0, rely=0, relwidth=1, relheight=0.05)
	root.mainloop()


if __name__ == '__main__':
	main()