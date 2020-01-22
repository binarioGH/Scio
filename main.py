#-*-coding: utf-8-*-
from tkinter import *
from json import loads, dumps
from codecs import open as copen
from random import choice
from pyperclip import copy
from winsound import PlaySound, SND_ASYNC, SND_ALIAS
from time import sleep

def sound(file):
	PlaySound(file, SND_ASYNC)




class WindowConfiguration:
	def __init__(self):
		self.WIDTH = 700
		self.HEIGHT = 400
		self.MAIN_COLOR = "#00FF80"
		self.SECONDARY_COLOR = "#ECF0F1"
		self.WRONG = "#DF013A"
		self.GOOD = "#00FF80"
		self.ADD_WORD = "F7FE2E" 


wc = WindowConfiguration()

def load_colors(content):
	for value in content:
		if value in dir(wc):
			exec("wc.{} = {}".format(value, content[value])) 
class Worder:
	def __init__(self,root, file="", answares="" ,open_file=True, fnt=("Courier", 15)):
		self.label = Label(root, bg=wc.SECONDARY_COLOR, font=fnt, fg="black", justify="left")
		self.answares = answares
		self.file = file
		self.content = 0
		self.root = root
		self.pointc = 0
		self.points = Label(root, bg=wc.SECONDARY_COLOR, font=fnt, fg=wc.WRONG, text="Points: {}".format(self.pointc))
		#self.dictionary = 0
		self.wordlist = []
		if open_file:
			self.load_file()
			if self.content:
				if len(self.wordlist) == 0:
					self.wordlist = list(self.content["Language"])
				self.newWord()
	def load_file(self, file=-1, changing=False, label="", border=""):
		if file == -1:
			file = self.file
		try:
			with copen(file, "r", encoding="utf-8") as f:
				content = loads(f.read())
		except Exception as e: 
			if changing:
				label.config(fg=wc.WRONG)
				sound("source\\wrong.wav")
				if border != "":
					border.config(bg=wc.WRONG)
					self.root.update()
					sleep(0.2)
					border.config(bg="black")
				label["text"] = "The file {} wasn't found.".format(file)
				#print("Works")
			return -1
		else:
			load_colors(content["Colors"])
			self.content = content
			if type(self.content) != type(1):
				self.wordlist = list(self.content["Language"])
			if changing:
				if border != "":
					border.config(bg=wc.GOOD)
					self.root.update()
					sound("source\\correct.wav")
					sleep(0.2)
					border.config(bg="black")
				label.config(fg="black")
				label["text"] = "File {} loaded correctly.".format(file)
				self.newWord()
			

	def update_points(self):
		self.points["text"] = "Points: {}".format(self.pointc)

	def check_translation(self, entry):
		answare = entry.get()
		if self.content != 0:
			if answare.lower() in self.content["Language"][self.label["text"]]:
				sound("source\\correct.wav")
				self.label.config(bg=wc.GOOD)
				self.root.update()
				sleep(0.4)
				self.label.config(bg=wc.SECONDARY_COLOR)
				self.newWord()
				entry.delete(0, END)
				self.pointc += 1
				self.update_points()
			else:
				sound("source\\wrong.wav")
				self.label.config(bg=wc.WRONG)
				self.root.update()
				sleep(0.4)
				self.label.config(bg=wc.SECONDARY_COLOR)
				#print(":(")
				self.pointc -= 1
				self.update_points()
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

	def cleanansw(self, lst=-1):
		if lst == -1 :
			lst = self.answares
		lst.delete(0, END)

	def getansw(self, lst=-1, word=-1, searching=False):
		if lst == -1:
			lst = self.answares
		if word == -1:
			word = self.label["text"]
		word = word.lower()
		word = word.strip()
		if searching:
			if word == self.label["text"]:
				self.pointc -= 2
		self.update_points()
		self.cleanansw(lst)
		current = word
		if type(self.content["Language"][current]) == type(""):
			lst.insert(END, word)
		else:
			for word in self.content["Language"][current]:
				lst.insert(END, "    {}".format(word.title()))
	def addNewAnsware(self, ans, delete=False):
		word = self.label["text"]
		if self.content:
			#print("1")
			if ans != " " and ans != "":
				#print("2")
				if ans in self.content["Language"][word]:
					#print("3")
					if not delete:
						return 0
				ans = ans.lower()
				ans = ans.strip()
				if delete and not ans in self.content["Language"][word]:
					return
				self.label.config(bg=wc.ADD_WORD)
				sound("source\\added.wav")
				self.root.update()
				if delete:
					self.content["Language"][word].remove(ans)
				else:
					self.content["Language"][word].append(ans)
				self.getansw()
				sleep(0.4)
				self.label.config(bg=wc.SECONDARY_COLOR)
				self.root.update()
				with open(self.file, "w", encoding="utf-8") as f:
					f.write(dumps(self.content, indent=4))




