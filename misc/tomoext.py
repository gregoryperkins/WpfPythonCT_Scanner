from base import *

class Tomoext(Base):
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

	def setTomographyPosition(self, value):
		try:
			self.setValue(self.objectName, "tomographyPosition", value)
		except ApiError as e:
			print(e)
	def getTomographyPosition(self):
		try:
			return self.getValue(self.objectName, "tomographyPosition")
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

	def setNumberOfImagePerTurnList(self, value):
		try:
			self.setValue(self.objectName, "numberOfImagePerTurnList", value)
		except ApiError as e:
			print(e)
	def getNumberOfImagePerTurnList(self):
		try:
			return self.getValue(self.objectName, "numberOfImagePerTurnList")
		except ApiError as e:
			print(e)

	def setAvrFramesPerTurnList(self, value):
		try:
			self.setValue(self.objectName, "avrFramesPerTurnList", value)
		except ApiError as e:
			print(e)
	def getAvrFramesPerTurnList(self):
		try:
			return self.getValue(self.objectName, "avrFramesPerTurnList")
		except ApiError as e:
			print(e)

	def setTypeOption(self, value):
		try:
			self.setValue(self.objectName, "typeOption", value)
		except ApiError as e:
			print(e)
	def getTypeOption(self):
		try:
			return self.getValue(self.objectName, "typeOption")
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

	def setNumberOfTurns(self, value):
		try:
			self.setValue(self.objectName, "numberOfTurns", value)
		except ApiError as e:
			print(e)
	def getNumberOfTurns(self):
		try:
			return self.getValue(self.objectName, "numberOfTurns")
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

	def setNumberOfImagesPerTurn(self, value):
		try:
			self.setValue(self.objectName, "numberOfImagesPerTurn", value)
		except ApiError as e:
			print(e)
	def getNumberOfImagesPerTurn(self):
		try:
			return self.getValue(self.objectName, "numberOfImagesPerTurn")
		except ApiError as e:
			print(e)

	def setVerticalStart(self, value):
		try:
			self.setValue(self.objectName, "verticalStart", value)
		except ApiError as e:
			print(e)
	def getVerticalStart(self):
		try:
			return self.getValue(self.objectName, "verticalStart")
		except ApiError as e:
			print(e)

	def setVerticalEnd(self, value):
		try:
			self.setValue(self.objectName, "verticalEnd", value)
		except ApiError as e:
			print(e)
	def getVerticalEnd(self):
		try:
			return self.getValue(self.objectName, "verticalEnd")
		except ApiError as e:
			print(e)

	def setSleepTimeBlack(self, value):
		try:
			self.setValue(self.objectName, "sleepTimeBlack", value)
		except ApiError as e:
			print(e)
	def getSleepTimeBlack(self):
		try:
			return self.getValue(self.objectName, "sleepTimeBlack")
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

	def setSleepAfterMove(self, value):
		try:
			self.setValue(self.objectName, "sleepAfterMove", value)
		except ApiError as e:
			print(e)
	def getSleepAfterMove(self):
		try:
			return self.getValue(self.objectName, "sleepAfterMove")
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

	def setRunBlackCalibration(self, value):
		try:
			self.setValue(self.objectName, "runBlackCalibration", value)
		except ApiError as e:
			print(e)
	def getRunBlackCalibration(self):
		try:
			return self.getValue(self.objectName, "runBlackCalibration")
		except ApiError as e:
			print(e)

	def setRunGainCalibration(self, value):
		try:
			self.setValue(self.objectName, "runGainCalibration", value)
		except ApiError as e:
			print(e)
	def getRunGainCalibration(self):
		try:
			return self.getValue(self.objectName, "runGainCalibration")
		except ApiError as e:
			print(e)

	def setVirtualCentering(self, value):
		try:
			self.setValue(self.objectName, "virtualCentering", value)
		except ApiError as e:
			print(e)
	def getVirtualCentering(self):
		try:
			return self.getValue(self.objectName, "virtualCentering")
		except ApiError as e:
			print(e)

	def setCenterX(self, value):
		try:
			self.setValue(self.objectName, "centerX", value)
		except ApiError as e:
			print(e)
	def getCenterX(self):
		try:
			return self.getValue(self.objectName, "centerX")
		except ApiError as e:
			print(e)

	def setCenterZ(self, value):
		try:
			self.setValue(self.objectName, "centerZ", value)
		except ApiError as e:
			print(e)
	def getCenterZ(self):
		try:
			return self.getValue(self.objectName, "centerZ")
		except ApiError as e:
			print(e)

	def setLimitedAngleMin(self, value):
		try:
			self.setValue(self.objectName, "limitedAngleMin", value)
		except ApiError as e:
			print(e)
	def getLimitedAngleMin(self):
		try:
			return self.getValue(self.objectName, "limitedAngleMin")
		except ApiError as e:
			print(e)

	def setLimitedAngleMAx(self, value):
		try:
			self.setValue(self.objectName, "limitedAngleMAx", value)
		except ApiError as e:
			print(e)
	def getLimitedAngleMAx(self):
		try:
			return self.getValue(self.objectName, "limitedAngleMAx")
		except ApiError as e:
			print(e)

	def setTemplateReconstructionXML(self, value):
		try:
			self.setValue(self.objectName, "templateReconstructionXML", value)
		except ApiError as e:
			print(e)
	def getTemplateReconstructionXML(self):
		try:
			return self.getValue(self.objectName, "templateReconstructionXML")
		except ApiError as e:
			print(e)

	def setAntiRingShift(self, value):
		try:
			self.setValue(self.objectName, "antiRingShift", value)
		except ApiError as e:
			print(e)
	def getAntiRingShift(self):
		try:
			return self.getValue(self.objectName, "antiRingShift")
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

	def setSampleShift(self, value):
		try:
			self.setValue(self.objectName, "sampleShift", value)
		except ApiError as e:
			print(e)
	def getSampleShift(self):
		try:
			return self.getValue(self.objectName, "sampleShift")
		except ApiError as e:
			print(e)

	def setEnableAuto(self, value):
		try:
			self.setValue(self.objectName, "enableAuto", value)
		except ApiError as e:
			print(e)
	def getEnableAuto(self):
		try:
			return self.getValue(self.objectName, "enableAuto")
		except ApiError as e:
			print(e)

	def getEstimatedTime(self):
		try:
			return self.getValue(self.objectName, "estimatedTime")
		except ApiError as e:
			print(e)

	def setBoxWarning(self, value):
		try:
			self.setValue(self.objectName, "boxWarning", value)
		except ApiError as e:
			print(e)
	def getBoxWarning(self):
		try:
			return self.getValue(self.objectName, "boxWarning")
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
	def cmdCaptureVerticalStart(self):
		try:
			self.executeCommand(self.objectName, "captureVerticalStart")
		except ApiError as e:
			print(e)
	def cmdCaptureVerticalEnd(self):
		try:
			self.executeCommand(self.objectName, "captureVerticalEnd")
		except ApiError as e:
			print(e)
	def cmdGuiDestroyed(self):
		try:
			self.executeCommand(self.objectName, "guiDestroyed")
		except ApiError as e:
			print(e)
	def cmdSaveSettings(self):
		try:
			self.executeCommand(self.objectName, "saveSettings")
		except ApiError as e:
			print(e)
	def cmdStagePositionChanged(self, v):
		try:
			parameters = [v]
			self.executeCommand(self.objectName, "stagePositionChanged", parameters)
		except ApiError as e:
			print(e)
	def cmdRotationLimitsChanged(self):
		try:
			self.executeCommand(self.objectName, "rotationLimitsChanged")
		except ApiError as e:
			print(e)
	def cmdFinishedPrivate(self):
		try:
			self.executeCommand(self.objectName, "finishedPrivate")
		except ApiError as e:
			print(e)
	def cmdAcquiProgress(self):
		try:
			self.executeCommand(self.objectName, "acquiProgress")
		except ApiError as e:
			print(e)
	def cmdRotationAxisSetPositionChanged(self):
		try:
			self.executeCommand(self.objectName, "rotationAxisSetPositionChanged")
		except ApiError as e:
			print(e)
	def cmdSetVirtualCentering(self, enable):
		try:
			parameters = [enable]
			self.executeCommand(self.objectName, "setVirtualCentering", parameters)
		except ApiError as e:
			print(e)
	def cmdStartFromMacroPoint(self):
		try:
			self.executeCommand(self.objectName, "startFromMacroPoint")
		except ApiError as e:
			print(e)
	def cmdStart(self):
		try:
			self.executeCommand(self.objectName, "start")
		except ApiError as e:
			print(e)
	def cmdCancel(self):
		try:
			self.executeCommand(self.objectName, "cancel")
		except ApiError as e:
			print(e)
	def cmdSetRotationAxisOffset(self):
		try:
			self.executeCommand(self.objectName, "setRotationAxisOffset")
		except ApiError as e:
			print(e)
	def cmdSetRotationAxisOffsetAntiRing(self):
		try:
			self.executeCommand(self.objectName, "setRotationAxisOffsetAntiRing")
		except ApiError as e:
			print(e)
	def cmdTomographyPositionOffset(self):
		try:
			self.executeCommand(self.objectName, "tomographyPositionOffset")
		except ApiError as e:
			print(e)
	def cmdUpdateXZStageMatrix(self):
		try:
			self.executeCommand(self.objectName, "updateXZStageMatrix")
		except ApiError as e:
			print(e)
	def cmdUpdateCentering(self):
		try:
			self.executeCommand(self.objectName, "updateCentering")
		except ApiError as e:
			print(e)
	def cmdUpdtateLcdLabel(self, timeLeft):
		try:
			parameters = [timeLeft]
			self.executeCommand(self.objectName, "updtateLcdLabel", parameters)
		except ApiError as e:
			print(e)
	def cmdOptimizeXRaySpotSize(self):
		try:
			self.executeCommand(self.objectName, "optimizeXRaySpotSize")
		except ApiError as e:
			print(e)
	def cmdSetExternalVolume(self, diam, top, bottom, position):
		try:
			parameters = [diam, top, bottom, position]
			self.executeCommand(self.objectName, "setExternalVolume", parameters)
		except ApiError as e:
			print(e)
	def cmdStoreCurrentBeforeGain(self):
		try:
			self.executeCommand(self.objectName, "storeCurrentBeforeGain")
		except ApiError as e:
			print(e)
