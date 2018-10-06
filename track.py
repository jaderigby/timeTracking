import json, helpers

import messages as msg

def execute(REPRESS_STATUS):
	record = helpers.load_record()
	
	current = record['current']

	if current == '':
		msg.no_current_project()
	else:
		recordedTime = helpers.time_stamp()
		obj = {}
		# print json.dumps(record, sort_keys=True, indent=4)
		for item in record['projects'][current]['time']:
			if item['end'] == '':
				obj = item

		if len(obj) <= 0 and not REPRESS_STATUS:
			newItem = helpers.new_time_obj(recordedTime)
			record['projects'][current]['time'].append(newItem)

			content = helpers.glue_updated_record(record)
			helpers.write_file(helpers.recordPath, content)

			msg.tracking_message(newItem, current)
		elif REPRESS_STATUS:
			msg.new_project_tracking(current, recordedTime)
		else:
			msg.already_tracking(current)