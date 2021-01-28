from base import *

class Simpleblend(Base):
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
	def cmdSetFirstImage(self):
		try:
			self.executeCommand(self.objectName, "setFirstImage")
		except ApiError as e:
			print(e)
	def cmdSetSecondImage(self):
		try:
			self.executeCommand(self.objectName, "setSecondImage")
		except ApiError as e:
			print(e)
	def cmdRenderToImage(self):
		try:
			self.executeCommand(self.objectName, "renderToImage")
		except ApiError as e:
			print(e)
	def cmdRenderToFile(self):
		try:
			self.executeCommand(self.objectName, "renderToFile")
		except ApiError as e:
			print(e)
	def cmdRaiseFirst(self):
		try:
			self.executeCommand(self.objectName, "raiseFirst")
		except ApiError as e:
			print(e)
	def cmdRaiseSecond(self):
		try:
			self.executeCommand(self.objectName, "raiseSecond")
		except ApiError as e:
			print(e)
	def cmdRaiseResult(self):
		try:
			self.executeCommand(self.objectName, "raiseResult")
		except ApiError as e:
			print(e)
	def cmdRenderToImagePrivate(self):
		try:
			self.executeCommand(self.objectName, "renderToImagePrivate")
		except ApiError as e:
			print(e)
	def cmdRenderToFilePrivate(self):
		try:
			self.executeCommand(self.objectName, "renderToFilePrivate")
		except ApiError as e:
			print(e)
	def cmdSetCurrentImageArray(self, obj):
		try:
			parameters = [obj]
			self.executeCommand(self.objectName, "setCurrentImageArray", parameters)
		except ApiError as e:
			print(e)
	def cmdShow(self):
		try:
			self.executeCommand(self.objectName, "show")
		except ApiError as e:
			print(e)
	def cmdImageDestroyed(self):
		try:
			self.executeCommand(self.objectName, "imageDestroyed")
		except ApiError as e:
			print(e)
	def cmdViewerDestroyed(self):
		try:
			self.executeCommand(self.objectName, "viewerDestroyed")
		except ApiError as e:
			print(e)
