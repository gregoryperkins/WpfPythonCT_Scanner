from base import *

class Visionstat(Base):
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
	def cmdSetEnableLive(self):
		try:
			self.executeCommand(self.objectName, "setEnableLive")
		except ApiError as e:
			print(e)
	def cmdRemoveImageInResults(self, image):
		try:
			parameters = [image]
			self.executeCommand(self.objectName, "removeImageInResults", parameters)
		except ApiError as e:
			print(e)
	def cmdProcess(self, image):
		try:
			parameters = [image]
			self.executeCommand(self.objectName, "process", parameters)
		except ApiError as e:
			print(e)
	def cmdLayerUpdated(self):
		try:
			self.executeCommand(self.objectName, "layerUpdated")
		except ApiError as e:
			print(e)
	def cmdRemoveCurrentLayer(self):
		try:
			self.executeCommand(self.objectName, "removeCurrentLayer")
		except ApiError as e:
			print(e)
	def cmdGetMeasure(self, image, measure):
		try:
			parameters = [image, measure]
			self.executeCommand(self.objectName, "getMeasure", parameters)
		except ApiError as e:
			print(e)
	def cmdGetMeasureStr(self, image, measure):
		try:
			parameters = [image, measure]
			self.executeCommand(self.objectName, "getMeasureStr", parameters)
		except ApiError as e:
			print(e)
	def cmdSetMeasurementArea(self, image, p1, p2):
		try:
			parameters = [image, p1, p2]
			self.executeCommand(self.objectName, "setMeasurementArea", parameters)
		except ApiError as e:
			print(e)
	def cmdSetMeasurementArea(self, image, p1, p2):
		try:
			parameters = [image, p1, p2]
			self.executeCommand(self.objectName, "setMeasurementArea", parameters)
		except ApiError as e:
			print(e)
	def cmdLogConnexion(self):
		try:
			self.executeCommand(self.objectName, "logConnexion")
		except ApiError as e:
			print(e)
	def cmdLogConnexionCurrent(self):
		try:
			self.executeCommand(self.objectName, "logConnexionCurrent")
		except ApiError as e:
			print(e)
	def cmdStopLogClick(self):
		try:
			self.executeCommand(self.objectName, "StopLogClick")
		except ApiError as e:
			print(e)
	def cmdStartLogValue(self):
		try:
			self.executeCommand(self.objectName, "startLogValue")
		except ApiError as e:
			print(e)
	def cmdExportCurrentValue(self):
		try:
			self.executeCommand(self.objectName, "exportCurrentValue")
		except ApiError as e:
			print(e)
	def cmdClearViewTable(self):
		try:
			self.executeCommand(self.objectName, "clearViewTable")
		except ApiError as e:
			print(e)
	def cmdUpdateViewTable(self, measures):
		try:
			parameters = [measures]
			self.executeCommand(self.objectName, "updateViewTable", parameters)
		except ApiError as e:
			print(e)
	def cmdOverlayMetaToggled(self, value):
		try:
			parameters = [value]
			self.executeCommand(self.objectName, "overlayMetaToggled", parameters)
		except ApiError as e:
			print(e)
	def cmdLog(self, m):
		try:
			parameters = [m]
			self.executeCommand(self.objectName, "log", parameters)
		except ApiError as e:
			print(e)
	def cmdResetDialogPointer(self, obj):
		try:
			parameters = [obj]
			self.executeCommand(self.objectName, "resetDialogPointer", parameters)
		except ApiError as e:
			print(e)
