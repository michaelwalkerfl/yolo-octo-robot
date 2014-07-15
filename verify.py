#!/usr/bin/env python

print """
**********************************
Let\'s verify some emails spammer!
**********************************
"""

from validate_email import validate_email

email_list = raw_input('Enter the name of your email list: ')

with open('%s' % email_list) as input, open('valid.%s' % email_list, 'w') as output:
    for line in input:
        is_valid = validate_email(line, verify=True)
        if is_valid:
            output.write(line + '\n')
