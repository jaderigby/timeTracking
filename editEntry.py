import helpers
import messages as msg

def execute():
	record = helpers.load_record()

	selection = helpers.select_project(record)

	if selection != 'x':
		entry, entryIndex = helpers.select_entry(record, selection)
		if entry != 'x':
			selectedEdit = input('''
PROJECT: {}
ENTRY:
         [1] start - {}
         [2] end -   {}

Select an item to change: '''.format(selection, entry['start'], entry['end']))

# 	editWhich = input('''
# [1] Date
# [2] Time
# [3] Both
#
# [x] Exit
#
# : ''')
		if selectedEdit is 1:
			record['projects'][selection]['time'][int(entryIndex) - 1]['start'] = raw_input('''Enter correct start time [{}]: '''.format(entry['start']))

			start = record['projects'][selection]['time'][int(entryIndex) - 1]['start']
			end = record['projects'][selection]['time'][int(entryIndex) - 1]['end']
			record['projects'][selection]['time'][int(entryIndex) - 1]['spent'] = helpers.calculate_time_by_start_stop(start, end)
		elif selectedEdit is 2:
			record['projects'][selection]['time'][int(entryIndex) - 1]['end'] = raw_input('''Enter correct end time [{}]: '''.format(entry['end']))
			newDate = record['projects'][selection]['time'][int(entryIndex) - 1]['end'][:-6]
			record['projects'][selection]['time'][int(entryIndex) - 1]['spent_date'] = newDate

			start = record['projects'][selection]['time'][int(entryIndex) - 1]['start'][11:]
			end = record['projects'][selection]['time'][int(entryIndex) - 1]['end'][11:]
			print("start: {}  end: {}".format(start, end))
			print helpers.calculate_time_by_start_stop(start, end)
			record['projects'][selection]['time'][int(entryIndex) - 1]['spent'] = helpers.calculate_time_by_start_stop(start, end)

		confirmChange = raw_input('''
You are about to change the entry to:
---------------------------------------------------

PROJECT:    "{}"

START:      {}
END:        {}
SPENT_DATE: {}
SPENT:      {}

Confirm Change (y/n): '''.format(
selection,
record['projects'][selection]['time'][int(entryIndex) - 1]['start'],
record['projects'][selection]['time'][int(entryIndex) - 1]['end'],
record['projects'][selection]['time'][int(entryIndex) - 1]['spent_date'],
record['projects'][selection]['time'][int(entryIndex) - 1]['spent']
))
		if confirmChange is 'y':
			content = helpers.glue_updated_record(record)

			helpers.write_file(helpers.recordPath, content)

			print('\nThe entry has been changed!\n')

		elif confirmChange is 'n':
			print('\nChange Aborted!\n')

		msg.process_completed()

	else:
		msg.process_completed()


	# project
	# entry
	# edit
	# save
