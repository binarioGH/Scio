#-*-coding: utf-8-*-
from json import loads, dumps
from os import listdir
from codecs import open as copen
def change_content(file):
	try:
		with copen(file, "r", encoding="utf-8") as f:
			content = loads(f.read())

	except FileNotFoundError:
		return -1 
	else:
		new_content = {"Colors": {}, "Language": content}
		new_content = dumps(new_content, indent=4)
		with open(file, "w", encoding="utf-8") as f:
			f.write(new_content)


def main():
	for file in listdir():
		if file[-5:] == ".json":
			change_content(file)

if __name__ == '__main__':
	main()