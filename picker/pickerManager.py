from enum import IntFlag
import random

from .schemePicker import SchemePicker
from .themePicker import ThemePicker
from .truePicker import TruePicker

class PickerType(IntFlag):
	TRUE = 1
	THEME = 2
	SCHEME = 4
	ALL = 7

class PickerManager:

	@staticmethod
	def getPickerList(pickerType: PickerType):
		trp = TruePicker()
		thp = ThemePicker()
		shp = SchemePicker()
		pickerList = []
		if pickerType in [1, 3, 5, 7]:
			pickerList.append(trp)
		if pickerType in [2, 3, 6, 7]:
			pickerList.append(thp)
		if pickerType in [4, 5, 6, 7]:
			pickerList.append(shp)
		return pickerList

	@staticmethod
	def getPicker(pickerType: PickerType = PickerType.ALL, num: int = 1, subtype: str = None):

		pickerList = PickerManager.getPickerList(pickerType)
		randomPicker = random.choice(pickerList)

		randomPicker.setSubtype(num, subtype)

		return randomPicker

