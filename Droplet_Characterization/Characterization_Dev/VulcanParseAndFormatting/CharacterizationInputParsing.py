# File for formatted argument input to the Characterization program.
# Create instance of the class and access input elements with obj.args["<argument>"]
import argparse
import argcomplete

class CharacterizationInputParsing:
	def __init__(self):
		self.parsing = argparse.ArgumentParser()
		self.parsing.add_argument("-v", "--video", help = "path to the input video")
		self.parsing.add_argument("-o", "--output", default = "csv", help = "output formatting")
		self.parsing.add_argument("-f", "--format", action = "append",  help = "Formatting for the output, use -f for each section. E.g: -f option1 -f option2 -f option3")

		self.args = vars(self.parsing.parse_args())
		argcomplete.autocomplete(self.parsing)

	def getFormat():
		return self.args["format"]
