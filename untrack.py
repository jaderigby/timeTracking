import json, helpers

import messages as msg

from time import gmtime, strftime


def execute():
	record = helpers.load_record()
	
	current = record['current']

	if current == "":
		msg.no_current_project()
	else:
		obj = {}
		spentList = []
		for item in record['projects'][current]['time']:
			spentList.append(item['spent'])
			if item['end'] == '':
				obj = item

		if len(obj) > 0:
			recordedTime = helpers.time_stamp()
			recordedDate = helpers.date_stamp()
			obj['end'] = recordedTime
			obj['spent'] = helpers.time_spent(obj['start'], obj['end'])
			obj['spent_date'] = recordedDate

			content = helpers.glue_updated_record(record)
			helpers.write_file(helpers.recordPath, content)

			msg.untracking_message(obj)
		else:
			msg.nothing_being_tracked()