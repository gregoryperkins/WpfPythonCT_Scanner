from base import *

class Tomowizard(Base):
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
	def cmdMainWindowDestroyed(self):
		try:
			self.executeCommand(self.objectName, "mainWindowDestroyed")
		except ApiError as e:
			print(e)
	def cmdTomographyParamsSet(self):
		try:
			self.executeCommand(self.objectName, "tomographyParamsSet")
		except ApiError as e:
			print(e)
	def cmdSpotSizeSet(self):
		try:
			self.executeCommand(self.objectName, "spotSizeSet")
		except ApiError as e:
			print(e)
	def cmdImagerParamsSet(self):
		try:
			self.executeCommand(self.objectName, "imagerParamsSet")
		except ApiError as e:
			print(e)
	def cmdBlackCalibrationDone(self):
		try:
			self.executeCommand(self.objectName, "blackCalibrationDone")
		except ApiError as e:
			print(e)
	def cmdGainCalibrationDone(self):
		try:
			self.executeCommand(self.objectName, "gainCalibrationDone")
		except ApiError as e:
			print(e)
	def cmdXRaySwitchedOffForBlackCalibration(self):
		try:
			self.executeCommand(self.objectName, "xRaySwitchedOffForBlackCalibration")
		except ApiError as e:
			print(e)
	def cmdAcquisitionCanceled(self):
		try:
			self.executeCommand(self.objectName, "acquisitionCanceled")
		except ApiError as e:
			print(e)
	def cmdRemoveSampleManually(self):
		try:
			self.executeCommand(self.objectName, "removeSampleManually")
		except ApiError as e:
			print(e)
	def cmdSetSampleManually(self):
		try:
			self.executeCommand(self.objectName, "setSampleManually")
		except ApiError as e:
			print(e)
	def cmdXRayOnAfterSampleSet(self):
		try:
			self.executeCommand(self.objectName, "xRayOnAfterSampleSet")
		except ApiError as e:
			print(e)
	def cmdAutoExpoBeforeVolumeDetection(self):
		try:
			self.executeCommand(self.objectName, "autoExpoBeforeVolumeDetection")
		except ApiError as e:
			print(e)
	def cmdDebugProjection(self):
		try:
			self.executeCommand(self.objectName, "debugProjection")
		except ApiError as e:
			print(e)
	def cmdWizardCanceled(self):
		try:
			self.executeCommand(self.objectName, "wizardCanceled")
		except ApiError as e:
			print(e)
	def cmdComputeTomoProfiles(self):
		try:
			self.executeCommand(self.objectName, "computeTomoProfiles")
		except ApiError as e:
			print(e)
	def cmdCancel(self):
		try:
			self.executeCommand(self.objectName, "cancel")
		except ApiError as e:
			print(e)
	def cmdSkipWaitingTime(self):
		try:
			self.executeCommand(self.objectName, "skipWaitingTime")
		except ApiError as e:
			print(e)
	def cmdSetRotationAxisOffset(self):
		try:
			self.executeCommand(self.objectName, "setRotationAxisOffset")
		except ApiError as e:
			print(e)
	def cmdTomographyPositionOffset(self):
		try:
			self.executeCommand(self.objectName, "tomographyPositionOffset")
		except ApiError as e:
			print(e)
	def cmdSetUpForDrawCylinder(self):
		try:
			self.executeCommand(self.objectName, "setUpForDrawCylinder")
		except ApiError as e:
			print(e)
	def cmdCylinderDone(self):
		try:
			self.executeCommand(self.objectName, "cylinderDone")
		except ApiError as e:
			print(e)
	def cmdTomography_progess(self):
		try:
			self.executeCommand(self.objectName, "tomography_progess")
		except ApiError as e:
			print(e)
	def cmdTomographyFinished(self):
		try:
			self.executeCommand(self.objectName, "tomographyFinished")
		except ApiError as e:
			print(e)
	def cmdRunGainCalibration(self):
		try:
			self.executeCommand(self.objectName, "runGainCalibration")
		except ApiError as e:
			print(e)
	def cmdRunBlackCalibration(self):
		try:
			self.executeCommand(self.objectName, "runBlackCalibration")
		except ApiError as e:
			print(e)
	def cmdStartAcquisition(self):
		try:
			self.executeCommand(self.objectName, "startAcquisition")
		except ApiError as e:
			print(e)
	def cmdCancelAcquisition(self):
		try:
			self.executeCommand(self.objectName, "cancelAcquisition")
		except ApiError as e:
			print(e)
	def cmdPrepareStartAcquisition(self):
		try:
			self.executeCommand(self.objectName, "prepareStartAcquisition")
		except ApiError as e:
			print(e)
	def cmdResetAxisPosition(self):
		try:
			self.executeCommand(self.objectName, "resetAxisPosition")
		except ApiError as e:
			print(e)
	def cmdResetSampleInField(self):
		try:
			self.executeCommand(self.objectName, "resetSampleInField")
		except ApiError as e:
			print(e)
	def cmdSetTomographyProperties(self):
		try:
			self.executeCommand(self.objectName, "setTomographyProperties")
		except ApiError as e:
			print(e)
	def cmdDebugDetectBorders(self, filter):
		try:
			parameters = [filter]
			self.executeCommand(self.objectName, "debugDetectBorders", parameters)
		except ApiError as e:
			print(e)
	def cmdResetState(self):
		try:
			self.executeCommand(self.objectName, "resetState")
		except ApiError as e:
			print(e)
	def cmdMinImageReadyDebug(self):
		try:
			self.executeCommand(self.objectName, "minImageReadyDebug")
		except ApiError as e:
			print(e)
	def cmdStdMapReady(self):
		try:
			self.executeCommand(self.objectName, "stdMapReady")
		except ApiError as e:
			print(e)
	def cmdDebugProfileList(self, voxelSize, frameRate, focalSpot, sourcePower):
		try:
			parameters = [voxelSize, frameRate, focalSpot, sourcePower]
			self.executeCommand(self.objectName, "debugProfileList", parameters)
		except ApiError as e:
			print(e)
	def cmdWaitToStartAcquisition(self):
		try:
			self.executeCommand(self.objectName, "waitToStartAcquisition")
		except ApiError as e:
			print(e)
	def cmdContinuousRotationDone(self):
		try:
			self.executeCommand(self.objectName, "continuousRotationDone")
		except ApiError as e:
			print(e)
	def cmdThreadCanceled(self):
		try:
			self.executeCommand(self.objectName, "threadCanceled")
		except ApiError as e:
			print(e)
	def cmdQuickAcquisition(self):
		try:
			self.executeCommand(self.objectName, "quickAcquisition")
		except ApiError as e:
			print(e)
	def cmdSetQuickAcquisition(self, quickAcquisition):
		try:
			parameters = [quickAcquisition]
			self.executeCommand(self.objectName, "setQuickAcquisition", parameters)
		except ApiError as e:
			print(e)
	def cmdPowerXraySource(self):
		try:
			self.executeCommand(self.objectName, "powerXraySource")
		except ApiError as e:
			print(e)
	def cmdAxisStartPositionReached(self):
		try:
			self.executeCommand(self.objectName, "axisStartPositionReached")
		except ApiError as e:
			print(e)
	def cmdStartVolumeDetermination(self):
		try:
			self.executeCommand(self.objectName, "startVolumeDetermination")
		except ApiError as e:
			print(e)
	def cmdZoomFit(self):
		try:
			self.executeCommand(self.objectName, "zoomFit")
		except ApiError as e:
			print(e)
	def cmdSleepTimeFinished(self):
		try:
			self.executeCommand(self.objectName, "sleepTimeFinished")
		except ApiError as e:
			print(e)
	def cmdSleepBeforeAcquisition(self):
		try:
			self.executeCommand(self.objectName, "sleepBeforeAcquisition")
		except ApiError as e:
			print(e)
	def cmdImageProgress(self, inProgress):
		try:
			parameters = [inProgress]
			self.executeCommand(self.objectName, "imageProgress", parameters)
		except ApiError as e:
			print(e)
	def cmdShowImage(self, inImage):
		try:
			parameters = [inImage]
			self.executeCommand(self.objectName, "showImage", parameters)
		except ApiError as e:
			print(e)
	def cmdPrepareGainCalibration(self):
		try:
			self.executeCommand(self.objectName, "prepareGainCalibration")
		except ApiError as e:
			print(e)
	def cmdAdjustCurrentWithoutSample(self):
		try:
			self.executeCommand(self.objectName, "adjustCurrentWithoutSample")
		except ApiError as e:
			print(e)
	def cmdPrepareBlackCalibration(self):
		try:
			self.executeCommand(self.objectName, "prepareBlackCalibration")
		except ApiError as e:
			print(e)
	def cmdPositionSetAfterCentering(self):
		try:
			self.executeCommand(self.objectName, "positionSetAfterCentering")
		except ApiError as e:
			print(e)
