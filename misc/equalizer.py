from base import *

class Equalizer(Base):
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
	def cmdGuiDestroyed(self):
		try:
			self.executeCommand(self.objectName, "guiDestroyed")
		except ApiError as e:
			print(e)
	def cmdUpdateFilter(self):
		try:
			self.executeCommand(self.objectName, "updateFilter")
		except ApiError as e:
			print(e)
	def cmdUpdateFilterFinished(self):
		try:
			self.executeCommand(self.objectName, "updateFilterFinished")
		except ApiError as e:
			print(e)
	def cmdFilterArrayFinished(self):
		try:
			self.executeCommand(self.objectName, "filterArrayFinished")
		except ApiError as e:
			print(e)
	def cmdAddNewImage(self, nbImage):
		try:
			parameters = [nbImage]
			self.executeCommand(self.objectName, "addNewImage", parameters)
		except ApiError as e:
			print(e)
	def cmdUnlinkImageArray(self, imArray):
		try:
			parameters = [imArray]
			self.executeCommand(self.objectName, "unlinkImageArray", parameters)
		except ApiError as e:
			print(e)
	def cmdLinkImageArray(self, array):
		try:
			parameters = [array]
			self.executeCommand(self.objectName, "linkImageArray", parameters)
		except ApiError as e:
			print(e)
	def cmdThreadError(self, title, msg):
		try:
			parameters = [title, msg]
			self.executeCommand(self.objectName, "threadError", parameters)
		except ApiError as e:
			print(e)
	def cmdLinkCurrentImageArray(self):
		try:
			self.executeCommand(self.objectName, "linkCurrentImageArray")
		except ApiError as e:
			print(e)
	def cmdUnlinkLinkedImageArray(self):
		try:
			self.executeCommand(self.objectName, "unlinkLinkedImageArray")
		except ApiError as e:
			print(e)
	def cmdFilterArray(self):
		try:
			self.executeCommand(self.objectName, "filterArray")
		except ApiError as e:
			print(e)
	def cmdCancelFiltering(self):
		try:
			self.executeCommand(self.objectName, "cancelFiltering")
		except ApiError as e:
			print(e)
	def cmdSaveCurentFilterAsPrest(self, title):
		try:
			parameters = [title]
			self.executeCommand(self.objectName, "saveCurentFilterAsPrest", parameters)
		except ApiError as e:
			print(e)
	def cmdAddCustomerPreset(self, preset):
		try:
			parameters = [preset]
			self.executeCommand(self.objectName, "addCustomerPreset", parameters)
		except ApiError as e:
			print(e)
	def cmdSetPreset(self, preset):
		try:
			parameters = [preset]
			self.executeCommand(self.objectName, "setPreset", parameters)
		except ApiError as e:
			print(e)
	def cmdSetFilterParam(self, filterParam):
		try:
			parameters = [filterParam]
			self.executeCommand(self.objectName, "setFilterParam", parameters)
		except ApiError as e:
			print(e)
	def cmdSetInterpolationMethod(self, method):
		try:
			parameters = [method]
			self.executeCommand(self.objectName, "setInterpolationMethod", parameters)
		except ApiError as e:
			print(e)
	def cmdSetFilterValues(self, val):
		try:
			parameters = [val]
			self.executeCommand(self.objectName, "setFilterValues", parameters)
		except ApiError as e:
			print(e)
	def cmdSetRescale(self, rescale):
		try:
			parameters = [rescale]
			self.executeCommand(self.objectName, "setRescale", parameters)
		except ApiError as e:
			print(e)
	def cmdSetMaxRescale(self, maxval):
		try:
			parameters = [maxval]
			self.executeCommand(self.objectName, "setMaxRescale", parameters)
		except ApiError as e:
			print(e)
	def cmdSetMinRescale(self, minval):
		try:
			parameters = [minval]
			self.executeCommand(self.objectName, "setMinRescale", parameters)
		except ApiError as e:
			print(e)
	def cmdSetPreGainFunc(self, func):
		try:
			parameters = [func]
			self.executeCommand(self.objectName, "setPreGainFunc", parameters)
		except ApiError as e:
			print(e)
	def cmdSetPostGainFunc(self, func):
		try:
			parameters = [func]
			self.executeCommand(self.objectName, "setPostGainFunc", parameters)
		except ApiError as e:
			print(e)
	def cmdGetPreGainFunc(self):
		try:
			self.executeCommand(self.objectName, "getPreGainFunc")
		except ApiError as e:
			print(e)
	def cmdGetPostGainFunc(self):
		try:
			self.executeCommand(self.objectName, "getPostGainFunc")
		except ApiError as e:
			print(e)
	def cmdSetPaddingFactor(self, factor):
		try:
			parameters = [factor]
			self.executeCommand(self.objectName, "setPaddingFactor", parameters)
		except ApiError as e:
			print(e)
	def cmdSetNumberOfBand(self, nbBand):
		try:
			parameters = [nbBand]
			self.executeCommand(self.objectName, "setNumberOfBand", parameters)
		except ApiError as e:
			print(e)
