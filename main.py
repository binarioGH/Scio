#-*-coding: utf-8-*-
from tkinter import *
from json import loads
from codecs import open as copen
from random import choice
from pyperclip import copy
from winsound import PlaySound, SND_ASYNC, SND_ALIAS
from time import sleep

def sound(file):
	PlaySound(file, SND_ASYNC)


WIDTH = 700
HEIGHT= 400 
BLUE = "#2E2EFE"
GREEN = "#00FF80"
SILVER = "#ECF0F1"
YELLOW = "#F7FE2E"
RED = "#DF013A"

class Worder:
	def __init__(self,root, file="", answares="" ,open_file=True, fnt=("Courier", 15)):
		self.label = Label(root, bg=SILVER, font=fnt, fg="black", justify="left")
		self.answares = answares
		self.file = file
		self.content = 0
		self.root = root
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
	def check_translation(self, entry):
		answare = entry.get()
		if self.content != 0:
			if answare.lower() in self.content[self.label["text"]]:
				sound("source\\correct.wav")
				self.label.config(bg=GREEN)
				self.root.update()
				sleep(0.4)
				self.label.config(bg=SILVER)
				self.newWord()
				entry.delete(0, END)
				return 1
			else:
				sound("source\\wrong.wav")
				self.label.config(bg=RED)
				self.root.update()
				sleep(0.4)
				self.label.config(bg=SILVER)
				#print(":(")
				return 0
		else:
			#print("bruh!")
			return -1

	def newWord(self):
		self.cleanansw()
		current = self.label["text"]
		newword = choice(self.wordlist)
		#print("owo")
		while current == newword:
		    newword = choice(self.wordlist)
		#print("uwu")
		self.label.config(text=newword)		

	def cleanansw(self):
		self.answares.delete(0, END)

	def getansw(self):
		self.cleanansw()
		current = self.label["text"]
		if type(self.content[current]) == type(""):
			self.answares.insert(END, word)
		else:
			for word in self.content[current]:
				self.answares.insert(END, word)


def main():
	root = Tk()
	root.title("Scio")
	root.geometry("{}x{}".format(WIDTH, HEIGHT))
	mainpage = Frame(root, bg=GREEN)
	mainpage.place(relx=0, rely=0, relwidth=1, relheight=1)
	questions = Canvas(mainpage, bg=SILVER)
	questions.place(relx=0.3, rely=0, relwidth=0.8, relheight=1)
	promp = Label(questions, bg=SILVER, font=("Courier", 18))
	promp["text"] = "Translate this: "
	promp.place(relx=0, rely=0.01, relwidth=0.7, relheight=0.4)
	questionborder = Label(questions, bg="black")
	questionborder.place(relx=0, rely=0.3, relwidth=1, relheight=0.052)
	answarebox = Listbox(questions, bg="white", font=("Courier", 14))
	answarebox.place(relx=0.15, rely=0.45, relwidth=0.7, relheight=0.4)
	scrollbar = Scrollbar(answarebox)
	scrollbar.pack(side=RIGHT, fill=Y)
	scrollbar.config(command=answarebox.yview)
	wordquestion = Worder(questions, "source\\esperanto-english.json", answarebox)
	wordquestion.label.place(relx=0, rely=0.3, relwidth=0.99, relheight=0.05)
	console = Canvas(mainpage,bg=GREEN)
	console.place(relx=0, rely=0, relwidth=0.4, relheight=1.1)
	answare = Entry(console, font=("Courier", 16))
	answare.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.05)
	send = Button(console, text="Check!", font=("Courier", 16), command=lambda: wordquestion.check_translation(answare))
	send.place(relx=0.1, rely=0.17, relwidth=0.3, relheight=0.05)
	copytext = Button(console, text="Copy!", font=("Courier", 16), command=lambda: copy(wordquestion.label["text"]))
	copytext.place(relx=0.1, rely=0.24, relwidth=0.3, relheight=0.05)
	newwbutton = Button(console, text="NEW WORD", font=("Courier", 11), command=lambda: wordquestion.newWord())
	newwbutton.place(relx=0.5, rely=0.17, relwidth=0.3, relheight=0.05)
	getans = Button(console, text="ANSWARES", font=("Courier", 11), command=lambda: wordquestion.getansw())
	getans.place(relx=0.5, rely=0.24, relwidth=0.3, relheight=0.05)
	root.mainloop()


if __name__ == '__main__':
	main()