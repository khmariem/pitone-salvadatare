# pitone-salvadatare
Save appointments, check them and do other stuff with your google calendar account from your terminal. The ultimate goal would be to understand the input of the user no matter how it's inputted. E.g: "football arena 2 march" or "football 2 3 arena" or "arena 2 march football" should create the same event.


Let pitone salvadatare help you with saving important data, dates, etc... and from your terminal.
If you're a busy software developer, just use your already open terminal. No need to waste precious time and open a new tab on your browser.

Will use he goolge calendar API: https://developers.google.com/calendar/quickstart/python

Gets answer in an unorderd way from the terminal and recognizes the parts (where, when, what). Asks for additional information if pitone is not sure about something.

<h1> Requirements:</h1>
<p> As mentioned in the Google Calendar API (<a href="https://developers.google.com/calendar/quickstart/python">link</a>), these elemnts should be present in order for this project to function:
  <ul>
    <li>Python 3.6 or greater (The API itself is designed for python >= 2.6, however this prroject does not surely supports it)</li>
    <li>pip package management tool</li>
    <li>A google account with google calendar enabled</li>
</ul>

<p><span style="color:#228B22;">Remark:<span> Do not forget to create you <b>Google Calendar API</b> credentials in the link provided above and save the file in the working directory of the project.</p>
