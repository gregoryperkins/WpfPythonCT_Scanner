from base import *

class Wizardinterface(Base):
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
	def cmdStartAutoExposure(self):
		try:
			self.executeCommand(self.objectName, "startAutoExposure")
		except ApiError as e:
			print(e)
	def cmdPrepareObjectDetection(self):
		try:
			self.executeCommand(self.objectName, "prepareObjectDetection")
		except ApiError as e:
			print(e)
	def cmdPrepareZoom(self, adjustOnDiameter):
		try:
			parameters = [adjustOnDiameter]
			self.executeCommand(self.objectName, "prepareZoom", parameters)
		except ApiError as e:
			print(e)
	def cmdStartMovement(self):
		try:
			self.executeCommand(self.objectName, "startMovement")
		except ApiError as e:
			print(e)
	def cmdStopMovement(self):
		try:
			self.executeCommand(self.objectName, "stopMovement")
		except ApiError as e:
			print(e)
