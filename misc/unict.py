from base import *

class Unict(Base):
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
	def cmdCurrentImageArrayChanged(self):
		try:
			self.executeCommand(self.objectName, "currentImageArrayChanged")
		except ApiError as e:
			print(e)
	def cmdAcquisitionStarted(self, name):
		try:
			parameters = [name]
			self.executeCommand(self.objectName, "acquisitionStarted", parameters)
		except ApiError as e:
			print(e)
	def cmdOpenProject(self, name, projArray, doc):
		try:
			parameters = [name, projArray, doc]
			self.executeCommand(self.objectName, "openProject", parameters)
		except ApiError as e:
			print(e)
	def cmdCloseProject(self, name):
		try:
			parameters = [name]
			self.executeCommand(self.objectName, "closeProject", parameters)
		except ApiError as e:
			print(e)
	def cmdOpenProjectPrivate(self, projArray, doc, projectPath):
		try:
			parameters = [projArray, doc, projectPath]
			self.executeCommand(self.objectName, "openProjectPrivate", parameters)
		except ApiError as e:
			print(e)
	def cmdLaunchConeBeamProject(self, inXmlFileName):
		try:
			parameters = [inXmlFileName]
			self.executeCommand(self.objectName, "launchConeBeamProject", parameters)
		except ApiError as e:
			print(e)
	def cmdLaunchConeBeamProject(self, projArray, doc, projectPath):
		try:
			parameters = [projArray, doc, projectPath]
			self.executeCommand(self.objectName, "launchConeBeamProject", parameters)
		except ApiError as e:
			print(e)
	def cmdLaunchFanBeamProject(self, inXmlFileName):
		try:
			parameters = [inXmlFileName]
			self.executeCommand(self.objectName, "launchFanBeamProject", parameters)
		except ApiError as e:
			print(e)
	def cmdCloseCurrentProject(self, askForSave):
		try:
			parameters = [askForSave]
			self.executeCommand(self.objectName, "closeCurrentProject", parameters)
		except ApiError as e:
			print(e)
	def cmdLoadingCanceled(self):
		try:
			self.executeCommand(self.objectName, "loadingCanceled")
		except ApiError as e:
			print(e)
	def cmdSetTolAutoGeometryCorrection(self, tol):
		try:
			parameters = [tol]
			self.executeCommand(self.objectName, "setTolAutoGeometryCorrection", parameters)
		except ApiError as e:
			print(e)
	def cmdSetFinishPressisionAutoGeometryCorrection(self, press):
		try:
			parameters = [press]
			self.executeCommand(self.objectName, "setFinishPressisionAutoGeometryCorrection", parameters)
		except ApiError as e:
			print(e)
	def cmdSetNbPassAutoGeometryCorrection(self, passs):
		try:
			parameters = [passs]
			self.executeCommand(self.objectName, "setNbPassAutoGeometryCorrection", parameters)
		except ApiError as e:
			print(e)
	def cmdSetStackStepAutoGeometryCorrection(self, passs):
		try:
			parameters = [passs]
			self.executeCommand(self.objectName, "setStackStepAutoGeometryCorrection", parameters)
		except ApiError as e:
			print(e)
	def cmdGetTolAutoGeometryCorrection(self):
		try:
			self.executeCommand(self.objectName, "getTolAutoGeometryCorrection")
		except ApiError as e:
			print(e)
	def cmdGetFinishPressisionAutoGeometryCorrection(self):
		try:
			self.executeCommand(self.objectName, "getFinishPressisionAutoGeometryCorrection")
		except ApiError as e:
			print(e)
	def cmdGetNbPassAutoGeometryCorrection(self):
		try:
			self.executeCommand(self.objectName, "getNbPassAutoGeometryCorrection")
		except ApiError as e:
			print(e)
	def cmdGetStackStepAutoGeometryCorrection(self):
		try:
			self.executeCommand(self.objectName, "getStackStepAutoGeometryCorrection")
		except ApiError as e:
			print(e)
	def cmdProjectProcessFinished(self):
		try:
			self.executeCommand(self.objectName, "projectProcessFinished")
		except ApiError as e:
			print(e)
	def cmdSilentMode(self):
		try:
			self.executeCommand(self.objectName, "silentMode")
		except ApiError as e:
			print(e)
	def cmdSetSilentMode(self, silent):
		try:
			parameters = [silent]
			self.executeCommand(self.objectName, "setSilentMode", parameters)
		except ApiError as e:
			print(e)
	def cmdLoadFirstQueuedProject(self):
		try:
			self.executeCommand(self.objectName, "loadFirstQueuedProject")
		except ApiError as e:
			print(e)
	def cmdGetQueuedProjects(self):
		try:
			self.executeCommand(self.objectName, "getQueuedProjects")
		except ApiError as e:
			print(e)
	def cmdStartBeamProfileSelection(self, dir):
		try:
			parameters = [dir]
			self.executeCommand(self.objectName, "startBeamProfileSelection", parameters)
		except ApiError as e:
			print(e)
	def cmdSelectBeamProfileFromName(self, name):
		try:
			parameters = [name]
			self.executeCommand(self.objectName, "selectBeamProfileFromName", parameters)
		except ApiError as e:
			print(e)
	def cmdStartReconstruction(self):
		try:
			self.executeCommand(self.objectName, "startReconstruction")
		except ApiError as e:
			print(e)
	def cmdStartScatterCorrection(self, bottomLimit):
		try:
			parameters = [bottomLimit]
			self.executeCommand(self.objectName, "startScatterCorrection", parameters)
		except ApiError as e:
			print(e)
	def cmdStartGeometryCorrection(self):
		try:
			self.executeCommand(self.objectName, "startGeometryCorrection")
		except ApiError as e:
			print(e)
	def cmdActivateAutomation(self, activate):
		try:
			parameters = [activate]
			self.executeCommand(self.objectName, "activateAutomation", parameters)
		except ApiError as e:
			print(e)
	def cmdActivateAutomaticGeometry(self, activate):
		try:
			parameters = [activate]
			self.executeCommand(self.objectName, "activateAutomaticGeometry", parameters)
		except ApiError as e:
			print(e)
	def cmdActivateAutomaticScatter(self, activate):
		try:
			parameters = [activate]
			self.executeCommand(self.objectName, "activateAutomaticScatter", parameters)
		except ApiError as e:
			print(e)
	def cmdSaveSettings(self, doc):
		try:
			parameters = [doc]
			self.executeCommand(self.objectName, "saveSettings", parameters)
		except ApiError as e:
			print(e)
	def cmdCancel(self):
		try:
			self.executeCommand(self.objectName, "cancel")
		except ApiError as e:
			print(e)
