from base import *

class Guidedacquisition(Base):
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
	def cmdState(self):
		try:
			self.executeCommand(self.objectName, "state")
		except ApiError as e:
			print(e)
	def cmdWaitForGhostRemoval(self):
		try:
			self.executeCommand(self.objectName, "waitForGhostRemoval")
		except ApiError as e:
			print(e)
	def cmdGhostRemoved(self):
		try:
			self.executeCommand(self.objectName, "ghostRemoved")
		except ApiError as e:
			print(e)
	def cmdStopWaitForGhostRemoval(self):
		try:
			self.executeCommand(self.objectName, "stopWaitForGhostRemoval")
		except ApiError as e:
			print(e)
	def cmdComputeTopAndBottomPosition(self, outTopPosition, outBottomPosition, simulation, inZoomPosition, inPosOnImager):
		try:
			parameters = [outTopPosition, outBottomPosition, simulation, inZoomPosition, inPosOnImager]
			self.executeCommand(self.objectName, "computeTopAndBottomPosition", parameters)
		except ApiError as e:
			print(e)
	def cmdDetectBorders(self):
		try:
			self.executeCommand(self.objectName, "detectBorders")
		except ApiError as e:
			print(e)
	def cmdPrepareTomoConfig(self, callback, verticalAxis):
		try:
			parameters = [callback, verticalAxis]
			self.executeCommand(self.objectName, "prepareTomoConfig", parameters)
		except ApiError as e:
			print(e)
	def cmdXRayReady(self):
		try:
			self.executeCommand(self.objectName, "xRayReady")
		except ApiError as e:
			print(e)
	def cmdFastCentering(self, callBack):
		try:
			parameters = [callBack]
			self.executeCommand(self.objectName, "fastCentering", parameters)
		except ApiError as e:
			print(e)
	def cmdComputeStagePosition(self, inStartingZoom, inDiameter):
		try:
			parameters = [inStartingZoom, inDiameter]
			self.executeCommand(self.objectName, "computeStagePosition", parameters)
		except ApiError as e:
			print(e)
	def cmdBordersDetected(self, left, right, top, bottom, fromAutoDetection):
		try:
			parameters = [left, right, top, bottom, fromAutoDetection]
			self.executeCommand(self.objectName, "bordersDetected", parameters)
		except ApiError as e:
			print(e)
	def cmdMinImageReady(self):
		try:
			self.executeCommand(self.objectName, "minImageReady")
		except ApiError as e:
			print(e)
	def cmdAutoExposureDone(self):
		try:
			self.executeCommand(self.objectName, "autoExposureDone")
		except ApiError as e:
			print(e)
	def cmdAutoExposureCanceled(self):
		try:
			self.executeCommand(self.objectName, "autoExposureCanceled")
		except ApiError as e:
			print(e)
	def cmdAdjustImagerParams(self, callback):
		try:
			parameters = [callback]
			self.executeCommand(self.objectName, "adjustImagerParams", parameters)
		except ApiError as e:
			print(e)
	def cmdSecurityLimit(self):
		try:
			self.executeCommand(self.objectName, "securityLimit")
		except ApiError as e:
			print(e)
	def cmdFillSecureAxis(self):
		try:
			self.executeCommand(self.objectName, "fillSecureAxis")
		except ApiError as e:
			print(e)
	def cmdCenterHSample(self, callBack, secureMovement):
		try:
			parameters = [callBack, secureMovement]
			self.executeCommand(self.objectName, "centerHSample", parameters)
		except ApiError as e:
			print(e)
	def cmdCylinderChanged(self):
		try:
			self.executeCommand(self.objectName, "cylinderChanged")
		except ApiError as e:
			print(e)
	def cmdAxisMovementProgress(self, progress):
		try:
			parameters = [progress]
			self.executeCommand(self.objectName, "axisMovementProgress", parameters)
		except ApiError as e:
			print(e)
	def cmdSleepTimeLeftBlack(self, timeLeft):
		try:
			parameters = [timeLeft]
			self.executeCommand(self.objectName, "sleepTimeLeftBlack", parameters)
		except ApiError as e:
			print(e)
	def cmdSleepTimeLeftGain(self, timeLeft):
		try:
			parameters = [timeLeft]
			self.executeCommand(self.objectName, "sleepTimeLeftGain", parameters)
		except ApiError as e:
			print(e)
	def cmdSleepTimeLeftAcquisition(self, timeLeft):
		try:
			parameters = [timeLeft]
			self.executeCommand(self.objectName, "sleepTimeLeftAcquisition", parameters)
		except ApiError as e:
			print(e)
	def cmdBorderDetectionDone(self):
		try:
			self.executeCommand(self.objectName, "borderDetectionDone")
		except ApiError as e:
			print(e)
	def cmdBorderDetectionFailed(self):
		try:
			self.executeCommand(self.objectName, "borderDetectionFailed")
		except ApiError as e:
			print(e)
	def cmdReadyToStartMovement(self):
		try:
			self.executeCommand(self.objectName, "readyToStartMovement")
		except ApiError as e:
			print(e)
	def cmdInterlockState(self, state):
		try:
			parameters = [state]
			self.executeCommand(self.objectName, "interlockState", parameters)
		except ApiError as e:
			print(e)
	def cmdImagerClipping(self):
		try:
			self.executeCommand(self.objectName, "imagerClipping")
		except ApiError as e:
			print(e)
	def cmdXRaySwitchedOnToShowImage(self):
		try:
			self.executeCommand(self.objectName, "xRaySwitchedOnToShowImage")
		except ApiError as e:
			print(e)
	def cmdAutomaticBordersDetection(self):
		try:
			self.executeCommand(self.objectName, "automaticBordersDetection")
		except ApiError as e:
			print(e)
	def cmdManualBordersDetection(self):
		try:
			self.executeCommand(self.objectName, "manualBordersDetection")
		except ApiError as e:
			print(e)
	def cmdZoomDone(self):
		try:
			self.executeCommand(self.objectName, "zoomDone")
		except ApiError as e:
			print(e)
	def cmdResetDone(self):
		try:
			self.executeCommand(self.objectName, "resetDone")
		except ApiError as e:
			print(e)
	def cmdCenterAfterZoom(self):
		try:
			self.executeCommand(self.objectName, "centerAfterZoom")
		except ApiError as e:
			print(e)
	def cmdPrepareStartAcquisition(self):
		try:
			self.executeCommand(self.objectName, "prepareStartAcquisition")
		except ApiError as e:
			print(e)
	def cmdStartProcess(self):
		try:
			self.executeCommand(self.objectName, "startProcess")
		except ApiError as e:
			print(e)
	def cmdQualityValueChanged(self, value):
		try:
			parameters = [value]
			self.executeCommand(self.objectName, "qualityValueChanged", parameters)
		except ApiError as e:
			print(e)
	def cmdWaitForSampleRemove(self):
		try:
			self.executeCommand(self.objectName, "waitForSampleRemove")
		except ApiError as e:
			print(e)
	def cmdRestorePositionsAfterSampleRemove(self, nextStep):
		try:
			parameters = [nextStep]
			self.executeCommand(self.objectName, "restorePositionsAfterSampleRemove", parameters)
		except ApiError as e:
			print(e)
	def cmdShowImage(self):
		try:
			self.executeCommand(self.objectName, "showImage")
		except ApiError as e:
			print(e)
	def cmdSetWaitingTimes(self):
		try:
			self.executeCommand(self.objectName, "setWaitingTimes")
		except ApiError as e:
			print(e)
	def cmdSkipWaitingTime(self):
		try:
			self.executeCommand(self.objectName, "skipWaitingTime")
		except ApiError as e:
			print(e)
	def cmdCancelAcquisition(self):
		try:
			self.executeCommand(self.objectName, "cancelAcquisition")
		except ApiError as e:
			print(e)
	def cmdCurrentGeneratorMaxKV(self):
		try:
			self.executeCommand(self.objectName, "currentGeneratorMaxKV")
		except ApiError as e:
			print(e)
	def cmdStartXRaysForGainCalibration(self):
		try:
			self.executeCommand(self.objectName, "startXRaysForGainCalibration")
		except ApiError as e:
			print(e)
	def cmdContinueWaitBlackCalibration(self):
		try:
			self.executeCommand(self.objectName, "continueWaitBlackCalibration")
		except ApiError as e:
			print(e)
	def cmdCheckStackAcqNecessity(self):
		try:
			self.executeCommand(self.objectName, "checkStackAcqNecessity")
		except ApiError as e:
			print(e)
	def cmdCheckShiftNecesssity(self):
		try:
			self.executeCommand(self.objectName, "checkShiftNecesssity")
		except ApiError as e:
			print(e)
	def cmdCheckZoomOutNecessity(self):
		try:
			self.executeCommand(self.objectName, "checkZoomOutNecessity")
		except ApiError as e:
			print(e)
	def cmdTomoBoxWarning(self, display):
		try:
			parameters = [display]
			self.executeCommand(self.objectName, "tomoBoxWarning", parameters)
		except ApiError as e:
			print(e)
	def cmdResetTomoDisabledFields(self):
		try:
			self.executeCommand(self.objectName, "resetTomoDisabledFields")
		except ApiError as e:
			print(e)
	def cmdWarningMessagesFromBox(self):
		try:
			self.executeCommand(self.objectName, "warningMessagesFromBox")
		except ApiError as e:
			print(e)
	def cmdStartAutomaticBorderDetection(self):
		try:
			self.executeCommand(self.objectName, "startAutomaticBorderDetection")
		except ApiError as e:
			print(e)
	def cmdZoomPositionChanged(self):
		try:
			self.executeCommand(self.objectName, "zoomPositionChanged")
		except ApiError as e:
			print(e)
	def cmdUpdateZoom(self):
		try:
			self.executeCommand(self.objectName, "updateZoom")
		except ApiError as e:
			print(e)
	def cmdXRaySwitchedOffForBlackCalibration(self):
		try:
			self.executeCommand(self.objectName, "xRaySwitchedOffForBlackCalibration")
		except ApiError as e:
			print(e)
	def cmdPrepareBlackCalibration(self):
		try:
			self.executeCommand(self.objectName, "prepareBlackCalibration")
		except ApiError as e:
			print(e)
	def cmdRunBlackCalibration(self):
		try:
			self.executeCommand(self.objectName, "runBlackCalibration")
		except ApiError as e:
			print(e)
	def cmdBlackCalibrationDone(self):
		try:
			self.executeCommand(self.objectName, "blackCalibrationDone")
		except ApiError as e:
			print(e)
	def cmdPrepareGainCalibration(self):
		try:
			self.executeCommand(self.objectName, "prepareGainCalibration")
		except ApiError as e:
			print(e)
	def cmdSleepBeforeAcquisition(self):
		try:
			self.executeCommand(self.objectName, "sleepBeforeAcquisition")
		except ApiError as e:
			print(e)
	def cmdSleepTimeFinished(self):
		try:
			self.executeCommand(self.objectName, "sleepTimeFinished")
		except ApiError as e:
			print(e)
	def cmdRunGainCalibration(self):
		try:
			self.executeCommand(self.objectName, "runGainCalibration")
		except ApiError as e:
			print(e)
	def cmdGainCalibrationDone(self):
		try:
			self.executeCommand(self.objectName, "gainCalibrationDone")
		except ApiError as e:
			print(e)
	def cmdWaitToStartAcquisition(self):
		try:
			self.executeCommand(self.objectName, "waitToStartAcquisition")
		except ApiError as e:
			print(e)
	def cmdStartAcquisition(self):
		try:
			self.executeCommand(self.objectName, "startAcquisition")
		except ApiError as e:
			print(e)
	def cmdTopAndBottomPositionFound(self, needStack, top, bottom):
		try:
			parameters = [needStack, top, bottom]
			self.executeCommand(self.objectName, "topAndBottomPositionFound", parameters)
		except ApiError as e:
			print(e)
	def cmdVoxelAndTurnEstimated(self, voxelHighestZoom, turnsHighestZoom, voxelHighZoom, turnsHighZoom):
		try:
			parameters = [voxelHighestZoom, turnsHighestZoom, voxelHighZoom, turnsHighZoom]
			self.executeCommand(self.objectName, "voxelAndTurnEstimated", parameters)
		except ApiError as e:
			print(e)
	def cmdTomographyProgress(self, progress):
		try:
			parameters = [progress]
			self.executeCommand(self.objectName, "tomographyProgress", parameters)
		except ApiError as e:
			print(e)
	def cmdTomographyFinished(self):
		try:
			self.executeCommand(self.objectName, "tomographyFinished")
		except ApiError as e:
			print(e)
	def cmdImageProgress(self, inProgress):
		try:
			parameters = [inProgress]
			self.executeCommand(self.objectName, "imageProgress", parameters)
		except ApiError as e:
			print(e)
