# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.

import datetime
date = datetime.date.today().strftime('%a %d %b %Y')
time = datetime.datetime.now().strftime('%I:%M%p')
print(date, time)