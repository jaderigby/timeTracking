import json, helpers

import messages as msg

from time import gmtime, strftime
from settings import settings

def execute():
	current = settings['current']

	def updatedSettings(CURRENT):
		settings['projects'][CURRENT]
		settingsString = json.dumps(settings, sort_keys=True, indent=4)
		newString = '''settings = {}'''.format(settingsString)
		return newString

	# def time_calc(VAL):


	# def calculate_time_spent(START, END):
	# 	startDate = START[0:-6]
	# 	endDate = END[0:-6]
	# 	startTime = START[10:]
	# 	endTime = END[10:]
		# if startDate == endDate:
		# 	time_calc(startTime) - time_calc(endTime)

	# def record_time_spent(OBJ, TIME):
	# 	OBJ['end'] = TIME
	# 	spent = calculate_time_spent(OBJ['start'], TIME)
	# 	OBJ['spent'] = spent
	# 	return OBJ

	obj = {}
	spentList = []
	for item in settings['projects'][current]['time']:
		spentList.append(item['spent'])
		if item['end'] == '':
			obj = item

	if len(obj) > 0:
		recordedTime = strftime("%Y-%m-%d %H:%M", gmtime())
		obj['end'] = recordedTime
		obj['spent'] = helpers.time_spent(obj['start'], obj['end'])

		content = updatedSettings(current)

		total = 0
		for item in spentList:
			total += item

		helpers.write_file(settings['url'] + 'projectTracking/settings.py', content)

		msg.untracking_message(obj, total)

	# def recordTimeObj(TIME):
	# 	newObj = {}

	# 	newObj['start'] = TIME
	# 	newObj['end'] = ""
	# 	newObj['spent'] = ""

	# 	return newObj

	# def updatedSettings(CURRENT):
	# 	settings['projects'][CURRENT]
	# 	settingsString = json.dumps(settings, sort_keys=True, indent=4)
	# 	newString = '''settings = {}'''.format(settingsString)
	# 	return newString

	# obj = {}
	# for item in settings['projects'][current]['time']:
	# 	if item['end'] == '':
	# 		obj = item

	# if len(obj) <= 0:
	# 	recordedTime = strftime("%Y-%m-%d %H:%M", gmtime())
	# 	newItem = recordTimeObj(recordedTime)
	# 	settings['projects'][current]['time'].append(newItem)

	# 	content = updatedSettings(current)

	# 	helpers.write_file('/Users/jrigby/Documents/local-bash-tools/projectTracking/settings.py', content)

	# 	msg.recorded()