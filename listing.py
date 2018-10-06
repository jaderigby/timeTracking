import json, helpers

import messages as msg

from time import gmtime, strftime

def execute():
	record = helpers.load_record()

	selection = helpers.select_project(record)

	if selection != 'x':
		record['current'] = selection

		content = helpers.glue_updated_record(record)

		helpers.write_file(helpers.recordPath, content)

		msg.switching_project(selection)

	else:
		msg.process_completed()
