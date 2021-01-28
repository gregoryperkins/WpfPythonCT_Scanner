from base import *

class Mesh2Image(Base):
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
	def cmdSetCurrentImageArray(self, obj):
		try:
			parameters = [obj]
			self.executeCommand(self.objectName, "setCurrentImageArray", parameters)
		except ApiError as e:
			print(e)
	def cmdRender(self):
		try:
			self.executeCommand(self.objectName, "render")
		except ApiError as e:
			print(e)
	def cmdFitCurve(self):
		try:
			self.executeCommand(self.objectName, "fitCurve")
		except ApiError as e:
			print(e)
	def cmdExtractMesh(self):
		try:
			self.executeCommand(self.objectName, "extractMesh")
		except ApiError as e:
			print(e)
	def cmdExportStl(self):
		try:
			self.executeCommand(self.objectName, "exportStl")
		except ApiError as e:
			print(e)
	def cmdRemoveMesh(self):
		try:
			self.executeCommand(self.objectName, "removeMesh")
		except ApiError as e:
			print(e)
	def cmdSimplifyMesh(self):
		try:
			self.executeCommand(self.objectName, "simplifyMesh")
		except ApiError as e:
			print(e)
	def cmdSimplifyMeshQuadricMetric(self):
		try:
			self.executeCommand(self.objectName, "simplifyMeshQuadricMetric")
		except ApiError as e:
			print(e)
	def cmdCleanUpMesh(self):
		try:
			self.executeCommand(self.objectName, "cleanUpMesh")
		except ApiError as e:
			print(e)
	def cmdCountVoxels(self):
		try:
			self.executeCommand(self.objectName, "countVoxels")
		except ApiError as e:
			print(e)
	def cmdImagejLikeThreshold(self):
		try:
			self.executeCommand(self.objectName, "imagejLikeThreshold")
		except ApiError as e:
			print(e)
	def cmdUpdateThreshold(self):
		try:
			self.executeCommand(self.objectName, "updateThreshold")
		except ApiError as e:
			print(e)
