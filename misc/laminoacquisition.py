from base import *

class Laminoacquisition(Base):
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

	def setLaminoMode(self, value):
		try:
			self.setValue(self.objectName, "laminoMode", value)
		except ApiError as e:
			print(e)
	def getLaminoMode(self):
		try:
			return self.getValue(self.objectName, "laminoMode")
		except ApiError as e:
			print(e)

	def setProjectDir(self, value):
		try:
			self.setValue(self.objectName, "projectDir", value)
		except ApiError as e:
			print(e)
	def getProjectDir(self):
		try:
			return self.getValue(self.objectName, "projectDir")
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

	def setType(self, value):
		try:
			self.setValue(self.objectName, "type", value)
		except ApiError as e:
			print(e)
	def getType(self):
		try:
			return self.getValue(self.objectName, "type")
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

	def setSample(self, value):
		try:
			self.setValue(self.objectName, "sample", value)
		except ApiError as e:
			print(e)
	def getSample(self):
		try:
			return self.getValue(self.objectName, "sample")
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

	def setSampleWidth(self, value):
		try:
			self.setValue(self.objectName, "sampleWidth", value)
		except ApiError as e:
			print(e)
	def getSampleWidth(self):
		try:
			return self.getValue(self.objectName, "sampleWidth")
		except ApiError as e:
			print(e)

	def setSampleHeight(self, value):
		try:
			self.setValue(self.objectName, "sampleHeight", value)
		except ApiError as e:
			print(e)
	def getSampleHeight(self):
		try:
			return self.getValue(self.objectName, "sampleHeight")
		except ApiError as e:
			print(e)

	def setSampleThickness(self, value):
		try:
			self.setValue(self.objectName, "sampleThickness", value)
		except ApiError as e:
			print(e)
	def getSampleThickness(self):
		try:
			return self.getValue(self.objectName, "sampleThickness")
		except ApiError as e:
			print(e)

	def setSampleOffsetX(self, value):
		try:
			self.setValue(self.objectName, "sampleOffsetX", value)
		except ApiError as e:
			print(e)
	def getSampleOffsetX(self):
		try:
			return self.getValue(self.objectName, "sampleOffsetX")
		except ApiError as e:
			print(e)

	def setSampleOffsetY(self, value):
		try:
			self.setValue(self.objectName, "sampleOffsetY", value)
		except ApiError as e:
			print(e)
	def getSampleOffsetY(self):
		try:
			return self.getValue(self.objectName, "sampleOffsetY")
		except ApiError as e:
			print(e)

	def setSampleOffsetZ(self, value):
		try:
			self.setValue(self.objectName, "sampleOffsetZ", value)
		except ApiError as e:
			print(e)
	def getSampleOffsetZ(self):
		try:
			return self.getValue(self.objectName, "sampleOffsetZ")
		except ApiError as e:
			print(e)

	def setSwitchOffXrays(self, value):
		try:
			self.setValue(self.objectName, "switchOffXrays", value)
		except ApiError as e:
			print(e)
	def getSwitchOffXrays(self):
		try:
			return self.getValue(self.objectName, "switchOffXrays")
		except ApiError as e:
			print(e)

	def setSleepTime(self, value):
		try:
			self.setValue(self.objectName, "sleepTime", value)
		except ApiError as e:
			print(e)
	def getSleepTime(self):
		try:
			return self.getValue(self.objectName, "sleepTime")
		except ApiError as e:
			print(e)

	def setOverwrite(self, value):
		try:
			self.setValue(self.objectName, "overwrite", value)
		except ApiError as e:
			print(e)
	def getOverwrite(self):
		try:
			return self.getValue(self.objectName, "overwrite")
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
	def cmdStart(self):
		try:
			self.executeCommand(self.objectName, "start")
		except ApiError as e:
			print(e)
	def cmdStartFromMacroPoint(self):
		try:
			self.executeCommand(self.objectName, "startFromMacroPoint")
		except ApiError as e:
			print(e)
	def cmdCancel(self):
		try:
			self.executeCommand(self.objectName, "cancel")
		except ApiError as e:
			print(e)
	def cmdSetAccelerationLimit(self):
		try:
			self.executeCommand(self.objectName, "setAccelerationLimit")
		except ApiError as e:
			print(e)
	def cmdGuiDestroyed(self):
		try:
			self.executeCommand(self.objectName, "guiDestroyed")
		except ApiError as e:
			print(e)
	def cmdFinishedPrivate(self):
		try:
			self.executeCommand(self.objectName, "finishedPrivate")
		except ApiError as e:
			print(e)
