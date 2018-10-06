import json, re

from datetime import datetime
from time import gmtime, strftime, localtime
from datetime import timedelta
from settings import settings
import messages as msg

recordPath = settings['record_url'] + settings['record']

def load_record():
	return json.loads(read_file(recordPath))

def write_file(FILEPATH, DATA):
	FILE = open(FILEPATH, 'w')
	FILE.write(DATA)
	FILE.close()

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data

def time_stamp():
	return strftime("%Y-%m-%d %H:%M", localtime())

def date_stamp():
	return strftime("%Y-%m-%d", localtime())

def time_spent(START, END):
	startFormat = datetime.strptime(START, '%Y-%m-%d %H:%M')
	endFormat = datetime.strptime(END, '%Y-%m-%d %H:%M')
	spent = endFormat - startFormat
	timeFormatted = str(spent)[:-3]
	return timeFormatted

def project_list(SETTINGS):
		i = 0
		newList = []
		for item in SETTINGS['projects']:
			newList.append(item)
		return newList

def retrieve_project_name(ID, PROJECTS):
	projectName = PROJECTS[int(ID) - 1]
	return projectName

def calculate_todays_time(OBJ_A, OBJ_B, TODAY):
	if (OBJ_A['start'] == OBJ_B['end'] and OBJ_A['start'] == TODAY):
		a = OBJ_A['spent']
		b = OBJ_B['spent']

	return calculate_time(a, b)

def format_timedelta(td):
	#= http://stackoverflow.com/questions/28503838/how-can-i-display-timedelta-in-hoursminsec
	minutes, seconds = divmod(td.seconds + td.days * 86400, 60)
	hours, minutes = divmod(minutes, 60)
	return '{:d}:{:02d}:{:02d}'.format(hours, minutes, seconds)

def calculate_time(A, B):
	# print "A: {}\nB: {}\n".format(A,B)
	if not A or not B:
		totalTime = '00:00'
	else:
		hrPat = ":[0-9]{2}"
		minPat = "[0-9]+:"
		re.sub(hrPat, '', A)

		aHours 		= int( re.sub(hrPat, '', A) )
		aMinutes 	= int( re.sub(minPat, '', A) )
		bHours 		= int( re.sub(hrPat, '', B) )
		bMinutes 	= int( re.sub(minPat, '', B) )

		totalHrs = aHours + bHours
		totalMinutes = aMinutes + bMinutes

		totalTimeString = str(timedelta(minutes=totalMinutes))[:-3]

		# totalTime = "{}:{}".format(totalHrs, totalMinutes)

		totalTime = str(format_timedelta(timedelta(minutes=totalMinutes + (totalHrs * 60))))[:-3]

	return totalTime

def glue_updated_settings(CURRENT, SETTINGS):
	# SETTINGS['projects'][CURRENT]
	settingsString = json.dumps(SETTINGS, sort_keys=True, indent=4)
	return settingsString
	# newString = '''settings = {}'''.format(settingsString)
	# return newString

def glue_updated_record(RECORD):
	# RECORD['projects'][CURRENT]
	recordString = json.dumps(RECORD, sort_keys=True, indent=4)
	return recordString
	# newString = '''record = {}'''.format(recordString)
	# return newString

def new_time_obj(START_TIME):
	newObj = {}

	newObj["start"] = START_TIME
	newObj["end"] = ""
	newObj["spent"] = ""
	newObj["spent_date"] = ""

	return newObj

def dissolve_to_unique_dates(OBJ, KEY):
	tempList = []
	newList = []
	for item in OBJ:
		tempList.append(item[KEY])
	for n in tempList:
		if n not in newList:
			newList.append(n)
	return newList

def calculate_time_by_start_stop(A, B):
	hrPat = ":[0-9]{2}"
	minPat = "[0-9]+:"

	aHours 		= int( re.sub(hrPat, '', A) )
	aMinutes 	= int( re.sub(minPat, '', A) )
	bHours 		= int( re.sub(hrPat, '', B) )
	bMinutes 	= int( re.sub(minPat, '', B) )

	totalHrs = bHours - aHours
	totalMinutes = bMinutes - aMinutes

	if totalMinutes < 0:
		totalHrs += -1
		aMinutes = 60 - aMinutes
		totalMinutes = aMinutes + bMinutes
	elif totalMinutes >= 60:
		totalHrs += 1
		totalMinutes = totalMinutes - 60

	def formatMinutes(VAL):
		if VAL < 10:
			return '0' + str(VAL)
		return str(VAL)

	totalTime = str(totalHrs) + ':' + formatMinutes(totalMinutes)

	return totalTime

