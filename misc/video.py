from base import *

class Video(Base):
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

	def setImager(self, value):
		try:
			self.setValue(self.objectName, "imager", value)
		except ApiError as e:
			print(e)
	def getImager(self):
		try:
			return self.getValue(self.objectName, "imager")
		except ApiError as e:
			print(e)

	def setNumberOfImages(self, value):
		try:
			self.setValue(self.objectName, "numberOfImages", value)
		except ApiError as e:
			print(e)
	def getNumberOfImages(self):
		try:
			return self.getValue(self.objectName, "numberOfImages")
		except ApiError as e:
			print(e)

	def setPrefix(self, value):
		try:
			self.setValue(self.objectName, "prefix", value)
		except ApiError as e:
			print(e)
	def getPrefix(self):
		try:
			return self.getValue(self.objectName, "prefix")
		except ApiError as e:
			print(e)

	def setPath(self, value):
		try:
			self.setValue(self.objectName, "path", value)
		except ApiError as e:
			print(e)
	def getPath(self):
		try:
			return self.getValue(self.objectName, "path")
		except ApiError as e:
			print(e)

	def setFormat(self, value):
		try:
			self.setValue(self.objectName, "format", value)
		except ApiError as e:
			print(e)
	def getFormat(self):
		try:
			return self.getValue(self.objectName, "format")
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
	def cmdSetImager(self):
		try:
			self.executeCommand(self.objectName, "setImager")
		except ApiError as e:
			print(e)
	def cmdSetImagerIndex(self):
		try:
			self.executeCommand(self.objectName, "setImagerIndex")
		except ApiError as e:
			print(e)
	def cmdSetNumberOfImages(self):
		try:
			self.executeCommand(self.objectName, "setNumberOfImages")
		except ApiError as e:
			print(e)
	def cmdSetPrefix(self):
		try:
			self.executeCommand(self.objectName, "setPrefix")
		except ApiError as e:
			print(e)
	def cmdSetPath(self):
		try:
			self.executeCommand(self.objectName, "setPath")
		except ApiError as e:
			print(e)
	def cmdSetFormat(self):
		try:
			self.executeCommand(self.objectName, "setFormat")
		except ApiError as e:
			print(e)
	def cmdStart(self):
		try:
			self.executeCommand(self.objectName, "start")
		except ApiError as e:
			print(e)
	def cmdCancel(self):
		try:
			self.executeCommand(self.objectName, "cancel")
		except ApiError as e:
			print(e)
	def cmdFinishedPrivate(self):
		try:
			self.executeCommand(self.objectName, "finishedPrivate")
		except ApiError as e:
			print(e)
