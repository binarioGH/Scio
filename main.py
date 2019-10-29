#-*-coding: utf-8-*-
from tkinter import *
from json import loads

WIDTH = 700
HEIGHT= 600
GREEN = "#2ECC71"
SILVER = "#ECF0F1"

def main():
	root = Tk()
	root.title("Scio")
	root.geometry("{}x{}".format(HEIGHT, WIDTH	))
	mainpage = Frame(root)
	mainpage.place(relx=0, rely=0, relwidth=1, relheight=1)
	console = Canvas(mainpage,bg=GREEN)
	console.place(relx=0, rely=0, relwidth=0.3, relheight=1)
	questions = Canvas(mainpage, bg=SILVER)
	questions.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
	questions.place()
	root.mainloop()


if __name__ == '__main__':
	main()