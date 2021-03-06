# FEUP Exam Calendar

A Python script to add exam events to your Google Calendar (with feupy)



## Prerequisites

Make sure you have all of the following prerequisites:

- [Python 3]( https://www.python.org/downloads/ )
- The pip package management tool
- A Google account with Google Calendar enabled
- A json credentials file in order to use the Google Calendar's API
    - can be found [here](https://developers.google.com/calendar/quickstart/python);
    - After you enable the API click on **DOWNLOAD CLIENT CONFIGURATION** and save the credentials file to the main folder of this project.
  

Before running any script install the following dependencies:

```bash
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
```bash
pip install feupy
```


## Usage

- You can automatically add every exam that shows up in SIGARRA to your Google Calendar with:
```bash
python create_events.py <curricular year> <course acronym>
```
​	this will add events starting with a graduation cap ([🎓](https://emojipedia.org/graduation-cap/)) to your Google Calendar with a 1-day reminder, you can change this later of course.



- You can automatically remove all upcoming events starting with a graduation cap or up to a max date with:

  ```bash
  python remove_events.py [max date]
  ```
  `max date` - **must** be in the YYYY-MM-DD format 

  

- Alternatively you can manually add an exam or test event to Google Calendar with:

  ```bash
  python add_event.py
  ```
  
  while this script is running you will be asked for some information, such as start date, rooms, etc. 



The first time it runs you'll be asked to authorize the script on a browser, a file `token-pickle` will be created, if you remove this file you will be prompt with the authorization message again.

You can always run `help(<file.py>)` to read the file's usage and documentation.

If you are getting any errors try executing your terminal with admin previleges.



## Thanks

This script would be much more complex if it weren't for Daniel Monteiro's python library [`feupy`]( https://pypi.org/project/feupy/ ).



## Contribution

Feel free to submit a Pull Request as no template has been done yet.

Starting an Issue is also nice!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
