from base import *

class Visiondetection(Base):
	def __init__(self, objectName):
		super().__init__(objectName)
	def getReady(self):
		try:
			return self.getValue(self.objectName, "ready")
		except ApiError as e:
			print(e)

	def getConfigurable(self):
		try:
			return self.getValue(self.objectName, "configurable")
		except ApiError as e:
			print(e)

	def getConnected(self):
		try:
			return self.getValue(self.objectName, "connected")
		except ApiError as e:
			print(e)

	def setOrigin(self, value):
		try:
			self.setValue(self.objectName, "origin", value)
		except ApiError as e:
			print(e)
	def getOrigin(self):
		try:
			return self.getValue(self.objectName, "origin")
		except ApiError as e:
			print(e)

	def setReadyDelay(self, value):
		try:
			self.setValue(self.objectName, "readyDelay", value)
		except ApiError as e:
			print(e)
	def getReadyDelay(self):
		try:
			return self.getValue(self.objectName, "readyDelay")
		except ApiError as e:
			print(e)

	def getProgress(self):
		try:
			return self.getValue(self.objectName, "progress")
		except ApiError as e:
			print(e)

	def cmdWaitUntilReady(self, timeout, mask):
		try:
			parameters = [timeout, mask]
			self.executeCommand(self.objectName, "waitUntilReady", parameters)
		except ApiError as e:
			print(e)
	def cmdInhibitWarningLogs(self, b):
		try:
			parameters = [b]
			self.executeCommand(self.objectName, "inhibitWarningLogs", parameters)
		except ApiError as e:
			print(e)
	def cmdInhibitInfoLogs(self, b):
		try:
			parameters = [b]
			self.executeCommand(self.objectName, "inhibitInfoLogs", parameters)
		except ApiError as e:
			print(e)
	def cmdWarningLogsInhibited(self):
		try:
			self.executeCommand(self.objectName, "warningLogsInhibited")
		except ApiError as e:
			print(e)
	def cmdInfoLogsInhibited(self):
		try:
			self.executeCommand(self.objectName, "infoLogsInhibited")
		except ApiError as e:
			print(e)
	def cmdReadyDelayTimerSlot(self):
		try:
			self.executeCommand(self.objectName, "readyDelayTimerSlot")
		except ApiError as e:
			print(e)
	def cmdSetEnableLive(self):
		try:
			self.executeCommand(self.objectName, "setEnableLive")
		except ApiError as e:
			print(e)
	def cmdRemoveImageInResults(self, image):
		try:
			parameters = [image]
			self.executeCommand(self.objectName, "removeImageInResults", parameters)
		except ApiError as e:
			print(e)
	def cmdProcess(self, image):
		try:
			parameters = [image]
			self.executeCommand(self.objectName, "process", parameters)
		except ApiError as e:
			print(e)
	def cmdGetEdgeMap(self, inImage, filter):
		try:
			parameters = [inImage, filter]
			self.executeCommand(self.objectName, "getEdgeMap", parameters)
		except ApiError as e:
			print(e)
	def cmdLinesDetection(self, inMap, width, height):
		try:
			parameters = [inMap, width, height]
			self.executeCommand(self.objectName, "linesDetection", parameters)
		except ApiError as e:
			print(e)
	def cmdObjectDetection(self, inMap, width, height):
		try:
			parameters = [inMap, width, height]
			self.executeCommand(self.objectName, "objectDetection", parameters)
		except ApiError as e:
			print(e)
	def cmdImageStdDev(self, inImage):
		try:
			parameters = [inImage]
			self.executeCommand(self.objectName, "imageStdDev", parameters)
		except ApiError as e:
			print(e)
