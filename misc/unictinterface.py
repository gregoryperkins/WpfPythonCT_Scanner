from base import *

class Unictinterface(Base):
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

	def setLoadProjection(self, value):
		try:
			self.setValue(self.objectName, "loadProjection", value)
		except ApiError as e:
			print(e)
	def getLoadProjection(self):
		try:
			return self.getValue(self.objectName, "loadProjection")
		except ApiError as e:
			print(e)

	def setGeometryCorrection(self, value):
		try:
			self.setValue(self.objectName, "geometryCorrection", value)
		except ApiError as e:
			print(e)
	def getGeometryCorrection(self):
		try:
			return self.getValue(self.objectName, "geometryCorrection")
		except ApiError as e:
			print(e)

	def setSpotCorrection(self, value):
		try:
			self.setValue(self.objectName, "spotCorrection", value)
		except ApiError as e:
			print(e)
	def getSpotCorrection(self):
		try:
			return self.getValue(self.objectName, "spotCorrection")
		except ApiError as e:
			print(e)

	def setRecoSliceX(self, value):
		try:
			self.setValue(self.objectName, "recoSliceX", value)
		except ApiError as e:
			print(e)
	def getRecoSliceX(self):
		try:
			return self.getValue(self.objectName, "recoSliceX")
		except ApiError as e:
			print(e)

	def setRecoSliceY(self, value):
		try:
			self.setValue(self.objectName, "recoSliceY", value)
		except ApiError as e:
			print(e)
	def getRecoSliceY(self):
		try:
			return self.getValue(self.objectName, "recoSliceY")
		except ApiError as e:
			print(e)

	def setRecoSliceZ(self, value):
		try:
			self.setValue(self.objectName, "recoSliceZ", value)
		except ApiError as e:
			print(e)
	def getRecoSliceZ(self):
		try:
			return self.getValue(self.objectName, "recoSliceZ")
		except ApiError as e:
			print(e)

	def setRecoVolume(self, value):
		try:
			self.setValue(self.objectName, "recoVolume", value)
		except ApiError as e:
			print(e)
	def getRecoVolume(self):
		try:
			return self.getValue(self.objectName, "recoVolume")
		except ApiError as e:
			print(e)

	def setSliceSubSampling(self, value):
		try:
			self.setValue(self.objectName, "sliceSubSampling", value)
		except ApiError as e:
			print(e)
	def getSliceSubSampling(self):
		try:
			return self.getValue(self.objectName, "sliceSubSampling")
		except ApiError as e:
			print(e)

	def setVoxelSizeX(self, value):
		try:
			self.setValue(self.objectName, "voxelSizeX", value)
		except ApiError as e:
			print(e)
	def getVoxelSizeX(self):
		try:
			return self.getValue(self.objectName, "voxelSizeX")
		except ApiError as e:
			print(e)

	def setVoxelSizeY(self, value):
		try:
			self.setValue(self.objectName, "voxelSizeY", value)
		except ApiError as e:
			print(e)
	def getVoxelSizeY(self):
		try:
			return self.getValue(self.objectName, "voxelSizeY")
		except ApiError as e:
			print(e)

	def setVoxelSizeZ(self, value):
		try:
			self.setValue(self.objectName, "voxelSizeZ", value)
		except ApiError as e:
			print(e)
	def getVoxelSizeZ(self):
		try:
			return self.getValue(self.objectName, "voxelSizeZ")
		except ApiError as e:
			print(e)

	def setVolumeSizeX(self, value):
		try:
			self.setValue(self.objectName, "volumeSizeX", value)
		except ApiError as e:
			print(e)
	def getVolumeSizeX(self):
		try:
			return self.getValue(self.objectName, "volumeSizeX")
		except ApiError as e:
			print(e)

	def setVolumeSizeY(self, value):
		try:
			self.setValue(self.objectName, "volumeSizeY", value)
		except ApiError as e:
			print(e)
	def getVolumeSizeY(self):
		try:
			return self.getValue(self.objectName, "volumeSizeY")
		except ApiError as e:
			print(e)

	def setVolumeSizeZ(self, value):
		try:
			self.setValue(self.objectName, "volumeSizeZ", value)
		except ApiError as e:
			print(e)
	def getVolumeSizeZ(self):
		try:
			return self.getValue(self.objectName, "volumeSizeZ")
		except ApiError as e:
			print(e)

	def setVolumeRotateX(self, value):
		try:
			self.setValue(self.objectName, "volumeRotateX", value)
		except ApiError as e:
			print(e)
	def getVolumeRotateX(self):
		try:
			return self.getValue(self.objectName, "volumeRotateX")
		except ApiError as e:
			print(e)

	def setVolumeRotateY(self, value):
		try:
			self.setValue(self.objectName, "volumeRotateY", value)
		except ApiError as e:
			print(e)
	def getVolumeRotateY(self):
		try:
			return self.getValue(self.objectName, "volumeRotateY")
		except ApiError as e:
			print(e)

	def setVolumeRotateZ(self, value):
		try:
			self.setValue(self.objectName, "volumeRotateZ", value)
		except ApiError as e:
			print(e)
	def getVolumeRotateZ(self):
		try:
			return self.getValue(self.objectName, "volumeRotateZ")
		except ApiError as e:
			print(e)

	def setVolumeOffsetX(self, value):
		try:
			self.setValue(self.objectName, "volumeOffsetX", value)
		except ApiError as e:
			print(e)
	def getVolumeOffsetX(self):
		try:
			return self.getValue(self.objectName, "volumeOffsetX")
		except ApiError as e:
			print(e)

	def setVolumeOffsetY(self, value):
		try:
			self.setValue(self.objectName, "volumeOffsetY", value)
		except ApiError as e:
			print(e)
	def getVolumeOffsetY(self):
		try:
			return self.getValue(self.objectName, "volumeOffsetY")
		except ApiError as e:
			print(e)

	def setVolumeOffsetZ(self, value):
		try:
			self.setValue(self.objectName, "volumeOffsetZ", value)
		except ApiError as e:
			print(e)
	def getVolumeOffsetZ(self):
		try:
			return self.getValue(self.objectName, "volumeOffsetZ")
		except ApiError as e:
			print(e)

	def setTestSliceX(self, value):
		try:
			self.setValue(self.objectName, "testSliceX", value)
		except ApiError as e:
			print(e)
	def getTestSliceX(self):
		try:
			return self.getValue(self.objectName, "testSliceX")
		except ApiError as e:
			print(e)

	def setTestSliceY(self, value):
		try:
			self.setValue(self.objectName, "testSliceY", value)
		except ApiError as e:
			print(e)
	def getTestSliceY(self):
		try:
			return self.getValue(self.objectName, "testSliceY")
		except ApiError as e:
			print(e)

	def setTestSliceZ(self, value):
		try:
			self.setValue(self.objectName, "testSliceZ", value)
		except ApiError as e:
			print(e)
	def getTestSliceZ(self):
		try:
			return self.getValue(self.objectName, "testSliceZ")
		except ApiError as e:
			print(e)

	def setSpotCorrectionOption(self, value):
		try:
			self.setValue(self.objectName, "spotCorrectionOption", value)
		except ApiError as e:
			print(e)
	def getSpotCorrectionOption(self):
		try:
			return self.getValue(self.objectName, "spotCorrectionOption")
		except ApiError as e:
			print(e)

	def setUseCorrectionPerStack(self, value):
		try:
			self.setValue(self.objectName, "useCorrectionPerStack", value)
		except ApiError as e:
			print(e)
	def getUseCorrectionPerStack(self):
		try:
			return self.getValue(self.objectName, "useCorrectionPerStack")
		except ApiError as e:
			print(e)

	def setInterpolateOffsetX(self, value):
		try:
			self.setValue(self.objectName, "interpolateOffsetX", value)
		except ApiError as e:
			print(e)
	def getInterpolateOffsetX(self):
		try:
			return self.getValue(self.objectName, "interpolateOffsetX")
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

	def setOffsetXStack(self, value):
		try:
			self.setValue(self.objectName, "offsetXStack", value)
		except ApiError as e:
			print(e)
	def getOffsetXStack(self):
		try:
			return self.getValue(self.objectName, "offsetXStack")
		except ApiError as e:
			print(e)

	def setTiltZ(self, value):
		try:
			self.setValue(self.objectName, "tiltZ", value)
		except ApiError as e:
			print(e)
	def getTiltZ(self):
		try:
			return self.getValue(self.objectName, "tiltZ")
		except ApiError as e:
			print(e)

	def setTrapezoidX(self, value):
		try:
			self.setValue(self.objectName, "trapezoidX", value)
		except ApiError as e:
			print(e)
	def getTrapezoidX(self):
		try:
			return self.getValue(self.objectName, "trapezoidX")
		except ApiError as e:
			print(e)

	def setTrapezoidY(self, value):
		try:
			self.setValue(self.objectName, "trapezoidY", value)
		except ApiError as e:
			print(e)
	def getTrapezoidY(self):
		try:
			return self.getValue(self.objectName, "trapezoidY")
		except ApiError as e:
			print(e)

	def setAspectRatio(self, value):
		try:
			self.setValue(self.objectName, "aspectRatio", value)
		except ApiError as e:
			print(e)
	def getAspectRatio(self):
		try:
			return self.getValue(self.objectName, "aspectRatio")
		except ApiError as e:
			print(e)

	def setScale(self, value):
		try:
			self.setValue(self.objectName, "scale", value)
		except ApiError as e:
			print(e)
	def getScale(self):
		try:
			return self.getValue(self.objectName, "scale")
		except ApiError as e:
			print(e)

	def setShearing(self, value):
		try:
			self.setValue(self.objectName, "shearing", value)
		except ApiError as e:
			print(e)
	def getShearing(self):
		try:
			return self.getValue(self.objectName, "shearing")
		except ApiError as e:
			print(e)

	def setOffsetXShift(self, value):
		try:
			self.setValue(self.objectName, "offsetXShift", value)
		except ApiError as e:
			print(e)
	def getOffsetXShift(self):
		try:
			return self.getValue(self.objectName, "offsetXShift")
		except ApiError as e:
			print(e)

	def setOffsetYShift(self, value):
		try:
			self.setValue(self.objectName, "offsetYShift", value)
		except ApiError as e:
			print(e)
	def getOffsetYShift(self):
		try:
			return self.getValue(self.objectName, "offsetYShift")
		except ApiError as e:
			print(e)

	def setEnhanceOffsetXCorrection(self, value):
		try:
			self.setValue(self.objectName, "enhanceOffsetXCorrection", value)
		except ApiError as e:
			print(e)
	def getEnhanceOffsetXCorrection(self):
		try:
			return self.getValue(self.objectName, "enhanceOffsetXCorrection")
		except ApiError as e:
			print(e)

	def setEnableRingFilter(self, value):
		try:
			self.setValue(self.objectName, "enableRingFilter", value)
		except ApiError as e:
			print(e)
	def getEnableRingFilter(self):
		try:
			return self.getValue(self.objectName, "enableRingFilter")
		except ApiError as e:
			print(e)

	def setKernelSize(self, value):
		try:
			self.setValue(self.objectName, "kernelSize", value)
		except ApiError as e:
			print(e)
	def getKernelSize(self):
		try:
			return self.getValue(self.objectName, "kernelSize")
		except ApiError as e:
			print(e)

	def setFalseDetectionLevel(self, value):
		try:
			self.setValue(self.objectName, "falseDetectionLevel", value)
		except ApiError as e:
			print(e)
	def getFalseDetectionLevel(self):
		try:
			return self.getValue(self.objectName, "falseDetectionLevel")
		except ApiError as e:
			print(e)

	def setEnableBadPixelFilter(self, value):
		try:
			self.setValue(self.objectName, "enableBadPixelFilter", value)
		except ApiError as e:
			print(e)
	def getEnableBadPixelFilter(self):
		try:
			return self.getValue(self.objectName, "enableBadPixelFilter")
		except ApiError as e:
			print(e)

	def setReplaceDefect(self, value):
		try:
			self.setValue(self.objectName, "replaceDefect", value)
		except ApiError as e:
			print(e)
	def getReplaceDefect(self):
		try:
			return self.getValue(self.objectName, "replaceDefect")
		except ApiError as e:
			print(e)

	def setReplaceNoisy(self, value):
		try:
			self.setValue(self.objectName, "replaceNoisy", value)
		except ApiError as e:
			print(e)
	def getReplaceNoisy(self):
		try:
			return self.getValue(self.objectName, "replaceNoisy")
		except ApiError as e:
			print(e)

	def setCorrectionPerTurn(self, value):
		try:
			self.setValue(self.objectName, "correctionPerTurn", value)
		except ApiError as e:
			print(e)
	def getCorrectionPerTurn(self):
		try:
			return self.getValue(self.objectName, "correctionPerTurn")
		except ApiError as e:
			print(e)

	def getBeamProfileList(self):
		try:
			return self.getValue(self.objectName, "beamProfileList")
		except ApiError as e:
			print(e)

	def setBeamProfile(self, value):
		try:
			self.setValue(self.objectName, "beamProfile", value)
		except ApiError as e:
			print(e)
	def getBeamProfile(self):
		try:
			return self.getValue(self.objectName, "beamProfile")
		except ApiError as e:
			print(e)

	def setProjectionsStartIndex(self, value):
		try:
			self.setValue(self.objectName, "projectionsStartIndex", value)
		except ApiError as e:
			print(e)
	def getProjectionsStartIndex(self):
		try:
			return self.getValue(self.objectName, "projectionsStartIndex")
		except ApiError as e:
			print(e)

	def setProjectionsEndIndex(self, value):
		try:
			self.setValue(self.objectName, "projectionsEndIndex", value)
		except ApiError as e:
			print(e)
	def getProjectionsEndIndex(self):
		try:
			return self.getValue(self.objectName, "projectionsEndIndex")
		except ApiError as e:
			print(e)

	def setProjectionsStep(self, value):
		try:
			self.setValue(self.objectName, "projectionsStep", value)
		except ApiError as e:
			print(e)
	def getProjectionsStep(self):
		try:
			return self.getValue(self.objectName, "projectionsStep")
		except ApiError as e:
			print(e)

	def getProjectionsTotal(self):
		try:
			return self.getValue(self.objectName, "projectionsTotal")
		except ApiError as e:
			print(e)

	def setEnableLimitedAngle(self, value):
		try:
			self.setValue(self.objectName, "enableLimitedAngle", value)
		except ApiError as e:
			print(e)
	def getEnableLimitedAngle(self):
		try:
			return self.getValue(self.objectName, "enableLimitedAngle")
		except ApiError as e:
			print(e)

	def setProjectionsCropLeft(self, value):
		try:
			self.setValue(self.objectName, "projectionsCropLeft", value)
		except ApiError as e:
			print(e)
	def getProjectionsCropLeft(self):
		try:
			return self.getValue(self.objectName, "projectionsCropLeft")
		except ApiError as e:
			print(e)

	def setProjectionsCropRight(self, value):
		try:
			self.setValue(self.objectName, "projectionsCropRight", value)
		except ApiError as e:
			print(e)
	def getProjectionsCropRight(self):
		try:
			return self.getValue(self.objectName, "projectionsCropRight")
		except ApiError as e:
			print(e)

	def setEnablePhaseContrast(self, value):
		try:
			self.setValue(self.objectName, "enablePhaseContrast", value)
		except ApiError as e:
			print(e)
	def getEnablePhaseContrast(self):
		try:
			return self.getValue(self.objectName, "enablePhaseContrast")
		except ApiError as e:
			print(e)

	def setPhaseContrastValue(self, value):
		try:
			self.setValue(self.objectName, "phaseContrastValue", value)
		except ApiError as e:
			print(e)
	def getPhaseContrastValue(self):
		try:
			return self.getValue(self.objectName, "phaseContrastValue")
		except ApiError as e:
			print(e)

	def setReconstructionMethod(self, value):
		try:
			self.setValue(self.objectName, "reconstructionMethod", value)
		except ApiError as e:
			print(e)
	def getReconstructionMethod(self):
		try:
			return self.getValue(self.objectName, "reconstructionMethod")
		except ApiError as e:
			print(e)

	def setNoiseFilter(self, value):
		try:
			self.setValue(self.objectName, "noiseFilter", value)
		except ApiError as e:
			print(e)
	def getNoiseFilter(self):
		try:
			return self.getValue(self.objectName, "noiseFilter")
		except ApiError as e:
			print(e)

	def setNoiseFilterMethod(self, value):
		try:
			self.setValue(self.objectName, "noiseFilterMethod", value)
		except ApiError as e:
			print(e)
	def getNoiseFilterMethod(self):
		try:
			return self.getValue(self.objectName, "noiseFilterMethod")
		except ApiError as e:
			print(e)

	def setBorderFilter(self, value):
		try:
			self.setValue(self.objectName, "borderFilter", value)
		except ApiError as e:
			print(e)
	def getBorderFilter(self):
		try:
			return self.getValue(self.objectName, "borderFilter")
		except ApiError as e:
			print(e)

	def setBorderFilterMethod(self, value):
		try:
			self.setValue(self.objectName, "borderFilterMethod", value)
		except ApiError as e:
			print(e)
	def getBorderFilterMethod(self):
		try:
			return self.getValue(self.objectName, "borderFilterMethod")
		except ApiError as e:
			print(e)

	def setVerticalBorderFilter(self, value):
		try:
			self.setValue(self.objectName, "verticalBorderFilter", value)
		except ApiError as e:
			print(e)
	def getVerticalBorderFilter(self):
		try:
			return self.getValue(self.objectName, "verticalBorderFilter")
		except ApiError as e:
			print(e)

	def setHorizontalBorderFilter(self, value):
		try:
			self.setValue(self.objectName, "horizontalBorderFilter", value)
		except ApiError as e:
			print(e)
	def getHorizontalBorderFilter(self):
		try:
			return self.getValue(self.objectName, "horizontalBorderFilter")
		except ApiError as e:
			print(e)

	def setEnableContrast(self, value):
		try:
			self.setValue(self.objectName, "enableContrast", value)
		except ApiError as e:
			print(e)
	def getEnableContrast(self):
		try:
			return self.getValue(self.objectName, "enableContrast")
		except ApiError as e:
			print(e)

	def setMinContrast(self, value):
		try:
			self.setValue(self.objectName, "minContrast", value)
		except ApiError as e:
			print(e)
	def getMinContrast(self):
		try:
			return self.getValue(self.objectName, "minContrast")
		except ApiError as e:
			print(e)

	def setMaxContrast(self, value):
		try:
			self.setValue(self.objectName, "maxContrast", value)
		except ApiError as e:
			print(e)
	def getMaxContrast(self):
		try:
			return self.getValue(self.objectName, "maxContrast")
		except ApiError as e:
			print(e)

	def setSaveOptionEnableX(self, value):
		try:
			self.setValue(self.objectName, "saveOptionEnableX", value)
		except ApiError as e:
			print(e)
	def getSaveOptionEnableX(self):
		try:
			return self.getValue(self.objectName, "saveOptionEnableX")
		except ApiError as e:
			print(e)

	def setSaveOptionEnableY(self, value):
		try:
			self.setValue(self.objectName, "saveOptionEnableY", value)
		except ApiError as e:
			print(e)
	def getSaveOptionEnableY(self):
		try:
			return self.getValue(self.objectName, "saveOptionEnableY")
		except ApiError as e:
			print(e)

	def setSaveOptionEnableZ(self, value):
		try:
			self.setValue(self.objectName, "saveOptionEnableZ", value)
		except ApiError as e:
			print(e)
	def getSaveOptionEnableZ(self):
		try:
			return self.getValue(self.objectName, "saveOptionEnableZ")
		except ApiError as e:
			print(e)

	def setSaveOptionFormatX(self, value):
		try:
			self.setValue(self.objectName, "saveOptionFormatX", value)
		except ApiError as e:
			print(e)
	def getSaveOptionFormatX(self):
		try:
			return self.getValue(self.objectName, "saveOptionFormatX")
		except ApiError as e:
			print(e)

	def setSaveOptionFormatY(self, value):
		try:
			self.setValue(self.objectName, "saveOptionFormatY", value)
		except ApiError as e:
			print(e)
	def getSaveOptionFormatY(self):
		try:
			return self.getValue(self.objectName, "saveOptionFormatY")
		except ApiError as e:
			print(e)

	def setSaveOptionFormatZ(self, value):
		try:
			self.setValue(self.objectName, "saveOptionFormatZ", value)
		except ApiError as e:
			print(e)
	def getSaveOptionFormatZ(self):
		try:
			return self.getValue(self.objectName, "saveOptionFormatZ")
		except ApiError as e:
			print(e)

	def setExportRaw(self, value):
		try:
			self.setValue(self.objectName, "exportRaw", value)
		except ApiError as e:
			print(e)
	def getExportRaw(self):
		try:
			return self.getValue(self.objectName, "exportRaw")
		except ApiError as e:
			print(e)

	def setExportStl(self, value):
		try:
			self.setValue(self.objectName, "exportStl", value)
		except ApiError as e:
			print(e)
	def getExportStl(self):
		try:
			return self.getValue(self.objectName, "exportStl")
		except ApiError as e:
			print(e)

	def setExportVg(self, value):
		try:
			self.setValue(self.objectName, "exportVg", value)
		except ApiError as e:
			print(e)
	def getExportVg(self):
		try:
			return self.getValue(self.objectName, "exportVg")
		except ApiError as e:
			print(e)

	def getProjectPath(self):
		try:
			return self.getValue(self.objectName, "projectPath")
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
	def cmdSetTestInterface(self, testInterface):
		try:
			parameters = [testInterface]
			self.executeCommand(self.objectName, "setTestInterface", parameters)
		except ApiError as e:
			print(e)
	def cmdProjectLoadingFinished(self):
		try:
			self.executeCommand(self.objectName, "projectLoadingFinished")
		except ApiError as e:
			print(e)
	def cmdReconstructionFinished(self):
		try:
			self.executeCommand(self.objectName, "reconstructionFinished")
		except ApiError as e:
			print(e)
	def cmdSpotFinished(self):
		try:
			self.executeCommand(self.objectName, "spotFinished")
		except ApiError as e:
			print(e)
	def cmdGeometryCorrectionFinished(self):
		try:
			self.executeCommand(self.objectName, "geometryCorrectionFinished")
		except ApiError as e:
			print(e)
	def cmdBeamSelectionFinished(self):
		try:
			self.executeCommand(self.objectName, "beamSelectionFinished")
		except ApiError as e:
			print(e)
	def cmdLoadProject(self, path):
		try:
			parameters = [path]
			self.executeCommand(self.objectName, "loadProject", parameters)
		except ApiError as e:
			print(e)
	def cmdCloseProject(self, askToSave):
		try:
			parameters = [askToSave]
			self.executeCommand(self.objectName, "closeProject", parameters)
		except ApiError as e:
			print(e)
	def cmdStartTestSlice(self, dir):
		try:
			parameters = [dir]
			self.executeCommand(self.objectName, "startTestSlice", parameters)
		except ApiError as e:
			print(e)
	def cmdStartAutomaticGeometryCorrection(self):
		try:
			self.executeCommand(self.objectName, "startAutomaticGeometryCorrection")
		except ApiError as e:
			print(e)
	def cmdStartVolumeReconstrution(self):
		try:
			self.executeCommand(self.objectName, "startVolumeReconstrution")
		except ApiError as e:
			print(e)
	def cmdCloseAllSubWindows(self):
		try:
			self.executeCommand(self.objectName, "closeAllSubWindows")
		except ApiError as e:
			print(e)
	def cmdStartSpotCorrelation(self):
		try:
			self.executeCommand(self.objectName, "startSpotCorrelation")
		except ApiError as e:
			print(e)
	def cmdStartBeamProfileSelection(self, dir):
		try:
			parameters = [dir]
			self.executeCommand(self.objectName, "startBeamProfileSelection", parameters)
		except ApiError as e:
			print(e)
	def cmdCancelOperation(self):
		try:
			self.executeCommand(self.objectName, "cancelOperation")
		except ApiError as e:
			print(e)
	def cmdAddBeamProfile(self, value):
		try:
			parameters = [value]
			self.executeCommand(self.objectName, "addBeamProfile", parameters)
		except ApiError as e:
			print(e)
	def cmdInitError(self, error):
		try:
			parameters = [error]
			self.executeCommand(self.objectName, "initError", parameters)
		except ApiError as e:
			print(e)
