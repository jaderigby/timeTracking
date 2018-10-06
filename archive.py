import os, helpers, json

from settings import settings

def execute():
	newRecordName = '{}-record.py'.format(helpers.date_stamp())

	settings['record'] = newRecordName

	content = "settings = {}".format(helpers.glue_updated_record(settings))

	newRecordBlueprint = '''{
	"current" : "",
	"projects" : {}
}'''
	print
	print "==========================================="
	print
	print "Creating new record file: {}".format(newRecordName)
	helpers.write_file(settings['record_url'] + newRecordName, newRecordBlueprint)

	print '''
Updating settings file:

...
    "record" : "{}"
...
'''.format(newRecordName)
	print "==========================================="
	print
	# print os.path.realpath(__file__).replace('archive.py', '') + 'settings.py'
	# print json.dumps(content)
	helpers.write_file(os.path.realpath(__file__).replace('archive.py', '') + 'settings.py', content)
