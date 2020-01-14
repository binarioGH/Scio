#-*-coding: utf-8-*-
from json import loads, dumps
from sys import argv
from optparse import OptionParser as opt


def main():
	with open("toki-english.json", "r") as f:
		content = loads(f.read())
	op = opt("Usage: %prog [flags] [values]")
	op.add_option("-w", "--word", dest="word", default="", help="Select the word that you want to modify.")
	op.add_option("-v", "--values", dest="values", default="", help="Select the translations and separate them by commas.")
	op.add_option("-d", "--delete", dest="delete", action="store_true", default=False, help="Delete a word.")
	(o, argv) = op.parse_args()
	if o.word == "":
		print("You didn't define a word.")
		return 0
	else:
		o.word = o.word.lower()

	if o.delete:
		try:
			del content[o.word]
		except KeyError:
			print("{} is not in the dictionary.".format(o.word))
			return 0
	else:
		if o.values != "":
			o.values = o.values.split(",")
		else:
			print("You didn't define values to add.")
			return 0
		if o.word not in content:
			content[o.word] = []
		for value in o.values:
			content[o.word].append(value)

	with open("toki-english.json", "w") as f:
		f.write(dumps(content, indent=4))



if __name__ == '__main__':
	main()