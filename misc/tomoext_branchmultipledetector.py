from base import *

class Tomoext_Branchmultipledetector(Base):
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

	def setImagers(self, value):
		try:
			self.setValue(self.objectName, "imagers", value)
		except ApiError as e:
			print(e)
	def getImagers(self):
		try:
			return self.getValue(self.objectName, "imagers")
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

	def setBeamAlignment(self, value):
		try:
			self.setValue(self.objectName, "beamAlignment", value)
		except ApiError as e:
			print(e)
	def getBeamAlignment(self):
		try:
			return self.getValue(self.objectName, "beamAlignment")
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

	def setUseCustomTurnParam(self, value):
		try:
			self.setValue(self.objectName, "useCustomTurnParam", value)
		except ApiError as e:
			print(e)
	def getUseCustomTurnParam(self):
		try:
			return self.getValue(self.objectName, "useCustomTurnParam")
		except ApiError as e:
			print(e)

	def setCustomTurnParam(self, value):
		try:
			self.setValue(self.objectName, "customTurnParam", value)
		except ApiError as e:
			print(e)
	def getCustomTurnParam(self):
		try:
			return self.getValue(self.objectName, "customTurnParam")
		except ApiError as e:
			print(e)

	def setKeepProjInMemory(self, value):
		try:
			self.setValue(self.objectName, "keepProjInMemory", value)
		except ApiError as e:
			print(e)
	def getKeepProjInMemory(self):
		try:
			return self.getValue(self.objectName, "keepProjInMemory")
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
	def cmdSetVerticalStart(self):
		try:
			self.executeCommand(self.objectName, "setVerticalStart")
		except ApiError as e:
			print(e)
	def cmdSetVerticalEnd(self):
		try:
			self.executeCommand(self.objectName, "setVerticalEnd")
		except ApiError as e:
			print(e)
	def cmdUseCustomTurnParam(self):
		try:
			self.executeCommand(self.objectName, "useCustomTurnParam")
		except ApiError as e:
			print(e)
	def cmdSetUseCustomTurnParam(self, b):
		try:
			parameters = [b]
			self.executeCommand(self.objectName, "setUseCustomTurnParam", parameters)
		except ApiError as e:
			print(e)
	def cmdUpdateAvrFrame(self, avr):
		try:
			parameters = [avr]
			self.executeCommand(self.objectName, "updateAvrFrame", parameters)
		except ApiError as e:
			print(e)
	def cmdSetCustomTurnParam(self, param):
		try:
			parameters = [param]
			self.executeCommand(self.objectName, "setCustomTurnParam", parameters)
		except ApiError as e:
			print(e)
	def cmdSetCustomTurnParam(self, param):
		try:
			parameters = [param]
			self.executeCommand(self.objectName, "setCustomTurnParam", parameters)
		except ApiError as e:
			print(e)
	def cmdTurnParamList(self):
		try:
			self.executeCommand(self.objectName, "turnParamList")
		except ApiError as e:
			print(e)
	def cmdCustomTurnParam(self):
		try:
			self.executeCommand(self.objectName, "customTurnParam")
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
	def cmdFinished(self):
		try:
			self.executeCommand(self.objectName, "finished")
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
	def cmdSelectedImagers(self):
		try:
			self.executeCommand(self.objectName, "selectedImagers")
		except ApiError as e:
			print(e)
	def cmdSetImagersFromString(self, imagers):
		try:
			parameters = [imagers]
			self.executeCommand(self.objectName, "setImagersFromString", parameters)
		except ApiError as e:
			print(e)
	def cmdImagerListToStringList(self):
		try:
			self.executeCommand(self.objectName, "imagerListToStringList")
		except ApiError as e:
			print(e)
	def cmdSetImagersFromStringList(self, imagers):
		try:
			parameters = [imagers]
			self.executeCommand(self.objectName, "setImagersFromStringList", parameters)
		except ApiError as e:
			print(e)
	def cmdSetImagers(self, imagers):
		try:
			parameters = [imagers]
			self.executeCommand(self.objectName, "setImagers", parameters)
		except ApiError as e:
			print(e)
	def cmdSetImager(self, imager):
		try:
			parameters = [imager]
			self.executeCommand(self.objectName, "setImager", parameters)
		except ApiError as e:
			print(e)
	def cmdSetVirtualCentering(self, enable):
		try:
			parameters = [enable]
			self.executeCommand(self.objectName, "setVirtualCentering", parameters)
		except ApiError as e:
			print(e)
	def cmdSetNumberOfTurns(self):
		try:
			self.executeCommand(self.objectName, "setNumberOfTurns")
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
	def cmdRotationAxisOffset(self):
		try:
			self.executeCommand(self.objectName, "rotationAxisOffset")
		except ApiError as e:
			print(e)
	def cmdSetRotationAxisOffsetAntiRing(self):
		try:
			self.executeCommand(self.objectName, "setRotationAxisOffsetAntiRing")
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
	def cmdSetExternalVolume(self, im, diam, top, bottom, position):
		try:
			parameters = [im, diam, top, bottom, position]
			self.executeCommand(self.objectName, "setExternalVolume", parameters)
		except ApiError as e:
			print(e)
	def cmdShowCustomTrunPopup(self):
		try:
			self.executeCommand(self.objectName, "showCustomTrunPopup")
		except ApiError as e:
			print(e)
	def cmdCustomTurnPopupEnabled(self):
		try:
			self.executeCommand(self.objectName, "customTurnPopupEnabled")
		except ApiError as e:
			print(e)
	def cmdUpdateCustomParam(self, param):
		try:
			parameters = [param]
			self.executeCommand(self.objectName, "updateCustomParam", parameters)
		except ApiError as e:
			print(e)
	def cmdNumberOfImagePerTurnList(self):
		try:
			self.executeCommand(self.objectName, "numberOfImagePerTurnList")
		except ApiError as e:
			print(e)
	def cmdAvrFramesPerTurnList(self, im):
		try:
			parameters = [im]
			self.executeCommand(self.objectName, "avrFramesPerTurnList", parameters)
		except ApiError as e:
			print(e)
	def cmdDisplayZoom(self):
		try:
			self.executeCommand(self.objectName, "displayZoom")
		except ApiError as e:
			print(e)
	def cmdKeepProjInMemory(self):
		try:
			self.executeCommand(self.objectName, "keepProjInMemory")
		except ApiError as e:
			print(e)
	def cmdSetKeepProjInMemory(self, b):
		try:
			parameters = [b]
			self.executeCommand(self.objectName, "setKeepProjInMemory", parameters)
		except ApiError as e:
			print(e)
