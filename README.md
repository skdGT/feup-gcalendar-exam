# FEUP Exam Calendar

A Python script to add exam events to your Google Calendar (with feupy)



## Prerequisites

Make sure you have all of the following prerequisites:

- [Python 3]( https://www.python.org/downloads/ )
- The pip package management tool
- A Google account with Google Calendar enabled



Before running any script install the following dependences:

`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

`pip install feupy`



## Usage

- You can automatically add every exam that shows up in SIGARRA to your Google Calendar with:

  `python create_events.py <curricular year> <course acronym>`

​	this will add events starting with a graduation cap ( [🎓](https://emojipedia.org/graduation-cap/) ) to your Google Calendar with a 1-day reminder, you can change this later of course.



- You can automatically remove all upcoming events starting with a graduation cap or up to a max date with:

  `python remove_events.py [max date]`

  `max date` - **must** be in the YYYY-MM-DD format 

  

- Alternatively you can manually add an exam or test event to Google Calendar with:

  `python add_event.py`

  while this script is running you will be asked for some information, such as start date, rooms, etc. 



The first time it runs you'll be asked to authorize the script on a browser, a file `token-pickle` will be created, if you remove this file you will be prompt with the authorization message again.

You can always run `help(<file.py>)` to read the file's usage and documentation.



## Thanks

This script would be much more complex if it weren't for Daniel Monteiro's python library [`feupy`]( https://pypi.org/project/feupy/ ).



## Contribution

Feel free to submit a Pull Request as no template has been done yet.

Starting an Issue is also nice!