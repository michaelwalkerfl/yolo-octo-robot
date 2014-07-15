#!/usr/bin/env python

print """
**********************************
Let\'s verify some emails spammer!
**********************************
"""

from validate_email import validate_email

email_list = raw_input('Enter the name of your email list: ')

validation_mode = raw_input('What mode would you like for this run? (Please enter Basic, MX or Full)')

""" If 'Basic' mode, verify emails in list are syntactically correct. """
if validation_mode == 'Basic':
    with open('%s' % email_list, 'r') as input, open('valid.%s' % email_list, 'w') as output:
        for line in input:
            is_valid = validate_email(line)
            if is_valid:
                output.write(line)

""" If 'MX' mode, verify emails in list have MX server. """
if validation_mode == 'MX':
    with open('%s' % email_list, 'r') as input, open('valid.%s' % email_list, 'w') as output:
        for line in input:
            is_valid = validate_email(line, check_mx=True)
            if is_valid:
                output.write(line)

""" If 'Full' mode, attempt to verify that the user is valid at mx server. """
if validation_mode == 'Full':
    with open('%s' % email_list, 'r') as input, open('valid.%s' % email_list, 'w') as output:
        for line in input:
            is_valid = validate_email(line, verify=True)
            if is_valid:
                output.write(line)
