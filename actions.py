import sys, track, untrack, status, listing, addProject, allTime, helpDoc, timeBreakdown, archive, allTimeByDate, jiraLog, editEntry
# new imports start here

#= TODO
# - Log time if current project time is open, when switching  <track -l>
# - Start tracking when switching using <track -l>

try:
	action = str(sys.argv[1])
except:
	action = None

try:
	project = str(sys.argv[2])
except:
	project = None

if action == 'status' or action == None:
	status.execute()

elif action == '-t' and project == None:
	track.execute(False)

elif action == '-t' and project != None:
	addProject.execute(project)
	track.execute(True)

elif action == '-a':
	allTime.execute()

elif action == '-T':
	timeBreakdown.execute()

elif action == '-u':
	untrack.execute()

elif action == '-l':
	listing.execute()

elif action == '-ch' or action == 'archive':
	archive.execute()

elif action == '-d':
	allTimeByDate.execute()

elif action == '-h' or action == 'help':
	helpDoc.execute()

# elif action == '-j':
# 	jiraLog.execute()

elif action == '-U':
	untrack.execute()
	# jiraLog.execute()

elif action == "-e":
    editEntry.execute()
# new actions start here
