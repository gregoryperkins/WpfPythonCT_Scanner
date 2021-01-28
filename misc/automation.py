from base import *

class Automation(Base):
	def __init__(self, objectName):
		#super().__init__(objectName)
		Base.__init__(self, objectName)
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

	def setMacroFile(self, value):
		try:
			self.setValue(self.objectName, "macroFile", value)
		except ApiError as e:
			print(e)
	def getMacroFile(self):
		try:
			return self.getValue(self.objectName, "macroFile")
		except ApiError as e:
			print(e)

	def setReconstructionFile(self, value):
		try:
			self.setValue(self.objectName, "reconstructionFile", value)
		except ApiError as e:
			print(e)
	def getReconstructionFile(self):
		try:
			return self.getValue(self.objectName, "reconstructionFile")
		except ApiError as e:
			print(e)

	def setBaseDirectory(self, value):
		try:
			self.setValue(self.objectName, "baseDirectory", value)
		except ApiError as e:
			print(e)
	def getBaseDirectory(self):
		try:
			return self.getValue(self.objectName, "baseDirectory")
		except ApiError as e:
			print(e)

	def setProjectName(self, value):
		try:
			self.setValue(self.objectName, "projectName", value)
		except ApiError as e:
			print(e)
	def getProjectName(self):
		try:
			return self.getValue(self.objectName, "projectName")
		except ApiError as e:
			print(e)

	def setOpenDoor(self, value):
		try:
			self.setValue(self.objectName, "openDoor", value)
		except ApiError as e:
			print(e)
	def getOpenDoor(self):
		try:
			return self.getValue(self.objectName, "openDoor")
		except ApiError as e:
			print(e)

	def setTomoLinkedUniCT(self, value):
		try:
			self.setValue(self.objectName, "tomoLinkedUniCT", value)
		except ApiError as e:
			print(e)
	def getTomoLinkedUniCT(self):
		try:
			return self.getValue(self.objectName, "tomoLinkedUniCT")
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
	def cmdSetUpTomography(self):
		try:
			self.executeCommand(self.objectName, "setUpTomography")
		except ApiError as e:
			print(e)
	def cmdMacroEditorReady(self):
		try:
			self.executeCommand(self.objectName, "macroEditorReady")
		except ApiError as e:
			print(e)
	def cmdXRayReadyOff(self):
		try:
			self.executeCommand(self.objectName, "xRayReadyOff")
		except ApiError as e:
			print(e)
	def cmdStart(self, applyMacroLimits):
		try:
			parameters = [applyMacroLimits]
			self.executeCommand(self.objectName, "start", parameters)
		except ApiError as e:
			print(e)
	def cmdCancel(self):
		try:
			self.executeCommand(self.objectName, "cancel")
		except ApiError as e:
			print(e)
	def cmdSendAcqProject(self):
		try:
			self.executeCommand(self.objectName, "sendAcqProject")
		except ApiError as e:
			print(e)
	def cmdRemoveAcqProject(self):
		try:
			self.executeCommand(self.objectName, "removeAcqProject")
		except ApiError as e:
			print(e)
