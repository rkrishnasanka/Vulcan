class CharacterizationOutputFormatting:
	def __init__(self):
		self.formatting = ""
		self.data = ""
		self.outputPath = ""
	
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

	def doFormatting():
		if self.checkOutputRequirements() is False:
			return False

		
