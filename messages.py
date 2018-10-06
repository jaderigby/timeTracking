def no_current_project():
	print '''
You currently have no project set.
'''

def tracking_message(OBJ, CURRENT):
	print '''
===========================================
Project: {}

Beginning tracking: {}
[time recording]
===========================================
'''.format(CURRENT, OBJ['start'])

def untracking_message(OBJ):
	print '''
===========================================
Ending tracking: {end}
[time recorded]

Time spent: {spent}
===========================================
'''.format(end=OBJ['end'], spent=OBJ['spent'])

def already_tracking(ITEM):
	print '''
Project \"{}\" already being tracked.
'''.format(ITEM)

def nothing_being_tracked():
	print '''
No project is currently being tracked.
'''

def statusMessage():
	print
	print "It has been created."
	print

def recorded():
	print
	print "Time for project has been recorded."
	print

def switch_to_a_project(ITEMS, CURRENT):
	i = 1
	print
	print "Projects:"
	print "---------"
	print
	for item in ITEMS:
		if item['name'] == CURRENT:
			isCurrent = '*'
			isCurrentFront = "** "
			isCurrentBack = " **"
		else:
			isCurrentFront = ""
			isCurrentBack = ""
		print '[{number}] {isCurrentFront}{item}{isCurrentBack} ({total})\n    Description: {description}\n    Today: {today}\n'.format(number=i, isCurrentFront=isCurrentFront, isCurrentBack=isCurrentBack, item=item['name'], total=item['total'], description=item['description'], today=item['total_today'])
		i += 1
	print "[x] Exit"
	print
	selection = raw_input("Select a project to switch to: ")
	print
	return selection

def select_project_for_times(SETTINGS):
	i = 0
	print
	print 'Projects:'
	print '---------'
	print
	for item in SETTINGS['projects']:
		i += 1
		print '[{number}] {name}'.format(number=i, name=item)
	print
	print '[x] Exit'
	print

	projectSelection = raw_input('Please select a project: ')

	return projectSelection

def select_date_for_times(SETTINGS):
	projectList = []
	dateList = []
	filteredDateList = []
	i = 0
	print
	print 'Dates:'
	print '------'
	print
	for item in SETTINGS['projects']:
		projectList.append(item)
	for item in projectList:
		for elem in SETTINGS['projects'][item]['time']:
			dateList.append(elem['spent_date'])
	for item in dateList:
		if item not in filteredDateList:
			filteredDateList.append(item)
	print filteredDateList.sort(reverse=True)
	for item in filteredDateList:
		if item != "":
			i += 1
			print '[{number}] {date}'.format(number=i, date=item)
	print
	print '[x] Exit'
	print

	selection = raw_input('Please select a date: ')

	return selection

def switching_project(PROJECT):
	print "Switching to: {}".format(PROJECT)
	print

def currentProject(ITEM, DESCRIPTION, TOTAL, TIME, TRACKING):
	trackingString = ""
	if TRACKING == True:
		trackingString = "\n* Currently being tracked *"
	print '''
Current Project:
===========================================

TITLE: {title} ({total_time})

DESCRIPTION: {description}

TODAY: {time_today}
{tracked}
===========================================
'''.format(title=ITEM, description=DESCRIPTION, total_time=TOTAL, time_today=TIME, tracked=trackingString)

def process_completed():
	print '''[Process Completed]
'''

def new_project_tracking(PROJECT, TIME):
	print '''
===========================================
New Project Created: {}

Beginning tracking: {}
[time recording]
===========================================
'''.format(PROJECT, TIME)

def show_projects_for_date(OBJ, DATE):
	for item in OBJ:
		if item == DATE:
			i = 0
			print
			print '''
---- {} -------------------'''.format(DATE)
			for elem in OBJ[item][item]['projects']:
				i += 1
				print '''
{i}.  Title:        {title}
    Description:  {description}
    Spent:        {time}'''.format(i=i, date=item, title=elem['title'], description=elem['description'], time=elem['spent'])
	print
	print "-----------------------------------"
	print

def nothing_to_log():
	print '''
===========================================
Nothing to Log.
===========================================
'''

def jira_item_being_logged(ITEM):
	print '''
Time being logged for:

{summary}'''.format(summary=ITEM)
