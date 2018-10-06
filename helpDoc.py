def execute():
	print '''
TRACK DOCUMENTATION:

[ track ] or [ track status ] = show tracking status
[ track -t <project name>]    = add a new project and begin tracking it
[ track -t ]                  = start tracking current project
[ track -u ]                  = stop tracking current project
[ track -U ]                  = stop tracking and log work
[ track -l ]                  = list all projects
[ track -T ]                  = list project times by date
[ track -a ]                  = list all project times
[ track -d ]                  = list all project dates
[ track archive ]             = archive the current record and generate and attach a new one
[ track -j ]                  = log work for items not yet logged
'''
