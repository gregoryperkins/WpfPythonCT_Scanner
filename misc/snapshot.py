from base import *

class Snapshot(Base):
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

	def setProjectPath(self, value):
		try:
			self.setValue(self.objectName, "projectPath", value)
		except ApiError as e:
			print(e)
	def getProjectPath(self):
		try:
			return self.getValue(self.objectName, "projectPath")
		except ApiError as e:
			print(e)

	def setFileName(self, value):
		try:
			self.setValue(self.objectName, "fileName", value)
		except ApiError as e:
			print(e)
	def getFileName(self):
		try:
			return self.getValue(self.objectName, "fileName")
		except ApiError as e:
			print(e)

	def setSaveTiff(self, value):
		try:
			self.setValue(self.objectName, "saveTiff", value)
		except ApiError as e:
			print(e)
	def getSaveTiff(self):
		try:
			return self.getValue(self.objectName, "saveTiff")
		except ApiError as e:
			print(e)

	def setSavePng(self, value):
		try:
			self.setValue(self.objectName, "savePng", value)
		except ApiError as e:
			print(e)
	def getSavePng(self):
		try:
			return self.getValue(self.objectName, "savePng")
		except ApiError as e:
			print(e)

	def setSaveJpg(self, value):
		try:
			self.setValue(self.objectName, "saveJpg", value)
		except ApiError as e:
			print(e)
	def getSaveJpg(self):
		try:
			return self.getValue(self.objectName, "saveJpg")
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
	def cmdResetCounter(self):
		try:
			self.executeCommand(self.objectName, "resetCounter")
		except ApiError as e:
			print(e)
	def cmdShowImage(self):
		try:
			self.executeCommand(self.objectName, "showImage")
		except ApiError as e:
			print(e)
	def cmdTakeSnapshot(self):
		try:
			self.executeCommand(self.objectName, "takeSnapshot")
		except ApiError as e:
			print(e)
	def cmdSaveTiff(self):
		try:
			self.executeCommand(self.objectName, "saveTiff")
		except ApiError as e:
			print(e)
	def cmdSetSaveTiff(self, b):
		try:
			parameters = [b]
			self.executeCommand(self.objectName, "setSaveTiff", parameters)
		except ApiError as e:
			print(e)
	def cmdSavePng(self):
		try:
			self.executeCommand(self.objectName, "savePng")
		except ApiError as e:
			print(e)
	def cmdSetSavePng(self, b):
		try:
			parameters = [b]
			self.executeCommand(self.objectName, "setSavePng", parameters)
		except ApiError as e:
			print(e)
	def cmdSaveJpg(self):
		try:
			self.executeCommand(self.objectName, "saveJpg")
		except ApiError as e:
			print(e)
	def cmdSetSaveJpg(self, b):
		try:
			parameters = [b]
			self.executeCommand(self.objectName, "setSaveJpg", parameters)
		except ApiError as e:
			print(e)
	def cmdStartShowImageButton_clicked(self):
		try:
			self.executeCommand(self.objectName, "startShowImageButton_clicked")
		except ApiError as e:
			print(e)
	def cmdCancelShowImageButton_clicked(self):
		try:
			self.executeCommand(self.objectName, "cancelShowImageButton_clicked")
		except ApiError as e:
			print(e)
	def cmdGeneratorNeedsPreheat(self):
		try:
			self.executeCommand(self.objectName, "generatorNeedsPreheat")
		except ApiError as e:
			print(e)
	def cmdStartXrayGeneratorDone(self):
		try:
			self.executeCommand(self.objectName, "startXrayGeneratorDone")
		except ApiError as e:
			print(e)
	def cmdFinishShowImage(self):
		try:
			self.executeCommand(self.objectName, "finishShowImage")
		except ApiError as e:
			print(e)
	def cmdResetCounterButton_clicked(self):
		try:
			self.executeCommand(self.objectName, "resetCounterButton_clicked")
		except ApiError as e:
			print(e)
	def cmdCounterLineEdit_valueChanged(self, value):
		try:
			parameters = [value]
			self.executeCommand(self.objectName, "counterLineEdit_valueChanged", parameters)
		except ApiError as e:
			print(e)
	def cmdCounter(self):
		try:
			self.executeCommand(self.objectName, "counter")
		except ApiError as e:
			print(e)
	def cmdOutputDirectoryLineEdit_textChanged(self, path, valid):
		try:
			parameters = [path, valid]
			self.executeCommand(self.objectName, "outputDirectoryLineEdit_textChanged", parameters)
		except ApiError as e:
			print(e)
	def cmdOutputDir(self):
		try:
			self.executeCommand(self.objectName, "outputDir")
		except ApiError as e:
			print(e)
	def cmdSetOutputDir(self, path):
		try:
			parameters = [path]
			self.executeCommand(self.objectName, "setOutputDir", parameters)
		except ApiError as e:
			print(e)
	def cmdFilenameLineEdit_textChanged(self, filename):
		try:
			parameters = [filename]
			self.executeCommand(self.objectName, "filenameLineEdit_textChanged", parameters)
		except ApiError as e:
			print(e)
	def cmdFileName(self):
		try:
			self.executeCommand(self.objectName, "fileName")
		except ApiError as e:
			print(e)
	def cmdExtensionCheckBox_stateChanged(self, extensions):
		try:
			parameters = [extensions]
			self.executeCommand(self.objectName, "extensionCheckBox_stateChanged", parameters)
		except ApiError as e:
			print(e)
	def cmdImagerComboBox_currentObjectChanged(self, imager):
		try:
			parameters = [imager]
			self.executeCommand(self.objectName, "imagerComboBox_currentObjectChanged", parameters)
		except ApiError as e:
			print(e)
	def cmdSetupImagerAndXrayGenerator(self):
		try:
			self.executeCommand(self.objectName, "setupImagerAndXrayGenerator")
		except ApiError as e:
			print(e)
	def cmdMacroPointCheckBox_stateChanged(self, state):
		try:
			parameters = [state]
			self.executeCommand(self.objectName, "macroPointCheckBox_stateChanged", parameters)
		except ApiError as e:
			print(e)
	def cmdStartTakeSnapshotButton_clicked(self):
		try:
			self.executeCommand(self.objectName, "startTakeSnapshotButton_clicked")
		except ApiError as e:
			print(e)
	def cmdFinishTakeSnapshot(self):
		try:
			self.executeCommand(self.objectName, "finishTakeSnapshot")
		except ApiError as e:
			print(e)
	def cmdRaiseWarning(self, message):
		try:
			parameters = [message]
			self.executeCommand(self.objectName, "raiseWarning", parameters)
		except ApiError as e:
			print(e)
	def cmdRaiseError(self, message):
		try:
			parameters = [message]
			self.executeCommand(self.objectName, "raiseError", parameters)
		except ApiError as e:
			print(e)
	def cmdInterlockChanged(self, state):
		try:
			parameters = [state]
			self.executeCommand(self.objectName, "interlockChanged", parameters)
		except ApiError as e:
			print(e)
	def cmdCheckXrayState(self):
		try:
			self.executeCommand(self.objectName, "checkXrayState")
		except ApiError as e:
			print(e)
	def cmdUpdateProgress(self, value):
		try:
			parameters = [value]
			self.executeCommand(self.objectName, "updateProgress", parameters)
		except ApiError as e:
			print(e)
	def cmdUpdateProgressScaleOffset(self, scale, offset):
		try:
			parameters = [scale, offset]
			self.executeCommand(self.objectName, "updateProgressScaleOffset", parameters)
		except ApiError as e:
			print(e)
