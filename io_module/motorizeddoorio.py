from base import *

class Motorizeddoorio(Base):
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
	def cmdSetOutput(self, number, value):
		try:
			parameters = [number, value]
			self.executeCommand(self.objectName, "setOutput", parameters)
		except ApiError as e:
			print(e)
	def cmdGetOutput(self, number):
		try:
			parameters = [number]
			self.executeCommand(self.objectName, "getOutput", parameters)
		except ApiError as e:
			print(e)
	def cmdGetInput(self, number):
		try:
			parameters = [number]
			self.executeCommand(self.objectName, "getInput", parameters)
		except ApiError as e:
			print(e)
	def cmdSetOutputEnabled(self, number, enableOut):
		try:
			parameters = [number, enableOut]
			self.executeCommand(self.objectName, "setOutputEnabled", parameters)
		except ApiError as e:
			print(e)
	def cmdGetOutputEnabled(self, number):
		try:
			parameters = [number]
			self.executeCommand(self.objectName, "getOutputEnabled", parameters)
		except ApiError as e:
			print(e)
	def cmdNumOfInOut(self):
		try:
			self.executeCommand(self.objectName, "numOfInOut")
		except ApiError as e:
			print(e)
	def cmdNumOfIntput(self):
		try:
			self.executeCommand(self.objectName, "numOfIntput")
		except ApiError as e:
			print(e)
	def cmdNumOfOutput(self):
		try:
			self.executeCommand(self.objectName, "numOfOutput")
		except ApiError as e:
			print(e)
	def cmdGetAnalogInput(self, number):
		try:
			parameters = [number]
			self.executeCommand(self.objectName, "getAnalogInput", parameters)
		except ApiError as e:
			print(e)
	def cmdSetAnalogOutput(self, number, value):
		try:
			parameters = [number, value]
			self.executeCommand(self.objectName, "setAnalogOutput", parameters)
		except ApiError as e:
			print(e)
	def cmdGetAnalogOutput(self, number):
		try:
			parameters = [number]
			self.executeCommand(self.objectName, "getAnalogOutput", parameters)
		except ApiError as e:
			print(e)
	def cmdNumOfAnalogInput(self):
		try:
			self.executeCommand(self.objectName, "numOfAnalogInput")
		except ApiError as e:
			print(e)
	def cmdNumOfAnalogOutput(self):
		try:
			self.executeCommand(self.objectName, "numOfAnalogOutput")
		except ApiError as e:
			print(e)
	def cmdOpenDoor(self):
		try:
			self.executeCommand(self.objectName, "openDoor")
		except ApiError as e:
			print(e)
	def cmdCloseDoor(self):
		try:
			self.executeCommand(self.objectName, "closeDoor")
		except ApiError as e:
			print(e)
	def cmdCancel(self):
		try:
			self.executeCommand(self.objectName, "cancel")
		except ApiError as e:
			print(e)
	def cmdGetState(self):
		try:
			self.executeCommand(self.objectName, "getState")
		except ApiError as e:
			print(e)
	def cmdStopHoming(self):
		try:
			self.executeCommand(self.objectName, "stopHoming")
		except ApiError as e:
			print(e)
	def cmdStartHoming(self):
		try:
			self.executeCommand(self.objectName, "startHoming")
		except ApiError as e:
			print(e)
	def cmdHomingState(self, b):
		try:
			parameters = [b]
			self.executeCommand(self.objectName, "homingState", parameters)
		except ApiError as e:
			print(e)
	def cmdUpdateState(self, state):
		try:
			parameters = [state]
			self.executeCommand(self.objectName, "updateState", parameters)
		except ApiError as e:
			print(e)
	def cmdDestroy(self):
		try:
			self.executeCommand(self.objectName, "destroy")
		except ApiError as e:
			print(e)
	def cmdDriverConectionState(self):
		try:
			self.executeCommand(self.objectName, "driverConectionState")
		except ApiError as e:
			print(e)
	def cmdDoorMissIndexed(self):
		try:
			self.executeCommand(self.objectName, "doorMissIndexed")
		except ApiError as e:
			print(e)
	def cmdPopUpDoorMissIndexedClosed(self):
		try:
			self.executeCommand(self.objectName, "popUpDoorMissIndexedClosed")
		except ApiError as e:
			print(e)
	def cmdPopUpDoorMissIndexedRaised(self):
		try:
			self.executeCommand(self.objectName, "popUpDoorMissIndexedRaised")
		except ApiError as e:
			print(e)