def main():
	
	root = Tk()
	root.title("Scio")
	root.geometry("{}x{}".format(wc.WIDTH, wc.HEIGHT))
	change_json = Frame(root, bg=wc.SECONDARY_COLOR)
	change_json.place(relx=0,rely=0,relwidth=1, relheight=1)
	dictionary = Frame(root, bg=wc.SECONDARY_COLOR)
	dictionary.place(relx=0,rely=0,relwidth=1,relheight=1)
	mainpage = Frame(root, bg=wc.MAIN_COLOR)
	mainpage.place(relx=0, rely=0, relwidth=1, relheight=1)
	back = Button(dictionary, text="<-", bg=wc.WRONG, fg="white" ,font=("Courier", 13), command=lambda: mainpage.tkraise())
	back.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)
	questions = Canvas(mainpage, bg=wc.SECONDARY_COLOR)
	questions.place(relx=0.3, rely=0, relwidth=0.8, relheight=1)
	promp = Label(questions, bg=wc.SECONDARY_COLOR, font=("Courier", 18))
	promp["text"] = "Translate this: "
	promp.place(relx=0, rely=0.01, relwidth=0.7, relheight=0.4)
	answarebox = Listbox(questions, bg="white", font=("Courier", 14))
	answarebox.place(relx=0.15, rely=0.45, relwidth=0.7, relheight=0.4)
	scrollbar = Scrollbar(answarebox)
	scrollbar.pack(side=RIGHT, fill=Y)
	scrollbar.config(command=answarebox.yview)
	questionborder = Label(questions, bg="black")
	questionborder.place(relx=0, rely=0.3, relwidth=1, relheight=0.052)
	wordquestion = Worder(questions, "source\\esperanto-english.json", answarebox)
	words = Listbox(dictionary, bg="white", font=("Courier", 18))
	words.place(relx=0.2, rely=0.4, relwidth=0.6, relheight=0.5)
	dicscroll = Scrollbar(words)
	dicscroll.pack(side=RIGHT, fill=Y)
	dicscroll.config(command=words.yview)
	wordsearcher = Entry(dictionary, font=("Courier", 18))
	wordsearcher.place(relx=0.2, rely=0.2, relwidth=0.4, relheight=0.1)
	search = Button(dictionary, bg=wc.MAIN_COLOR, fg="black", text="Search",command=lambda:wordquestion.getansw(words, wordsearcher.get(), True))
	search.place(relx=0.65,rely=0.22, relwidth=0.15, relheight=0.05)
	
	#wordquestion.dictionary = words
	wordquestion.label.place(relx=0, rely=0.3, relwidth=0.99, relheight=0.050)
	wordquestion.points.place(relx=0.3, rely=0.9, relwidth=0.4, relheight=0.08)
	console = Canvas(mainpage,bg=wc.MAIN_COLOR)
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
	newans = Button(console, text="Add Answare", font=("Courier", 18), command=lambda: wordquestion.addNewAnsware(answare.get()))
	newans.place(relx=0.1, rely=0.75, relwidth=0.7, relheight=0.05)
	searchw = Button(console, bg=wc.WRONG, fg="white",text="Search a word", font=("Courier", 14), command=lambda:dictionary.tkraise())
	searchw.place(relx=0.1, rely=0.31, relwidth=0.7, relheight=0.05)
	delans = Button(console, text="Delete Answare", font = ("Courier", 18), command=lambda: wordquestion.addNewAnsware(answare.get(), True))
	delans.place(relx=0.1, rely=0.83, relwidth=0.7, relheight=0.05)
	change_jsonb = Button(questions, text="...", command=lambda:change_json.tkraise())
	change_jsonb.place(relx=0.75, rely=0.9, relwidth=0.1, relheight=0.08)
	jback = Button(change_json, bg=wc.WRONG, fg="white", font=("Courier", 18), text="<-", command=lambda: mainpage.tkraise())
	jback.place(relx=0.05, rely=0.05, relwidth=0.05, relheight=0.05)
	sborder = Label(change_json, bg="black")
	sborder.place(relx=0.24, rely=0.43, relwidth=0.58, relheight=0.14)
	disclaim = Label(change_json, font=("Courier", 14), text="Write the path of the new file:", bg=wc.SECONDARY_COLOR, fg="black", anchor="w")
	disclaim.place(relx=0.24, rely=0.3, relwidth=0.5, relheight=0.1)
	search_file = Entry(change_json, font=("Courier", 18))
	search_file.place(relx=0.25, rely=0.45, relwidth=0.4, relheight=0.1)
	errorLabel = Label(change_json, font=("Courier", 12), bg=wc.SECONDARY_COLOR, fg=wc.WRONG, text="")
	errorLabel.place(relx=0, rely=0.6, relwidth=1, relheight=0.14)	

	ssearch = Button(change_json, font=("Courier", 18), text="Change!", bg=wc.WRONG, fg="white", command=lambda:wordquestion.load_file(search_file.get(), True, errorLabel, sborder))
	ssearch.place(relx=0.65, rely=0.45, relwidth=0.16, relheight=0.1)
	root.mainloop()


if __name__ == '__main__':
	main()