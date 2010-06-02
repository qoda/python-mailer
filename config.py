"""
Global config file. Change variable below as needed but ensure that the log and
retry files have the correct permissions.
"""

# file settings
LOG_FILENAME = '/tmp/pymailer.log'
CSV_RETRY_FILENAME = '/tmp/pymailer.csv'

# smtp settings
SMTP_HOST = 'localhost'
SMTP_PORT = '25'

# the address and name the email comes from
FROM_NAME = 'Comapny Name'
FROM_EMAIL = 'company@example.com'

# test recipients list
TEST_RECIPIENTS = [
    {'name': 'Name', 'email': 'someone@example.com'},
]
