from base import *

class Temperatureplot(Base):
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
	def cmdRegisterSensor(self, owner, name):
		try:
			parameters = [owner, name]
			self.executeCommand(self.objectName, "registerSensor", parameters)
		except ApiError as e:
			print(e)
	def cmdStartLog(self, fileName):
		try:
			parameters = [fileName]
			self.executeCommand(self.objectName, "startLog", parameters)
		except ApiError as e:
			print(e)
	def cmdStopLog(self):
		try:
			self.executeCommand(self.objectName, "stopLog")
		except ApiError as e:
			print(e)
	def cmdStartRecordFrameByFrame(self, fileName):
		try:
			parameters = [fileName]
			self.executeCommand(self.objectName, "startRecordFrameByFrame", parameters)
		except ApiError as e:
			print(e)
	def cmdStopRecordFrameByFrame(self):
		try:
			self.executeCommand(self.objectName, "stopRecordFrameByFrame")
		except ApiError as e:
			print(e)
	def cmdRecordFrame(self, image, msrtCurrent, msrtVoltage):
		try:
			parameters = [image, msrtCurrent, msrtVoltage]
			self.executeCommand(self.objectName, "recordFrame", parameters)
		except ApiError as e:
			print(e)
	def cmdUpdateSensor(self, value):
		try:
			parameters = [value]
			self.executeCommand(self.objectName, "updateSensor", parameters)
		except ApiError as e:
			print(e)
