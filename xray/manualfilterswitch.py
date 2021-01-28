from base import *

class Manualfilterswitch(Base):
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

	def getMinLimit(self):
		try:
			return self.getValue(self.objectName, "minLimit")
		except ApiError as e:
			print(e)

	def getMaxLimit(self):
		try:
			return self.getValue(self.objectName, "maxLimit")
		except ApiError as e:
			print(e)

	def getFilters(self):
		try:
			return self.getValue(self.objectName, "filters")
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
	def cmdGetFilterNames(self):
		try:
			self.executeCommand(self.objectName, "getFilterNames")
		except ApiError as e:
			print(e)
	def cmdGetCurrentFilterIndex(self):
		try:
			self.executeCommand(self.objectName, "getCurrentFilterIndex")
		except ApiError as e:
			print(e)
	def cmdGetCurrentFilterName(self):
		try:
			self.executeCommand(self.objectName, "getCurrentFilterName")
		except ApiError as e:
			print(e)
	def cmdLoadSettings(self):
		try:
			self.executeCommand(self.objectName, "loadSettings")
		except ApiError as e:
			print(e)
	def cmdEditFilterList(self):
		try:
			self.executeCommand(self.objectName, "editFilterList")
		except ApiError as e:
			print(e)
	def cmdSetFilter(self, index):
		try:
			parameters = [index]
			self.executeCommand(self.objectName, "setFilter", parameters)
		except ApiError as e:
			print(e)
	def cmdSetFilterByName(self, filterName, notify):
		try:
			parameters = [filterName, notify]
			self.executeCommand(self.objectName, "setFilterByName", parameters)
		except ApiError as e:
			print(e)
	def cmdHoming(self):
		try:
			self.executeCommand(self.objectName, "homing")
		except ApiError as e:
			print(e)
	def cmdSaveSettings(self):
		try:
			self.executeCommand(self.objectName, "saveSettings")
		except ApiError as e:
			print(e)
