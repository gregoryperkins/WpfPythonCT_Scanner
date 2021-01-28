from base import *

class Geometrysolver(Base):
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

	def getLastCalibrationDate(self):
		try:
			return self.getValue(self.objectName, "lastCalibrationDate")
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
	def cmdSetSample(self, reference, calibrate, axisOrigins, axisDirections):
		try:
			parameters = [reference, calibrate, axisOrigins, axisDirections]
			self.executeCommand(self.objectName, "setSample", parameters)
		except ApiError as e:
			print(e)
	def cmdSetImager(self, reference, calibrate, calibrateOrientation, axisOrigins, axisDirections):
		try:
			parameters = [reference, calibrate, calibrateOrientation, axisOrigins, axisDirections]
			self.executeCommand(self.objectName, "setImager", parameters)
		except ApiError as e:
			print(e)
	def cmdSetSource(self, reference, calibrate, axisOrigins, axisDirections):
		try:
			parameters = [reference, calibrate, axisOrigins, axisDirections]
			self.executeCommand(self.objectName, "setSource", parameters)
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
	def cmdCancel(self):
		try:
			self.executeCommand(self.objectName, "cancel")
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
	def cmdMaxError(self):
		try:
			self.executeCommand(self.objectName, "maxError")
		except ApiError as e:
			print(e)
	def cmdSetActiveSphere(self):
		try:
			self.executeCommand(self.objectName, "setActiveSphere")
		except ApiError as e:
			print(e)
	def cmdSetSphereDiameter(self):
		try:
			self.executeCommand(self.objectName, "setSphereDiameter")
		except ApiError as e:
			print(e)
	def cmdStartAcquisition(self):
		try:
			self.executeCommand(self.objectName, "startAcquisition")
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
	def cmdCorrectXrayPosition(self, measuredValue, realValue):
		try:
			parameters = [measuredValue, realValue]
			self.executeCommand(self.objectName, "correctXrayPosition", parameters)
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
	def cmdShowCalibrationDialog(self):
		try:
			self.executeCommand(self.objectName, "showCalibrationDialog")
		except ApiError as e:
			print(e)
	def cmdCorrectXrayDialog(self):
		try:
			self.executeCommand(self.objectName, "correctXrayDialog")
		except ApiError as e:
			print(e)
