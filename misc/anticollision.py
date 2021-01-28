from base import *

class Anticollision(Base):
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
	def cmdMeanVariationCalibrationDone(self):
		try:
			self.executeCommand(self.objectName, "meanVariationCalibrationDone")
		except ApiError as e:
			print(e)
	def cmdSendCurVariation(self):
		try:
			self.executeCommand(self.objectName, "sendCurVariation")
		except ApiError as e:
			print(e)
	def cmdInitializeZonesFinished(self):
		try:
			self.executeCommand(self.objectName, "initializeZonesFinished")
		except ApiError as e:
			print(e)
	def cmdAutCalibrationDone(self):
		try:
			self.executeCommand(self.objectName, "autCalibrationDone")
		except ApiError as e:
			print(e)
	def cmdAutoCalibrationFailed(self):
		try:
			self.executeCommand(self.objectName, "autoCalibrationFailed")
		except ApiError as e:
			print(e)
	def cmdIMaxDebug(self):
		try:
			self.executeCommand(self.objectName, "iMaxDebug")
		except ApiError as e:
			print(e)
	def cmdSelectGeneratorPositionFinished(self):
		try:
			self.executeCommand(self.objectName, "selectGeneratorPositionFinished")
		except ApiError as e:
			print(e)
	def cmdStopAxis(self):
		try:
			self.executeCommand(self.objectName, "stopAxis")
		except ApiError as e:
			print(e)
	def cmdReduceAxisSpeed(self):
		try:
			self.executeCommand(self.objectName, "reduceAxisSpeed")
		except ApiError as e:
			print(e)
	def cmdNormalAxisSpeed(self):
		try:
			self.executeCommand(self.objectName, "normalAxisSpeed")
		except ApiError as e:
			print(e)
	def cmdCameraExpoChanged(self):
		try:
			self.executeCommand(self.objectName, "cameraExpoChanged")
		except ApiError as e:
			print(e)
