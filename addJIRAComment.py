#add comment 
import requests

# JIRA API credentials
JIRA_USERNAME = 'rohitpatils0096@gmail.com'
JIRA_API_TOKEN = 'ATATT3xFfGF0IA8JMNEY42uEJe37OvRjaPegV6tPwZR2hi90meb6Hv0Qid6HuXE6YEySsk06uyk-4krGsXBXKLtewiugNM3L5B1j0sNvnfchao4EUsrx51va_vgU1I35kjCTwFULc0mXM0YsTWGfWRlazhCzaawJbHHmi2VQAyLRuH0bMy4EsKM=4F575432'

# JIRA ticket details
JIRA_BASE_URL = 'https://test-portal.atlassian.net'
JIRA_TICKET_KEY = 'ITSM-1'

# JIRA API endpoint for creating comments
JIRA_COMMENTS_ENDPOINT = f'{JIRA_BASE_URL}/rest/api/2/issue/{JIRA_TICKET_KEY}/comment'

# Comment content to be added
comment_body = 'This is a comment on the JIRA ticket.'

# JIRA API request headers
headers = {
    'Content-Type': 'application/json'
}

# JIRA API request authentication (using username and API token)
auth = (JIRA_USERNAME, JIRA_API_TOKEN)

# JIRA API request body
body = {
    'body': comment_body
}

# Send the API request to create a comment on the JIRA ticket
response = requests.post(JIRA_COMMENTS_ENDPOINT, headers=headers, auth=auth, json=body)

if response.status_code == 201:
    print('Comment added successfully.')
else:
    print('Failed to add comment.')