def calculate_total_time(TIME):
	timeList = []
	for item in TIME:
		if item['spent'] == '' and item['spent_date'] == '' and item['end'] == '':
			item['spent'] = time_spent(item['start'], time_stamp())
		timeList.append(item['spent'])
	timeItem = '00:00'
	for i in timeList:
		timeItem = calculate_time(timeItem, i)
	return timeItem

def calculate_total_time_today(TIME, TODAY):
	timeList = []
	for item in TIME:
		if item['spent_date'] == TODAY:
			timeList.append(item['spent'])
	timeItem = '00:00'
	for i in timeList:
		timeItem = calculate_time(timeItem, i)
	return timeItem

def calculate_total_time_daily(TIME):
	tempList = dissolve_to_unique_dates(TIME, 'spent_date')
	newSet = []
	#= each item in list
	for item in tempList:
		totalTime = "00:00"
		newObj = {}
		newList = []
		#= compare all items to current
		for i in TIME:
			if item == i['spent_date']:
				newList.append(i['spent'])
		for s in newList:
			totalTime = calculate_time(s, totalTime)
		newObj['date'] = item
		newObj['spent'] = totalTime
		newSet.append(newObj)
	return newSet

def compile_date_list(SETTINGS):
	projectList = []
	dateList = []
	filteredDateList = []
	for item in SETTINGS['projects']:
		projectList.append(item)
	for item in projectList:
		for elem in SETTINGS['projects'][item]['time']:
			dateList.append(elem['spent_date'])
	for item in dateList:
		if item not in filteredDateList:
			filteredDateList.append(item)
	return filteredDateList

def compile_time_date_dict(SETTINGS):
	projectList = []
	dateList = []
	filteredDateList = []
	timeList = []
	for item in SETTINGS['projects']:
		projectList.append(item)
	for item in projectList:
		for elem in SETTINGS['projects'][item]['time']:
			dateList.append(elem['spent_date'])
	for item in dateList:
		if item not in filteredDateList:
			filteredDateList.append(item)
	for item in filteredDateList:
		newObj = {}
		newObj['spent_date'] = item
		newObj['total_spent'] = '00:00'
		for elem in SETTINGS['projects']:
			for i in SETTINGS['projects'][elem]['time']:
				if i['spent_date'] == newObj['spent_date']:
					newObj['total_spent'] = calculate_time(i['spent'], newObj['total_spent'])
		timeList.append(newObj)
	return timeList

def collect_projects_by_date(DATES, PROJECTS):
	newList = {}
	for date in DATES:
		newObj = {}
		newObj[date] = {}
		newObj[date]["projects"] = []
		newList[date] = newObj
		for item in PROJECTS:
			for elem in PROJECTS[item]['time']:
				newItemObj = {}
				# print "elem: {}".format(elem)
				if date == elem['spent_date']:
					newItemObj['title'] = item
					newItemObj['description'] = PROJECTS[item]['description']
					newItemObj['spent'] = elem['spent']
					newObj[date]["projects"].append(newItemObj)
	return newList

def bind_duplicates(LIST):
	for item in LIST:
		print item

def work_log_list(RECORD, CURRENT):
	newList = []
	for item in RECORD['projects'][CURRENT]['time']:
		if item['spent'] != '':
			if 'jira_recorded' in item:
				if item['jira_recorded'] == 'False':
					newList.append(item)
			else:
				newList.append(item)
	return newList

def time_worked(TIME):
	hrPat = "[0-9]{1,2}(?=\:)|$"
	minPat = "(?!\:)[0-9]{2}|$"
	hrs = re.search(hrPat, TIME).group() + 'h'
	mins = re.search(minPat, TIME).group() + 'm'
	newString = hrs + ' ' + mins
	return newString

