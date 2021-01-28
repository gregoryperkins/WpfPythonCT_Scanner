from base import *

class Demo(Base):
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

	def setRmMode(self, value):
		try:
			self.setValue(self.objectName, "rmMode", value)
		except ApiError as e:
			print(e)
	def getRmMode(self):
		try:
			return self.getValue(self.objectName, "rmMode")
		except ApiError as e:
			print(e)

	def getRmModeList(self):
		try:
			return self.getValue(self.objectName, "rmModeList")
		except ApiError as e:
			print(e)

	def setAvrFrames(self, value):
		try:
			self.setValue(self.objectName, "avrFrames", value)
		except ApiError as e:
			print(e)
	def getAvrFrames(self):
		try:
			return self.getValue(self.objectName, "avrFrames")
		except ApiError as e:
			print(e)

	def setNoAvrOnMove(self, value):
		try:
			self.setValue(self.objectName, "noAvrOnMove", value)
		except ApiError as e:
			print(e)
	def getNoAvrOnMove(self):
		try:
			return self.getValue(self.objectName, "noAvrOnMove")
		except ApiError as e:
			print(e)

	def setLookUpTableData(self, value):
		try:
			self.setValue(self.objectName, "lookUpTableData", value)
		except ApiError as e:
			print(e)
	def getLookUpTableData(self):
		try:
			return self.getValue(self.objectName, "lookUpTableData")
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

	def setRingBufferSize(self, value):
		try:
			self.setValue(self.objectName, "ringBufferSize", value)
		except ApiError as e:
			print(e)
	def getRingBufferSize(self):
		try:
			return self.getValue(self.objectName, "ringBufferSize")
		except ApiError as e:
			print(e)

	def setRingBufferIndex(self, value):
		try:
			self.setValue(self.objectName, "ringBufferIndex", value)
		except ApiError as e:
			print(e)
	def getRingBufferIndex(self):
		try:
			return self.getValue(self.objectName, "ringBufferIndex")
		except ApiError as e:
			print(e)

	def setRingBufferOn(self, value):
		try:
			self.setValue(self.objectName, "ringBufferOn", value)
		except ApiError as e:
			print(e)
	def getRingBufferOn(self):
		try:
			return self.getValue(self.objectName, "ringBufferOn")
		except ApiError as e:
			print(e)

	def getPixelWidth(self):
		try:
			return self.getValue(self.objectName, "pixelWidth")
		except ApiError as e:
			print(e)

	def getPixelHeight(self):
		try:
			return self.getValue(self.objectName, "pixelHeight")
		except ApiError as e:
			print(e)

	def setTemporalFilter(self, value):
		try:
			self.setValue(self.objectName, "temporalFilter", value)
		except ApiError as e:
			print(e)
	def getTemporalFilter(self):
		try:
			return self.getValue(self.objectName, "temporalFilter")
		except ApiError as e:
			print(e)

	def getOrientation(self):
		try:
			return self.getValue(self.objectName, "orientation")
		except ApiError as e:
			print(e)

	def getOverExposed(self):
		try:
			return self.getValue(self.objectName, "overExposed")
		except ApiError as e:
			print(e)

	def setNumOfCalFrames(self, value):
		try:
			self.setValue(self.objectName, "numOfCalFrames", value)
		except ApiError as e:
			print(e)
	def getNumOfCalFrames(self):
		try:
			return self.getValue(self.objectName, "numOfCalFrames")
		except ApiError as e:
			print(e)

	def setDigitalGain(self, value):
		try:
			self.setValue(self.objectName, "digitalGain", value)
		except ApiError as e:
			print(e)
	def getDigitalGain(self):
		try:
			return self.getValue(self.objectName, "digitalGain")
		except ApiError as e:
			print(e)

	def setCalibrationSlot(self, value):
		try:
			self.setValue(self.objectName, "calibrationSlot", value)
		except ApiError as e:
			print(e)
	def getCalibrationSlot(self):
		try:
			return self.getValue(self.objectName, "calibrationSlot")
		except ApiError as e:
			print(e)

	def getCalibrationPoints(self):
		try:
			return self.getValue(self.objectName, "calibrationPoints")
		except ApiError as e:
			print(e)

	def getNeedsBlackImage(self):
		try:
			return self.getValue(self.objectName, "needsBlackImage")
		except ApiError as e:
			print(e)

	def getNeedsGainImage(self):
		try:
			return self.getValue(self.objectName, "needsGainImage")
		except ApiError as e:
			print(e)

	def getSupportsAlign(self):
		try:
			return self.getValue(self.objectName, "supportsAlign")
		except ApiError as e:
			print(e)

	def setOffsetX(self, value):
		try:
			self.setValue(self.objectName, "offsetX", value)
		except ApiError as e:
			print(e)
	def getOffsetX(self):
		try:
			return self.getValue(self.objectName, "offsetX")
		except ApiError as e:
			print(e)

	def setOffsetY(self, value):
		try:
			self.setValue(self.objectName, "offsetY", value)
		except ApiError as e:
			print(e)
	def getOffsetY(self):
		try:
			return self.getValue(self.objectName, "offsetY")
		except ApiError as e:
			print(e)

	def setAlignToXRay(self, value):
		try:
			self.setValue(self.objectName, "alignToXRay", value)
		except ApiError as e:
			print(e)
	def getAlignToXRay(self):
		try:
			return self.getValue(self.objectName, "alignToXRay")
		except ApiError as e:
			print(e)

	def setShiftWidth(self, value):
		try:
			self.setValue(self.objectName, "shiftWidth", value)
		except ApiError as e:
			print(e)
	def getShiftWidth(self):
		try:
			return self.getValue(self.objectName, "shiftWidth")
		except ApiError as e:
			print(e)

	def setShiftHeight(self, value):
		try:
			self.setValue(self.objectName, "shiftHeight", value)
		except ApiError as e:
			print(e)
	def getShiftHeight(self):
		try:
			return self.getValue(self.objectName, "shiftHeight")
		except ApiError as e:
			print(e)

	def setShiftX(self, value):
		try:
			self.setValue(self.objectName, "shiftX", value)
		except ApiError as e:
			print(e)
	def getShiftX(self):
		try:
			return self.getValue(self.objectName, "shiftX")
		except ApiError as e:
			print(e)

	def setShiftY(self, value):
		try:
			self.setValue(self.objectName, "shiftY", value)
		except ApiError as e:
			print(e)
	def getShiftY(self):
		try:
			return self.getValue(self.objectName, "shiftY")
		except ApiError as e:
			print(e)

	def setMargin(self, value):
		try:
			self.setValue(self.objectName, "margin", value)
		except ApiError as e:
			print(e)
	def getMargin(self):
		try:
			return self.getValue(self.objectName, "margin")
		except ApiError as e:
			print(e)

	def setFramerate(self, value):
		try:
			self.setValue(self.objectName, "framerate", value)
		except ApiError as e:
			print(e)
	def getFramerate(self):
		try:
			return self.getValue(self.objectName, "framerate")
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
	def cmdSetXraySource(self, xray):
		try:
			parameters = [xray]
			self.executeCommand(self.objectName, "setXraySource", parameters)
		except ApiError as e:
			print(e)
	def cmdOpen(self):
		try:
			self.executeCommand(self.objectName, "open")
		except ApiError as e:
			print(e)
	def cmdClose(self):
		try:
			self.executeCommand(self.objectName, "close")
		except ApiError as e:
			print(e)
	def cmdStart(self):
		try:
			self.executeCommand(self.objectName, "start")
		except ApiError as e:
			print(e)
	def cmdStop(self):
		try:
			self.executeCommand(self.objectName, "stop")
		except ApiError as e:
			print(e)
	def cmdSnapshot(self, numOfSummedFrames):
		try:
			parameters = [numOfSummedFrames]
			self.executeCommand(self.objectName, "snapshot", parameters)
		except ApiError as e:
			print(e)
	def cmdFlush(self):
		try:
			self.executeCommand(self.objectName, "flush")
		except ApiError as e:
			print(e)
	def cmdSaveImage(self, path):
		try:
			parameters = [path]
			self.executeCommand(self.objectName, "saveImage", parameters)
		except ApiError as e:
			print(e)
	def cmdOverrideCopyParameter(self, offsetX, offsetY, border, stitchMask):
		try:
			parameters = [offsetX, offsetY, border, stitchMask]
			self.executeCommand(self.objectName, "overrideCopyParameter", parameters)
		except ApiError as e:
			print(e)
	def cmdRmModeRemap(self, i, v):
		try:
			parameters = [i, v]
			self.executeCommand(self.objectName, "rmModeRemap", parameters)
		except ApiError as e:
			print(e)
	def cmdSetSphereDetectionThreshold(self, v):
		try:
			parameters = [v]
			self.executeCommand(self.objectName, "setSphereDetectionThreshold", parameters)
		except ApiError as e:
			print(e)
	def cmdSetMotionTolerance(self, t):
		try:
			parameters = [t]
			self.executeCommand(self.objectName, "setMotionTolerance", parameters)
		except ApiError as e:
			print(e)
	def cmdSetOrientation(self, x, y, z, w):
		try:
			parameters = [x, y, z, w]
			self.executeCommand(self.objectName, "setOrientation", parameters)
		except ApiError as e:
			print(e)
	def cmdAutoExposure(self):
		try:
			self.executeCommand(self.objectName, "autoExposure")
		except ApiError as e:
			print(e)
	def cmdAutoExposureSimu(self):
		try:
			self.executeCommand(self.objectName, "autoExposureSimu")
		except ApiError as e:
			print(e)
	def cmdSetMountingOrientation(self):
		try:
			self.executeCommand(self.objectName, "setMountingOrientation")
		except ApiError as e:
			print(e)
	def cmdSaveSettings(self):
		try:
			self.executeCommand(self.objectName, "saveSettings")
		except ApiError as e:
			print(e)
	def cmdAbstractImagerGuiDestroyed(self):
		try:
			self.executeCommand(self.objectName, "abstractImagerGuiDestroyed")
		except ApiError as e:
			print(e)
	def cmdSetRmMode(self, mode):
		try:
			parameters = [mode]
			self.executeCommand(self.objectName, "setRmMode", parameters)
		except ApiError as e:
			print(e)
	def cmdSetAvrFrames(self, avr):
		try:
			parameters = [avr]
			self.executeCommand(self.objectName, "setAvrFrames", parameters)
		except ApiError as e:
			print(e)
	def cmdApplyAutoExposure(self):
		try:
			self.executeCommand(self.objectName, "applyAutoExposure")
		except ApiError as e:
			print(e)
	def cmdSetNoAvrOnMove(self, noAvr):
		try:
			parameters = [noAvr]
			self.executeCommand(self.objectName, "setNoAvrOnMove", parameters)
		except ApiError as e:
			print(e)
	def cmdSetLookUpTableData(self, lut):
		try:
			parameters = [lut]
			self.executeCommand(self.objectName, "setLookUpTableData", parameters)
		except ApiError as e:
			print(e)
	def cmdSetFilter(self, filter):
		try:
			parameters = [filter]
			self.executeCommand(self.objectName, "setFilter", parameters)
		except ApiError as e:
			print(e)
	def cmdDestroy(self):
		try:
			self.executeCommand(self.objectName, "destroy")
		except ApiError as e:
			print(e)
	def cmdCalibratedImagerGuiDestroyed(self):
		try:
			self.executeCommand(self.objectName, "calibratedImagerGuiDestroyed")
		except ApiError as e:
			print(e)
	def cmdReloadCalibration(self):
		try:
			self.executeCommand(self.objectName, "reloadCalibration")
		except ApiError as e:
			print(e)
	def cmdBlackImage(self):
		try:
			self.executeCommand(self.objectName, "blackImage")
		except ApiError as e:
			print(e)
	def cmdGainImage(self):
		try:
			self.executeCommand(self.objectName, "gainImage")
		except ApiError as e:
			print(e)
	def cmdAddGainImage(self):
		try:
			self.executeCommand(self.objectName, "addGainImage")
		except ApiError as e:
			print(e)
	def cmdExportDefectPixelmap(self, filename, includeDetectedPixels):
		try:
			parameters = [filename, includeDetectedPixels]
			self.executeCommand(self.objectName, "exportDefectPixelmap", parameters)
		except ApiError as e:
			print(e)
	def cmdImportDefectPixelmap(self, filename):
		try:
			parameters = [filename]
			self.executeCommand(self.objectName, "importDefectPixelmap", parameters)
		except ApiError as e:
			print(e)
	def cmdMaxCalibrationDerivation(self, black, gain, saveToConfig):
		try:
			parameters = [black, gain, saveToConfig]
			self.executeCommand(self.objectName, "maxCalibrationDerivation", parameters)
		except ApiError as e:
			print(e)
	def cmdLoadDistortionMap(self, path):
		try:
			parameters = [path]
			self.executeCommand(self.objectName, "loadDistortionMap", parameters)
		except ApiError as e:
			print(e)
	def cmdSetLevelTriggerParameter(self, averageLevel, minMaxLevel, singleTileLevel, requiredTiles, totalNumOfTiles):
		try:
			parameters = [averageLevel, minMaxLevel, singleTileLevel, requiredTiles, totalNumOfTiles]
			self.executeCommand(self.objectName, "setLevelTriggerParameter", parameters)
		except ApiError as e:
			print(e)
	def cmdSetLevelTrigger(self, enabled):
		try:
			parameters = [enabled]
			self.executeCommand(self.objectName, "setLevelTrigger", parameters)
		except ApiError as e:
			print(e)
	def cmdSearchHotPixelInRawImage(self):
		try:
			self.executeCommand(self.objectName, "searchHotPixelInRawImage")
		except ApiError as e:
			print(e)
	def cmdDisplayDefectPixels(self, checked):
		try:
			parameters = [checked]
			self.executeCommand(self.objectName, "displayDefectPixels", parameters)
		except ApiError as e:
			print(e)
	def cmdDisableCorrection(self):
		try:
			self.executeCommand(self.objectName, "disableCorrection")
		except ApiError as e:
			print(e)
	def cmdEnableCorrection(self):
		try:
			self.executeCommand(self.objectName, "enableCorrection")
		except ApiError as e:
			print(e)
	def cmdSetNumOfCalFrames(self, frames):
		try:
			parameters = [frames]
			self.executeCommand(self.objectName, "setNumOfCalFrames", parameters)
		except ApiError as e:
			print(e)
	def cmdSetDigitalGain(self, digitalGain):
		try:
			parameters = [digitalGain]
			self.executeCommand(self.objectName, "setDigitalGain", parameters)
		except ApiError as e:
			print(e)
	def cmdProgress2(self):
		try:
			self.executeCommand(self.objectName, "progress2")
		except ApiError as e:
			print(e)
	def cmdSetBlackImageStatus(self):
		try:
			self.executeCommand(self.objectName, "setBlackImageStatus")
		except ApiError as e:
			print(e)
	def cmdSetGainImageStatus(self):
		try:
			self.executeCommand(self.objectName, "setGainImageStatus")
		except ApiError as e:
			print(e)
	def cmdSetWaitForAxisReadyDisabled(self, disabled):
		try:
			parameters = [disabled]
			self.executeCommand(self.objectName, "setWaitForAxisReadyDisabled", parameters)
		except ApiError as e:
			print(e)
	def cmdSetAlignToXRay(self, a):
		try:
			parameters = [a]
			self.executeCommand(self.objectName, "setAlignToXRay", parameters)
		except ApiError as e:
			print(e)
	def cmdAxisMoved(self):
		try:
			self.executeCommand(self.objectName, "axisMoved")
		except ApiError as e:
			print(e)
	def cmdAxisBusyClear(self):
		try:
			self.executeCommand(self.objectName, "axisBusyClear")
		except ApiError as e:
			print(e)
	def cmdFlatPanelImagerGuiDestroyed(self):
		try:
			self.executeCommand(self.objectName, "flatPanelImagerGuiDestroyed")
		except ApiError as e:
			print(e)
	def cmdSnapshotAll(self, numOfImages):
		try:
			parameters = [numOfImages]
			self.executeCommand(self.objectName, "snapshotAll", parameters)
		except ApiError as e:
			print(e)
	def cmdTiltAngles(self):
		try:
			self.executeCommand(self.objectName, "tiltAngles")
		except ApiError as e:
			print(e)
	def cmdSetOverlap(self, x, y):
		try:
			parameters = [x, y]
			self.executeCommand(self.objectName, "setOverlap", parameters)
		except ApiError as e:
			print(e)
	def cmdSetImageInput(self, path, snapshotOnly):
		try:
			parameters = [path, snapshotOnly]
			self.executeCommand(self.objectName, "setImageInput", parameters)
		except ApiError as e:
			print(e)
	def cmdSetBinning(self, binning):
		try:
			parameters = [binning]
			self.executeCommand(self.objectName, "setBinning", parameters)
		except ApiError as e:
			print(e)
	def cmdAddSphere(self, sample):
		try:
			parameters = [sample]
			self.executeCommand(self.objectName, "addSphere", parameters)
		except ApiError as e:
			print(e)
	def cmdClearSpheres(self, sample):
		try:
			parameters = [sample]
			self.executeCommand(self.objectName, "clearSpheres", parameters)
		except ApiError as e:
			print(e)
	def cmdSetSTL(self, path):
		try:
			parameters = [path]
			self.executeCommand(self.objectName, "setSTL", parameters)
		except ApiError as e:
			print(e)
	def cmdSetBlur(self):
		try:
			self.executeCommand(self.objectName, "setBlur")
		except ApiError as e:
			print(e)
	def cmdSetCustomProjctionMatrix(self, mat):
		try:
			parameters = [mat]
			self.executeCommand(self.objectName, "setCustomProjctionMatrix", parameters)
		except ApiError as e:
			print(e)
	def cmdSetScatter(self):
		try:
			self.executeCommand(self.objectName, "setScatter")
		except ApiError as e:
			print(e)
	def cmdDistortionPoints(self):
		try:
			self.executeCommand(self.objectName, "distortionPoints")
		except ApiError as e:
			print(e)
	def cmdSetDistortionPoints(self, list):
		try:
			parameters = [list]
			self.executeCommand(self.objectName, "setDistortionPoints", parameters)
		except ApiError as e:
			print(e)
	def cmdExtractDistortionPoints(self):
		try:
			self.executeCommand(self.objectName, "extractDistortionPoints")
		except ApiError as e:
			print(e)
	def cmdSetDistortionParameter(self, horizontalStep, verticalStep, shearing):
		try:
			parameters = [horizontalStep, verticalStep, shearing]
			self.executeCommand(self.objectName, "setDistortionParameter", parameters)
		except ApiError as e:
			print(e)
	def cmdSetPixelSize(self, pixSizeX, pixSizeY):
		try:
			parameters = [pixSizeX, pixSizeY]
			self.executeCommand(self.objectName, "setPixelSize", parameters)
		except ApiError as e:
			print(e)
	def cmdGuiDestroyed(self):
		try:
			self.executeCommand(self.objectName, "guiDestroyed")
		except ApiError as e:
			print(e)
	def cmdSetFramerate(self):
		try:
			self.executeCommand(self.objectName, "setFramerate")
		except ApiError as e:
			print(e)
