#-*-coding: utf-8-*-
from json import loads, dumps
from os import listdir
from codecs import open as copen


def main():
	for file in listdir():
		if file[-5:].lower() == ".json":
			with copen(file, "r", encoding="utf-8") as f:
				content = loads(f.read())
			print("Configuring {}...".format(file))
			if "Colors" in content:
				content["Colors"]["WIDTH"] = 700
				content["Colors"]["HEIGHT"] = 400
				content["Colors"]["MAIN_COLOR"] = "#00FF80"
				content["Colors"]["SECONDARY_COLOR"] = "#ECF0F1"
				content["Colors"]["WRONG"] = "#DF013A"
				content["Colors"]["GOOD"] = "#00FF80"
				content["Colors"]["ADD_WORD"] = "F7FE2E"
			with copen(file, "w", encoding="utf-8") as f:
				f.write(dumps(content, indent=4))


if __name__ == '__main__':
	main()