def create_new_project(TIME):
	tempObj	 = {}
	timeObj = {}
	tempObj	['description'] = ""
	tempObj	['time'] = []
	timeObj['start'] = TIME
	timeObj['end'] = ""
	timeObj['spent'] = ""
	timeObj['spent_date'] = ""
	timeObj['jira_recorded'] = "False"
	tempObj	['time'].append(timeObj)
	return tempObj

def select_project(OBJ):
	current = OBJ['current']
	today = date_stamp()
	projectList = []
	projectListTimes = []

	#= Get list of project names
	for item in OBJ['projects']:
		projectList.append(item)

	#= Construct project info for message
	for item in OBJ['projects']:
		newObj = {}
		newObj['name'] = item
		newObj['description'] = OBJ['projects'][item]['description']
		t = calculate_total_time(OBJ['projects'][item]['time'])
		tt = calculate_total_time_today(OBJ['projects'][item]['time'], today)
		newObj['total'] = t
		newObj['total_today'] = tt
		projectListTimes.append(newObj)

	selection = msg.switch_to_a_project(projectListTimes, current)
	if selection != 'x':
		selectionName = projectList[int(selection) - 1]
	else:
		selectionName = 'x'
	return selectionName

def select_entry(RECORD, ITEM):
	selectionName = ITEM
	i = 1
	print("")
	for item in RECORD['projects'][ITEM]['time']:
		print('''[{}] START: {}
    END:   {}
'''.format(i, item['start'], item['end']))
		i += 1
	selection = raw_input('''[x] Exit

Select an entry to edit: ''')

	if selection != 'x':
		selectedItem = RECORD['projects'][ITEM]['time'][int(selection) - 1]
		selectedIndex = selection
	else:
		selectedItem = selection
		selectedIndex = False
	return selectedItem, selection

def add_a_description():
	return raw_input("Please enter a description: ")

def work_log_comment(DATE, ITEM):
	comment = raw_input('{date}:{time} ---> Comment: '.format(date=DATE, time=ITEM))
	if comment == '':
		return None
	else:
		return comment

def jira_log_items(ISSUE, ITEMS):
	print ISSUE
	for item in ITEMS:
		if item['spent'] != '':
			if 'jira_recorded' in item:
				if item['jira_recorded'] == 'False':
					timeWorked = time_worked(item['spent'])
					if timeWorked != '0h 00m':
						ISSUE.add_worklog(current, timeSpent=timeWorked, timeSpentSeconds=None, adjustEstimate=None, newEstimate=None, reduceBy=None, comment=work_log_comment(), started=None, user=None)
					item['jira_recorded'] = 'True'
			else:
				timeWorked = time_worked(item['spent'])
				if timeWorked != '0h 00m':
					ISSUE.add_worklog(current, timeSpent=timeWorked, timeSpentSeconds=None, adjustEstimate=None, newEstimate=None, reduceBy=None, comment=work_log_comment(), started=None, user=None)
				item['jira_recorded'] = 'True'

monthName = [
	  'Jan'
	, 'Feb'
	, 'Mar'
	, 'Apr'
	, 'May'
	, 'Jun'
	, 'Jul'
	, 'Aug'
	, 'Sep'
	, 'Oct'
	, 'Nov'
	, 'Dec'
]

def jira_start_date_format(DATE, START):
	# 01/Jun/17 9:21 AM
	dateList = DATE.split('-')
	dateString = ''
	for i, item in enumerate(reversed(dateList)):
		if i == 2:
			dateString += item[2:]
		elif i == 1:
			dateString += (monthName[int(item) - 1] + '/')
		else:
			dateString += (item + '/')
	dissolveToTime = START[11:]
	hrs = int(dissolveToTime[:-3])
	mins = dissolveToTime[3:]
	if hrs > 12:
		hrs = hrs - 12
		if hrs < 10:
			hrs = "0" + str(hrs)
		suffix = "PM"
	elif hrs < 10:
		hrs = "0" + str(hrs)
	else:
		hrs = hrs
		suffix = "AM"
	newString = dateString + " " + str(hrs) + ":" + mins + " " + suffix
	return newString

def jira_start_date_format2(ENTRY):
	date = ENTRY[:10]
	time = ENTRY[11:]
	newString = date + 'T' + time + ':00.273+0000'
	return newString
