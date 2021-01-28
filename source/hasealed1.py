from base import *

class Hasealed1(Base):
	def __init__(self, objectName):
		#super().__init__(self, objectName)
		Base.__init__(self, objectName)
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

	def setXRayEnabled(self, value):
		try:
			self.setValue(self.objectName, "xRayEnabled", value)
		except ApiError as e:
			print(e)
	def getXRayEnabled(self):
		try:
			return self.getValue(self.objectName, "xRayEnabled")
		except ApiError as e:
			print(e)

	def getInterlockClosed(self):
		try:
			return self.getValue(self.objectName, "interlockClosed")
		except ApiError as e:
			print(e)

	def setTimer(self, value):
		try:
			self.setValue(self.objectName, "timer", value)
		except ApiError as e:
			print(e)
	def getTimer(self):
		try:
			return self.getValue(self.objectName, "timer")
		except ApiError as e:
			print(e)

	def setFilter(self, value):
		try:
			self.setValue(self.objectName, "filter", value)
		except ApiError as e:
			print(e)
	def getFilter(self):
		try:
			return self.getValue(self.objectName, "filter")
		except ApiError as e:
			print(e)

	def setVoltage(self, value):
		try:
			self.setValue(self.objectName, "voltage", value)
		except ApiError as e:
			print(e)
	def getVoltage(self):
		try:
			return self.getValue(self.objectName, "voltage")
		except ApiError as e:
			print(e)

	def getMaxVoltage(self):
		try:
			return self.getValue(self.objectName, "maxVoltage")
		except ApiError as e:
			print(e)

	def getMinVoltage(self):
		try:
			return self.getValue(self.objectName, "minVoltage")
		except ApiError as e:
			print(e)

	def getMsrtVoltage(self):
		try:
			return self.getValue(self.objectName, "msrtVoltage")
		except ApiError as e:
			print(e)

	def setCurrent(self, value):
		try:
			self.setValue(self.objectName, "current", value)
		except ApiError as e:
			print(e)
	def getCurrent(self):
		try:
			return self.getValue(self.objectName, "current")
		except ApiError as e:
			print(e)

	def getMaxCurrent(self):
		try:
			return self.getValue(self.objectName, "maxCurrent")
		except ApiError as e:
			print(e)

	def getMinCurrent(self):
		try:
			return self.getValue(self.objectName, "minCurrent")
		except ApiError as e:
			print(e)

	def getMsrtCurrent(self):
		try:
			return self.getValue(self.objectName, "msrtCurrent")
		except ApiError as e:
			print(e)

	def getPowerLimit(self):
		try:
			return self.getValue(self.objectName, "powerLimit")
		except ApiError as e:
			print(e)

	def setFocalMode(self, value):
		try:
			self.setValue(self.objectName, "focalMode", value)
		except ApiError as e:
			print(e)
	def getFocalMode(self):
		try:
			return self.getValue(self.objectName, "focalMode")
		except ApiError as e:
			print(e)

	def getFocalModeList(self):
		try:
			return self.getValue(self.objectName, "focalModeList")
		except ApiError as e:
			print(e)

	def getMaxFocalMode(self):
		try:
			return self.getValue(self.objectName, "maxFocalMode")
		except ApiError as e:
			print(e)

	def getSpotsize(self):
		try:
			return self.getValue(self.objectName, "spotsize")
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
	def cmdXRayEnabled(self):
		try:
			self.executeCommand(self.objectName, "xRayEnabled")
		except ApiError as e:
			print(e)
	def cmdXRayOn(self):
		try:
			self.executeCommand(self.objectName, "xRayOn")
		except ApiError as e:
			print(e)
	def cmdXRayOff(self):
		try:
			self.executeCommand(self.objectName, "xRayOff")
		except ApiError as e:
			print(e)
	def cmdSetEmergencyStop(self, es):
		try:
			parameters = [es]
			self.executeCommand(self.objectName, "setEmergencyStop", parameters)
		except ApiError as e:
			print(e)
	def cmdStartHardware(self):
		try:
			self.executeCommand(self.objectName, "startHardware")
		except ApiError as e:
			print(e)
	def cmdHardwareReady(self):
		try:
			self.executeCommand(self.objectName, "hardwareReady")
		except ApiError as e:
			print(e)
	def cmdHardwareOn(self):
		try:
			self.executeCommand(self.objectName, "hardwareOn")
		except ApiError as e:
			print(e)
	def cmdAbstractSourceGuiDestroyed(self):
		try:
			self.executeCommand(self.objectName, "abstractSourceGuiDestroyed")
		except ApiError as e:
			print(e)
	def cmdXRayTimerEvent(self):
		try:
			self.executeCommand(self.objectName, "xRayTimerEvent")
		except ApiError as e:
			print(e)
	def cmdUpdateXRayIcon(self, on):
		try:
			parameters = [on]
			self.executeCommand(self.objectName, "updateXRayIcon", parameters)
		except ApiError as e:
			print(e)
	def cmdSaveSettings(self):
		try:
			self.executeCommand(self.objectName, "saveSettings")
		except ApiError as e:
			print(e)
	def cmdSetTimer(self, value):
		try:
			parameters = [value]
			self.executeCommand(self.objectName, "setTimer", parameters)
		except ApiError as e:
			print(e)
	def cmdSetXRayEnabled(self):
		try:
			self.executeCommand(self.objectName, "setXRayEnabled")
		except ApiError as e:
			print(e)
	def cmdSetInterLockState(self, closed):
		try:
			parameters = [closed]
			self.executeCommand(self.objectName, "setInterLockState", parameters)
		except ApiError as e:
			print(e)
	def cmdUpdateXRayButtons(self):
		try:
			self.executeCommand(self.objectName, "updateXRayButtons")
		except ApiError as e:
			print(e)
	def cmdSetFilter(self, notify):
		try:
			parameters = [notify]
			self.executeCommand(self.objectName, "setFilter", parameters)
		except ApiError as e:
			print(e)
	def cmdAbstractXRayGeneratorGuiDestroyed(self):
		try:
			self.executeCommand(self.objectName, "abstractXRayGeneratorGuiDestroyed")
		except ApiError as e:
			print(e)
	def cmdRequestSpotsize(self, s):
		try:
			parameters = [s]
			self.executeCommand(self.objectName, "requestSpotsize", parameters)
		except ApiError as e:
			print(e)
	def cmdReset(self):
		try:
			self.executeCommand(self.objectName, "reset")
		except ApiError as e:
			print(e)
	def cmdSetFocalMode(self, m):
		try:
			parameters = [m]
			self.executeCommand(self.objectName, "setFocalMode", parameters)
		except ApiError as e:
			print(e)
	def cmdSetMsrtVoltage(self, val):
		try:
			parameters = [val]
			self.executeCommand(self.objectName, "setMsrtVoltage", parameters)
		except ApiError as e:
			print(e)
	def cmdSetMsrtCurrent(self):
		try:
			self.executeCommand(self.objectName, "setMsrtCurrent")
		except ApiError as e:
			print(e)
	def cmdUpdateVoltageLimitation(self):
		try:
			self.executeCommand(self.objectName, "updateVoltageLimitation")
		except ApiError as e:
			print(e)
	def cmdForceNotReadyTimeOut(self):
		try:
			self.executeCommand(self.objectName, "forceNotReadyTimeOut")
		except ApiError as e:
			print(e)
	def cmdStartForceNotReadyTimer(self):
		try:
			self.executeCommand(self.objectName, "startForceNotReadyTimer")
		except ApiError as e:
			print(e)
	def cmdSetVoltage(self, volt):
		try:
			parameters = [volt]
			self.executeCommand(self.objectName, "setVoltage", parameters)
		except ApiError as e:
			print(e)
	def cmdSetCurrent(self, curr):
		try:
			parameters = [curr]
			self.executeCommand(self.objectName, "setCurrent", parameters)
		except ApiError as e:
			print(e)
	def cmdSetPreheat(self):
		try:
			self.executeCommand(self.objectName, "setPreheat")
		except ApiError as e:
			print(e)
	def cmdSetStatus(self):
		try:
			self.executeCommand(self.objectName, "setStatus")
		except ApiError as e:
			print(e)
	def cmdCheckReady(self):
		try:
			self.executeCommand(self.objectName, "checkReady")
		except ApiError as e:
			print(e)
	def cmdSwitchOffIo(self):
		try:
			self.executeCommand(self.objectName, "switchOffIo")
		except ApiError as e:
			print(e)
	def cmdDebugSetTemperature(self, temp):
		try:
			parameters = [temp]
			self.executeCommand(self.objectName, "debugSetTemperature", parameters)
		except ApiError as e:
			print(e)
	def cmdUpdateIoTimer(self, xRayState):
		try:
			parameters = [xRayState]
			self.executeCommand(self.objectName, "updateIoTimer", parameters)
		except ApiError as e:
			print(e)
	def cmdSetTemperature(self):
		try:
			self.executeCommand(self.objectName, "setTemperature")
		except ApiError as e:
			print(e)
	def cmdDestroy(self):
		try:
			self.executeCommand(self.objectName, "destroy")
		except ApiError as e:
			print(e)
	def cmdInitXRayType(self):
		try:
			self.executeCommand(self.objectName, "initXRayType")
		except ApiError as e:
			print(e)
	def cmdIoConnected(self):
		try:
			self.executeCommand(self.objectName, "ioConnected")
		except ApiError as e:
			print(e)
	def cmdInit(self):
		try:
			self.executeCommand(self.objectName, "init")
		except ApiError as e:
			print(e)
	def cmdSwitchOnIo(self):
		try:
			self.executeCommand(self.objectName, "switchOnIo")
		except ApiError as e:
			print(e)
	def cmdGuiDestroyed(self):
		try:
			self.executeCommand(self.objectName, "guiDestroyed")
		except ApiError as e:
			print(e)
	def cmdSetTimePowerOn(self):
		try:
			self.executeCommand(self.objectName, "setTimePowerOn")
		except ApiError as e:
			print(e)
	def cmdSetTimeXRayOn(self):
		try:
			self.executeCommand(self.objectName, "setTimeXRayOn")
		except ApiError as e:
			print(e)
