import helpers

import messages as msg


def execute():
	record = helpers.load_record()
	
	projectName = record['current']

	if projectName == "":
		msg.no_current_project()
	else:
		totalTimeDict = helpers.calculate_total_time_daily(record['projects'][projectName]['time'])
		totalTime = helpers.calculate_total_time(record['projects'][projectName]['time'])

		print '''
===========================================

{title} ({total})
Description: {description}

Breakdown by Day:
-----------------'''.format(title=projectName, description=record['projects'][projectName]['description'], total=totalTime)
		i = 0
		for item in totalTimeDict:
			if item['date'] == '':
				item['date'] = "-- {} --".format(helpers.date_stamp())
				item['spent'] = "currently tracking"
			i += 1
			print '''
{itemNumber}.  Date: {date}
    Spent: {spent}'''.format(itemNumber=i, date=item['date'], spent=item['spent'])
		print
		print '[Finished]'
		print "==========================================="
		print