# pitone-salvadatare
Save appointments, check them and do other stuff with your google calendar account from your terminal. The ultimate goal would be to understand the input of the user no matter how it's inputted. E.g: "football arena 2 march" or "football 2 3 arena" or "arena 2 march football" should create the same event.


Let pitone salvadatare help you with saving important data, dates, etc... and from your terminal.
If you're a busy software developer, just use your already open terminal. No need to waste precious time and open a new tab on your browser.

Will use he goolge calendar API: https://developers.google.com/calendar/quickstart/python

Gets answer in an unorderd way from the terminal and recognizes the parts (where, when, what). Asks for additional information if pitone is not sure about something.

<h1> Requirements:</h1>
<p> As mentioned in the Google Calendar API (<a href="https://developers.google.com/calendar/quickstart/python">link</a>), these elemnts should be present in order for this project to function:
  <ul>
    <li>Python 3.6 or greater (The API itself is designed for python >= 2.6, however this prroject does not surely support it)</li>
    <li>pip package management tool</li>
    <li>A google account with google calendar enabled</li>
</ul>

<p><span style="color:#228B22;">Remark:<span> Do not forget to create you <b>Google Calendar API</b> credentials in the link provided above and save the file in the working directory of the project.</p>
  
<h1> Setup </h1>
First off, install the dependencies necessary to the functioning of the project. The most important ones are included in the executable <b>req</b> file. You will also need to generate your credentials to use the Google Calendar API which should be placed in the pitone-salavadatare folder. You can look at step 1 in the <a href="https://developers.google.com/calendar/quickstart/python">link</a> that we have mentioned already.

```
$ ./req
```

Second, run the project:

```
$ python pitone
```

You will need to authorize the account and allow the required accesses. You should do this everytime you regenerate the token.pickle file. So, if it's saved, this authorization only happens once.
