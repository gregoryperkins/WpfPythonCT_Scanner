from base import *

class Displayzoom(Base):
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

	def getVoxelSize(self):
		try:
			return self.getValue(self.objectName, "voxelSize")
		except ApiError as e:
			print(e)

	def getZoom(self):
		try:
			return self.getValue(self.objectName, "zoom")
		except ApiError as e:
			print(e)

	def getSod(self):
		try:
			return self.getValue(self.objectName, "sod")
		except ApiError as e:
			print(e)

	def getSdd(self):
		try:
			return self.getValue(self.objectName, "sdd")
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
	def cmdAxisPositionChanged(self):
		try:
			self.executeCommand(self.objectName, "axisPositionChanged")
		except ApiError as e:
			print(e)
	def cmdImagerConnected(self):
		try:
			self.executeCommand(self.objectName, "imagerConnected")
		except ApiError as e:
			print(e)
	def cmdGetVoxelSize(self):
		try:
			self.executeCommand(self.objectName, "getVoxelSize")
		except ApiError as e:
			print(e)
	def cmdGetZoom(self):
		try:
			self.executeCommand(self.objectName, "getZoom")
		except ApiError as e:
			print(e)
	def cmdGetSOD(self):
		try:
			self.executeCommand(self.objectName, "getSOD")
		except ApiError as e:
			print(e)
	def cmdGetSDD(self):
		try:
			self.executeCommand(self.objectName, "getSDD")
		except ApiError as e:
			print(e)
