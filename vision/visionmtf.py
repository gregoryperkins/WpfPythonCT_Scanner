from base import *

class Visionmtf(Base):
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
	def cmdMtf(self):
		try:
			self.executeCommand(self.objectName, "mtf")
		except ApiError as e:
			print(e)
	def cmdMtf50(self):
		try:
			self.executeCommand(self.objectName, "mtf50")
		except ApiError as e:
			print(e)
	def cmdMtf10(self):
		try:
			self.executeCommand(self.objectName, "mtf10")
		except ApiError as e:
			print(e)
	def cmdSetCalcWindow(self, tl, br, vw):
		try:
			parameters = [tl, br, vw]
			self.executeCommand(self.objectName, "setCalcWindow", parameters)
		except ApiError as e:
			print(e)
	def cmdSetCalcWindow(self, vtl, vbr, vw):
		try:
			parameters = [vtl, vbr, vw]
			self.executeCommand(self.objectName, "setCalcWindow", parameters)
		except ApiError as e:
			print(e)
	def cmdRemoveCalcWindow(self, im):
		try:
			parameters = [im]
			self.executeCommand(self.objectName, "removeCalcWindow", parameters)
		except ApiError as e:
			print(e)
	def cmdGetTopLeftWindow(self, im):
		try:
			parameters = [im]
			self.executeCommand(self.objectName, "getTopLeftWindow", parameters)
		except ApiError as e:
			print(e)
	def cmdGetBottomRightWindow(self, im):
		try:
			parameters = [im]
			self.executeCommand(self.objectName, "getBottomRightWindow", parameters)
		except ApiError as e:
			print(e)
	def cmdExportSvg(self, filename, widht, height):
		try:
			parameters = [filename, widht, height]
			self.executeCommand(self.objectName, "exportSvg", parameters)
		except ApiError as e:
			print(e)
	def cmdExportCsv(self, filename):
		try:
			parameters = [filename]
			self.executeCommand(self.objectName, "exportCsv", parameters)
		except ApiError as e:
			print(e)
	def cmdDisableMTFOverlay(self):
		try:
			self.executeCommand(self.objectName, "disableMTFOverlay")
		except ApiError as e:
			print(e)
	def cmdUpdateVisionSelection(self, value):
		try:
			parameters = [value]
			self.executeCommand(self.objectName, "updateVisionSelection", parameters)
		except ApiError as e:
			print(e)
	def cmdLayerUpdated(self):
		try:
			self.executeCommand(self.objectName, "layerUpdated")
		except ApiError as e:
			print(e)
	def cmdUpdatePlot(self):
		try:
			self.executeCommand(self.objectName, "updatePlot")
		except ApiError as e:
			print(e)
	def cmdOverlayMetaToggled(self, value):
		try:
			parameters = [value]
			self.executeCommand(self.objectName, "overlayMetaToggled", parameters)
		except ApiError as e:
			print(e)
	def cmdKeepPlot(self):
		try:
			self.executeCommand(self.objectName, "keepPlot")
		except ApiError as e:
			print(e)
	def cmdDivide(self):
		try:
			self.executeCommand(self.objectName, "divide")
		except ApiError as e:
			print(e)
