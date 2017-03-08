import csv

class CharacterizationOutputFormatting:
	def __init__(self):
		self.formatting = ""
		self.data = ""
		self.outputPath = ""
		self.dataToFormat = []	
	def setFormat(inputFormat):
		self.formatting = inputFormat

	def setOutputPath(inputPath):
		self.outputPath = inputPath

	def setData(inputData):
		self.data = inputData

	def checkOutputRequirements():
		valid = True
	
		if not self.data:
			print "Error: No Data to format\n"
			valid = False
		
		if not self.formatting:
			print "Error: No Format specified\n"
			valid = False
		
		if not self.outputPath:
			print "Error: No Output Path specified\n"
			valid = False
		
		return valid

#	def addData(singleDataArray):
#		dataToFormat = singleDataArray

	def doFormattingAndWriting():
		if self.checkOutputRequirements() is False:
			return False

		if self.formatting == "csv"
			try:
				self.outputCSV(self.data, self.outputPath)

			except:
				print ":("

	def outputCSV(data, path):
		open(path, 'w', newline='') as fileDescriptor:
			csv.writer(fileDescriptor, delimiter=",").writerows(data)
		
