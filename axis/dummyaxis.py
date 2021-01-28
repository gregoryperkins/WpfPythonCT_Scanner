from base import *

class Dummyaxis(Base):
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

	def setUserLimit(self, value):
		try:
			self.setValue(self.objectName, "userLimit", value)
		except ApiError as e:
			print(e)
	def getUserLimit(self):
		try:
			return self.getValue(self.objectName, "userLimit")
		except ApiError as e:
			print(e)

	def setOffset(self, value):
		try:
			self.setValue(self.objectName, "offset", value)
		except ApiError as e:
			print(e)
	def getOffset(self):
		try:
			return self.getValue(self.objectName, "offset")
		except ApiError as e:
			print(e)

	def setPosition(self, value):
		try:
			self.setValue(self.objectName, "position", value)
		except ApiError as e:
			print(e)
	def getPosition(self):
		try:
			return self.getValue(self.objectName, "position")
		except ApiError as e:
			print(e)

	def getLimPosition(self):
		try:
			return self.getValue(self.objectName, "limPosition")
		except ApiError as e:
			print(e)

	def getCurrentPosition(self):
		try:
			return self.getValue(self.objectName, "currentPosition")
		except ApiError as e:
			print(e)

	def getPositionReached(self):
		try:
			return self.getValue(self.objectName, "positionReached")
		except ApiError as e:
			print(e)

	def getPositionLimited(self):
		try:
			return self.getValue(self.objectName, "positionLimited")
		except ApiError as e:
			print(e)

	def setSlaveOffset(self, value):
		try:
			self.setValue(self.objectName, "slaveOffset", value)
		except ApiError as e:
			print(e)
	def getSlaveOffset(self):
		try:
			return self.getValue(self.objectName, "slaveOffset")
		except ApiError as e:
			print(e)

	def setSlaveScale(self, value):
		try:
			self.setValue(self.objectName, "slaveScale", value)
		except ApiError as e:
			print(e)
	def getSlaveScale(self):
		try:
			return self.getValue(self.objectName, "slaveScale")
		except ApiError as e:
			print(e)

	def setMaster(self, value):
		try:
			self.setValue(self.objectName, "master", value)
		except ApiError as e:
			print(e)
	def getMaster(self):
		try:
			return self.getValue(self.objectName, "master")
		except ApiError as e:
			print(e)

	def setMinLimit(self, value):
		try:
			self.setValue(self.objectName, "minLimit", value)
		except ApiError as e:
			print(e)
	def getMinLimit(self):
		try:
			return self.getValue(self.objectName, "minLimit")
		except ApiError as e:
			print(e)

	def setMaxLimit(self, value):
		try:
			self.setValue(self.objectName, "maxLimit", value)
		except ApiError as e:
			print(e)
	def getMaxLimit(self):
		try:
			return self.getValue(self.objectName, "maxLimit")
		except ApiError as e:
			print(e)

	def setSpeedLimit(self, value):
		try:
			self.setValue(self.objectName, "speedLimit", value)
		except ApiError as e:
			print(e)
	def getSpeedLimit(self):
		try:
			return self.getValue(self.objectName, "speedLimit")
		except ApiError as e:
			print(e)

	def setAccelerationLimit(self, value):
		try:
			self.setValue(self.objectName, "accelerationLimit", value)
		except ApiError as e:
			print(e)
	def getAccelerationLimit(self):
		try:
			return self.getValue(self.objectName, "accelerationLimit")
		except ApiError as e:
			print(e)

	def setDecelerationLimit(self, value):
		try:
			self.setValue(self.objectName, "decelerationLimit", value)
		except ApiError as e:
			print(e)
	def getDecelerationLimit(self):
		try:
			return self.getValue(self.objectName, "decelerationLimit")
		except ApiError as e:
			print(e)

	def setSpeed(self, value):
		try:
			self.setValue(self.objectName, "speed", value)
		except ApiError as e:
			print(e)
	def getSpeed(self):
		try:
			return self.getValue(self.objectName, "speed")
		except ApiError as e:
			print(e)

	def setEnabled(self, value):
		try:
			self.setValue(self.objectName, "enabled", value)
		except ApiError as e:
			print(e)
	def getEnabled(self):
		try:
			return self.getValue(self.objectName, "enabled")
		except ApiError as e:
			print(e)

	def getUnit(self):
		try:
			return self.getValue(self.objectName, "unit")
		except ApiError as e:
			print(e)

	def getDirection(self):
		try:
			return self.getValue(self.objectName, "direction")
		except ApiError as e:
			print(e)

	def setVisibleInAxisControl(self, value):
		try:
			self.setValue(self.objectName, "visibleInAxisControl", value)
		except ApiError as e:
			print(e)
	def getVisibleInAxisControl(self):
		try:
			return self.getValue(self.objectName, "visibleInAxisControl")
		except ApiError as e:
			print(e)

	def setModulo(self, value):
		try:
			self.setValue(self.objectName, "modulo", value)
		except ApiError as e:
			print(e)
	def getModulo(self):
		try:
			return self.getValue(self.objectName, "modulo")
		except ApiError as e:
			print(e)

	def getIsManual(self):
		try:
			return self.getValue(self.objectName, "isManual")
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
	def cmdHomingAvailable(self):
		try:
			self.executeCommand(self.objectName, "homingAvailable")
		except ApiError as e:
			print(e)
	def cmdSuportsTriggerPulses(self, pulses, perNUnits):
		try:
			parameters = [pulses, perNUnits]
			self.executeCommand(self.objectName, "suportsTriggerPulses", parameters)
		except ApiError as e:
			print(e)
	def cmdEnableTriggerOutput(self, pulses, perNUnits, startPosition):
		try:
			parameters = [pulses, perNUnits, startPosition]
			self.executeCommand(self.objectName, "enableTriggerOutput", parameters)
		except ApiError as e:
			print(e)
	def cmdEnableJoystickInput(self):
		try:
			self.executeCommand(self.objectName, "enableJoystickInput")
		except ApiError as e:
			print(e)
	def cmdSetHalfSpeed(self):
		try:
			self.executeCommand(self.objectName, "setHalfSpeed")
		except ApiError as e:
			print(e)
	def cmdSetFullSpeed(self):
		try:
			self.executeCommand(self.objectName, "setFullSpeed")
		except ApiError as e:
			print(e)
	def cmdSetLowSpeed(self):
		try:
			self.executeCommand(self.objectName, "setLowSpeed")
		except ApiError as e:
			print(e)
	def cmdJoystickInput(self):
		try:
			self.executeCommand(self.objectName, "joystickInput")
		except ApiError as e:
			print(e)
	def cmdJoystickInputInverse(self):
		try:
			self.executeCommand(self.objectName, "joystickInputInverse")
		except ApiError as e:
			print(e)
	def cmdHoming(self):
		try:
			self.executeCommand(self.objectName, "homing")
		except ApiError as e:
			print(e)
	def cmdStopHoming(self):
		try:
			self.executeCommand(self.objectName, "stopHoming")
		except ApiError as e:
			print(e)
	def cmdZero(self):
		try:
			self.executeCommand(self.objectName, "zero")
		except ApiError as e:
			print(e)
	def cmdStop(self):
		try:
			self.executeCommand(self.objectName, "stop")
		except ApiError as e:
			print(e)
	def cmdStopAndSync(self):
		try:
			self.executeCommand(self.objectName, "stopAndSync")
		except ApiError as e:
			print(e)
	def cmdSetInterlockState(self):
		try:
			self.executeCommand(self.objectName, "setInterlockState")
		except ApiError as e:
			print(e)
	def cmdSetSlowSpeed(self):
		try:
			self.executeCommand(self.objectName, "setSlowSpeed")
		except ApiError as e:
			print(e)
	def cmdSetDirection(self, x, y, z, write):
		try:
			parameters = [x, y, z, write]
			self.executeCommand(self.objectName, "setDirection", parameters)
		except ApiError as e:
			print(e)
	def cmdDebugLimits(self):
		try:
			self.executeCommand(self.objectName, "debugLimits")
		except ApiError as e:
			print(e)
	def cmdDisableGeometry(self):
		try:
			self.executeCommand(self.objectName, "disableGeometry")
		except ApiError as e:
			print(e)
	def cmdSetDisableOnEmergencyStop(self, disable):
		try:
			parameters = [disable]
			self.executeCommand(self.objectName, "setDisableOnEmergencyStop", parameters)
		except ApiError as e:
			print(e)
	def cmdSetIngoreInterLock(self, ignore):
		try:
			parameters = [ignore]
			self.executeCommand(self.objectName, "setIngoreInterLock", parameters)
		except ApiError as e:
			print(e)
	def cmdClearMinLimit(self):
		try:
			self.executeCommand(self.objectName, "clearMinLimit")
		except ApiError as e:
			print(e)
	def cmdClearMaxLimit(self):
		try:
			self.executeCommand(self.objectName, "clearMaxLimit")
		except ApiError as e:
			print(e)
	def cmdFilterPosition(self, position, retry):
		try:
			parameters = [position, retry]
			self.executeCommand(self.objectName, "filterPosition", parameters)
		except ApiError as e:
			print(e)
	def cmdSetPosition(self, position):
		try:
			parameters = [position]
			self.executeCommand(self.objectName, "setPosition", parameters)
		except ApiError as e:
			print(e)
	def cmdPositionHandler(self):
		try:
			self.executeCommand(self.objectName, "positionHandler")
		except ApiError as e:
			print(e)
