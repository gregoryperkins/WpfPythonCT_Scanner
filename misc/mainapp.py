from base import *

class Mainapp(Base):
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
	def cmdListOfViewable(self):
		try:
			self.executeCommand(self.objectName, "listOfViewable")
		except ApiError as e:
			print(e)
	def cmdNumberOfImageArrays(self):
		try:
			self.executeCommand(self.objectName, "numberOfImageArrays")
		except ApiError as e:
			print(e)
	def cmdImageArray(self):
		try:
			self.executeCommand(self.objectName, "imageArray")
		except ApiError as e:
			print(e)
	def cmdCurrentImageArray(self):
		try:
			self.executeCommand(self.objectName, "currentImageArray")
		except ApiError as e:
			print(e)
	def cmdCurrentVolume(self):
		try:
			self.executeCommand(self.objectName, "currentVolume")
		except ApiError as e:
			print(e)
	def cmdLoadImageArray(self, path):
		try:
			parameters = [path]
			self.executeCommand(self.objectName, "loadImageArray", parameters)
		except ApiError as e:
			print(e)
	def cmdSaveCurrentImageArray(self, path, prefix):
		try:
			parameters = [path, prefix]
			self.executeCommand(self.objectName, "saveCurrentImageArray", parameters)
		except ApiError as e:
			print(e)
	def cmdExportCurrentImageArray(self, path, format, prefix):
		try:
			parameters = [path, format, prefix]
			self.executeCommand(self.objectName, "exportCurrentImageArray", parameters)
		except ApiError as e:
			print(e)
	def cmdExportCurrentImage(self, path):
		try:
			parameters = [path]
			self.executeCommand(self.objectName, "exportCurrentImage", parameters)
		except ApiError as e:
			print(e)
	def cmdLoadVolume(self, path):
		try:
			parameters = [path]
			self.executeCommand(self.objectName, "loadVolume", parameters)
		except ApiError as e:
			print(e)
	def cmdImportVolume(self, path, slicesDir):
		try:
			parameters = [path, slicesDir]
			self.executeCommand(self.objectName, "importVolume", parameters)
		except ApiError as e:
			print(e)
	def cmdSaveCurrentVolume(self, path):
		try:
			parameters = [path]
			self.executeCommand(self.objectName, "saveCurrentVolume", parameters)
		except ApiError as e:
			print(e)
	def cmdExportCurrentVolume(self, path, dir):
		try:
			parameters = [path, dir]
			self.executeCommand(self.objectName, "exportCurrentVolume", parameters)
		except ApiError as e:
			print(e)
	def cmdSetBlendFunction(self, imageArray, shader):
		try:
			parameters = [imageArray, shader]
			self.executeCommand(self.objectName, "setBlendFunction", parameters)
		except ApiError as e:
			print(e)
	def cmdNewViewer(self):
		try:
			self.executeCommand(self.objectName, "newViewer")
		except ApiError as e:
			print(e)
	def cmdLoadImageArrayPriv(self, imagFiles):
		try:
			parameters = [imagFiles]
			self.executeCommand(self.objectName, "loadImageArrayPriv", parameters)
		except ApiError as e:
			print(e)
	def cmdLoadVolumePriv(self, path):
		try:
			parameters = [path]
			self.executeCommand(self.objectName, "loadVolumePriv", parameters)
		except ApiError as e:
			print(e)
	def cmdImportVolumePriv(self, path, dir):
		try:
			parameters = [path, dir]
			self.executeCommand(self.objectName, "importVolumePriv", parameters)
		except ApiError as e:
			print(e)
