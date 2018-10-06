import helpers

import messages as msg

from passwordHide import passwordHide
from jira import JIRA

def execute():
    record = helpers.load_record()

    current = record['current']

    workLogList = helpers.work_log_list(record, current)
    if len(workLogList) != 0:
        jira = JIRA('https://contentwatch.atlassian.net', basic_auth=(passwordHide['username'], passwordHide['password']))
        issue = jira.issue(current)
        msg.jira_item_being_logged(issue.fields.summary)

        print "----------------------------------"
        for item in workLogList:
            print 'Time:   {time}'.format(time=helpers.time_worked(item['spent']))
        print
        for item in record['projects'][current]['time']:
            if item['spent'] != '':
                if 'jira_recorded' in item:
                    if item['jira_recorded'] == 'False':
                        timeWorked = helpers.time_worked(item['spent'])
                        if timeWorked != '0h 00m':
                            # print helpers.jira_start_date_format2(item['start'])
                            jira.add_worklog(current, timeSpent=timeWorked, timeSpentSeconds=None, adjustEstimate=None, newEstimate=None, reduceBy=None, comment=helpers.work_log_comment(item['spent_date'], timeWorked), started=None, user=None)
                        item['jira_recorded'] = 'True'
                else:
                    timeWorked = helpers.time_worked(item['spent'])
                    if timeWorked != '0h 00m':
                        # print helpers.jira_start_date_format2(item['start'])
                        jira.add_worklog(current, timeSpent=timeWorked, timeSpentSeconds=None, adjustEstimate=None, newEstimate=None, reduceBy=None, comment=helpers.work_log_comment(item['spent_date'], timeWorked), started=None, user=None)
                    item['jira_recorded'] = 'True'
        content = helpers.glue_updated_record(record)
        helpers.write_file(helpers.recordPath, content)
        print
        msg.process_completed()
    else:
        msg.nothing_to_log()
