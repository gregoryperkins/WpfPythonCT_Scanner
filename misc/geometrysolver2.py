from base import *

class Geometrysolver2(Base):
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

	def getProfiles(self):
		try:
			return self.getValue(self.objectName, "profiles")
		except ApiError as e:
			print(e)

	def getUserStep(self):
		try:
			return self.getValue(self.objectName, "userStep")
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
	def cmdClear(self):
		try:
			self.executeCommand(self.objectName, "clear")
		except ApiError as e:
			print(e)
	def cmdSetImager(self):
		try:
			self.executeCommand(self.objectName, "setImager")
		except ApiError as e:
			print(e)
	def cmdSetMeasurement(self, x, y, d):
		try:
			parameters = [x, y, d]
			self.executeCommand(self.objectName, "setMeasurement", parameters)
		except ApiError as e:
			print(e)
	def cmdMeasure(self, index):
		try:
			parameters = [index]
			self.executeCommand(self.objectName, "measure", parameters)
		except ApiError as e:
			print(e)
	def cmdDump(self, filename):
		try:
			parameters = [filename]
			self.executeCommand(self.objectName, "dump", parameters)
		except ApiError as e:
			print(e)
	def cmdRestore(self, filename):
		try:
			parameters = [filename]
			self.executeCommand(self.objectName, "restore", parameters)
		except ApiError as e:
			print(e)
	def cmdSolve(self, outerIterations, innerIterations):
		try:
			parameters = [outerIterations, innerIterations]
			self.executeCommand(self.objectName, "solve", parameters)
		except ApiError as e:
			print(e)
	def cmdReplay(self, i):
		try:
			parameters = [i]
			self.executeCommand(self.objectName, "replay", parameters)
		except ApiError as e:
			print(e)
	def cmdSaveGeometry(self):
		try:
			self.executeCommand(self.objectName, "saveGeometry")
		except ApiError as e:
			print(e)
	def cmdLoadGeometry(self):
		try:
			self.executeCommand(self.objectName, "loadGeometry")
		except ApiError as e:
			print(e)
	def cmdCancelOperation(self):
		try:
			self.executeCommand(self.objectName, "cancelOperation")
		except ApiError as e:
			print(e)
	def cmdEnableCentroidCorrection(self):
		try:
			self.executeCommand(self.objectName, "enableCentroidCorrection")
		except ApiError as e:
			print(e)
	def cmdNumberOfMeasurements(self):
		try:
			self.executeCommand(self.objectName, "numberOfMeasurements")
		except ApiError as e:
			print(e)
	def cmdAverageError(self):
		try:
			self.executeCommand(self.objectName, "averageError")
		except ApiError as e:
			print(e)
	def cmdRmsError(self):
		try:
			self.executeCommand(self.objectName, "rmsError")
		except ApiError as e:
			print(e)
	def cmdMaxError(self):
		try:
			self.executeCommand(self.objectName, "maxError")
		except ApiError as e:
			print(e)
	def cmdStartAcquisition(self, first):
		try:
			parameters = [first]
			self.executeCommand(self.objectName, "startAcquisition", parameters)
		except ApiError as e:
			print(e)
	def cmdContinueAcquisition(self):
		try:
			self.executeCommand(self.objectName, "continueAcquisition")
		except ApiError as e:
			print(e)
	def cmdMakeRelative(self, first, count):
		try:
			parameters = [first, count]
			self.executeCommand(self.objectName, "makeRelative", parameters)
		except ApiError as e:
			print(e)
	def cmdRemove(self, first, count):
		try:
			parameters = [first, count]
			self.executeCommand(self.objectName, "remove", parameters)
		except ApiError as e:
			print(e)
	def cmdRestoreProperties(self):
		try:
			self.executeCommand(self.objectName, "restoreProperties")
		except ApiError as e:
			print(e)
	def cmdErrorCSV(self, filename):
		try:
			parameters = [filename]
			self.executeCommand(self.objectName, "errorCSV", parameters)
		except ApiError as e:
			print(e)
	def cmdRemoveBadPoints(self):
		try:
			self.executeCommand(self.objectName, "removeBadPoints")
		except ApiError as e:
			print(e)
	def cmdRenderError(self):
		try:
			self.executeCommand(self.objectName, "renderError")
		except ApiError as e:
			print(e)
	def cmdSetDistortionEnabled(self):
		try:
			self.executeCommand(self.objectName, "setDistortionEnabled")
		except ApiError as e:
			print(e)
	def cmdEnableImagerAlignment(self):
		try:
			self.executeCommand(self.objectName, "enableImagerAlignment")
		except ApiError as e:
			print(e)
	def cmdAssignSpheres(self, numOfSpheres):
		try:
			parameters = [numOfSpheres]
			self.executeCommand(self.objectName, "assignSpheres", parameters)
		except ApiError as e:
			print(e)
	def cmdSetSphere(self, sphereNumber, targetNumber, cal, x, y, z, d):
		try:
			parameters = [sphereNumber, targetNumber, cal, x, y, z, d]
			self.executeCommand(self.objectName, "setSphere", parameters)
		except ApiError as e:
			print(e)
	def cmdSetTargetPosition(self, targetPositionNumber, targetNumber, sample, description, cal):
		try:
			parameters = [targetPositionNumber, targetNumber, sample, description, cal]
			self.executeCommand(self.objectName, "setTargetPosition", parameters)
		except ApiError as e:
			print(e)
	def cmdSetActiveSphere(self, sphereNumber):
		try:
			parameters = [sphereNumber]
			self.executeCommand(self.objectName, "setActiveSphere", parameters)
		except ApiError as e:
			print(e)
	def cmdSetActiveTargetPosition(self, targetPositionNumber):
		try:
			parameters = [targetPositionNumber]
			self.executeCommand(self.objectName, "setActiveTargetPosition", parameters)
		except ApiError as e:
			print(e)
	def cmdSetReferences(self, rotationUpAxis, zAxis, sample):
		try:
			parameters = [rotationUpAxis, zAxis, sample]
			self.executeCommand(self.objectName, "setReferences", parameters)
		except ApiError as e:
			print(e)
	def cmdConvertSimpleMachine(self, filename):
		try:
			parameters = [filename]
			self.executeCommand(self.objectName, "convertSimpleMachine", parameters)
		except ApiError as e:
			print(e)
	def cmdLastCalibrationInfos(self, profile):
		try:
			parameters = [profile]
			self.executeCommand(self.objectName, "lastCalibrationInfos", parameters)
		except ApiError as e:
			print(e)
	def cmdSetLastCalibrationInfos(self, profile, date):
		try:
			parameters = [profile, date]
			self.executeCommand(self.objectName, "setLastCalibrationInfos", parameters)
		except ApiError as e:
			print(e)
	def cmdLoadCalibrationProfile(self, profile):
		try:
			parameters = [profile]
			self.executeCommand(self.objectName, "loadCalibrationProfile", parameters)
		except ApiError as e:
			print(e)
	def cmdInitializeCalibration(self):
		try:
			self.executeCommand(self.objectName, "initializeCalibration")
		except ApiError as e:
			print(e)
	def cmdStartCalibration(self, launchSolver):
		try:
			parameters = [launchSolver]
			self.executeCommand(self.objectName, "startCalibration", parameters)
		except ApiError as e:
			print(e)
	def cmdStartSolver(self):
		try:
			self.executeCommand(self.objectName, "startSolver")
		except ApiError as e:
			print(e)
	def cmdApplyCalibration(self):
		try:
			self.executeCommand(self.objectName, "applyCalibration")
		except ApiError as e:
			print(e)
	def cmdShowCalibrationDialog(self):
		try:
			self.executeCommand(self.objectName, "showCalibrationDialog")
		except ApiError as e:
			print(e)
	def cmdManualStep(self, title, text, source, imager):
		try:
			parameters = [title, text, source, imager]
			self.executeCommand(self.objectName, "manualStep", parameters)
		except ApiError as e:
			print(e)
