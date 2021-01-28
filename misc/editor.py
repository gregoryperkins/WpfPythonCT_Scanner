from base import *

class Editor(Base):
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

	def setFileNameTemplate(self, value):
		try:
			self.setValue(self.objectName, "fileNameTemplate", value)
		except ApiError as e:
			print(e)
	def getFileNameTemplate(self):
		try:
			return self.getValue(self.objectName, "fileNameTemplate")
		except ApiError as e:
			print(e)

	def setCounter(self, value):
		try:
			self.setValue(self.objectName, "counter", value)
		except ApiError as e:
			print(e)
	def getCounter(self):
		try:
			return self.getValue(self.objectName, "counter")
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
	def cmdStore(self, pointName):
		try:
			parameters = [pointName]
			self.executeCommand(self.objectName, "store", parameters)
		except ApiError as e:
			print(e)
	def cmdRestore(self, index):
		try:
			parameters = [index]
			self.executeCommand(self.objectName, "restore", parameters)
		except ApiError as e:
			print(e)
	def cmdRemove(self, pointName):
		try:
			parameters = [pointName]
			self.executeCommand(self.objectName, "remove", parameters)
		except ApiError as e:
			print(e)
	def cmdRemove(self, index):
		try:
			parameters = [index]
			self.executeCommand(self.objectName, "remove", parameters)
		except ApiError as e:
			print(e)
	def cmdSave(self, filename):
		try:
			parameters = [filename]
			self.executeCommand(self.objectName, "save", parameters)
		except ApiError as e:
			print(e)
	def cmdLoad(self, filename):
		try:
			parameters = [filename]
			self.executeCommand(self.objectName, "load", parameters)
		except ApiError as e:
			print(e)
	def cmdClear(self):
		try:
			self.executeCommand(self.objectName, "clear")
		except ApiError as e:
			print(e)
	def cmdSnapOne(self, index):
		try:
			parameters = [index]
			self.executeCommand(self.objectName, "snapOne", parameters)
		except ApiError as e:
			print(e)
	def cmdSnapAll(self):
		try:
			self.executeCommand(self.objectName, "snapAll")
		except ApiError as e:
			print(e)
	def cmdPause(self):
		try:
			self.executeCommand(self.objectName, "pause")
		except ApiError as e:
			print(e)
	def cmdSetPassFail(self):
		try:
			self.executeCommand(self.objectName, "setPassFail")
		except ApiError as e:
			print(e)
	def cmdSetEnablePassFail(self):
		try:
			self.executeCommand(self.objectName, "setEnablePassFail")
		except ApiError as e:
			print(e)
	def cmdSetOverlayPosition(self, x, y, fontsize):
		try:
			parameters = [x, y, fontsize]
			self.executeCommand(self.objectName, "setOverlayPosition", parameters)
		except ApiError as e:
			print(e)
	def cmdCancel(self):
		try:
			self.executeCommand(self.objectName, "cancel")
		except ApiError as e:
			print(e)
	def cmdShowHardwareNotReadyPopUp(self):
		try:
			self.executeCommand(self.objectName, "showHardwareNotReadyPopUp")
		except ApiError as e:
			print(e)
	def cmdDoorOpen(self):
		try:
			self.executeCommand(self.objectName, "doorOpen")
		except ApiError as e:
			print(e)
	def cmdTubeNotRestarted(self, tubeList):
		try:
			parameters = [tubeList]
			self.executeCommand(self.objectName, "tubeNotRestarted", parameters)
		except ApiError as e:
			print(e)
	def cmdHideHardwareNotReadyPopUp(self):
		try:
			self.executeCommand(self.objectName, "hideHardwareNotReadyPopUp")
		except ApiError as e:
			print(e)
	def cmdHasObject(self, objectName):
		try:
			parameters = [objectName]
			self.executeCommand(self.objectName, "hasObject", parameters)
		except ApiError as e:
			print(e)
	def cmdBeginRestoringProcess(self, index, allowPopUp, applyMacroLimits):
		try:
			parameters = [index, allowPopUp, applyMacroLimits]
			self.executeCommand(self.objectName, "beginRestoringProcess", parameters)
		except ApiError as e:
			print(e)
	def cmdSetMacroProgress(self):
		try:
			self.executeCommand(self.objectName, "setMacroProgress")
		except ApiError as e:
			print(e)
	def cmdRegisterService(self, obj, name, functionName):
		try:
			parameters = [obj, name, functionName]
			self.executeCommand(self.objectName, "registerService", parameters)
		except ApiError as e:
			print(e)
	def cmdSaveConfig(self):
		try:
			self.executeCommand(self.objectName, "saveConfig")
		except ApiError as e:
			print(e)
