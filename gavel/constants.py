ANNOTATOR_ID = 'annotator_id'
TELEMETRY_URL = 'https://telemetry.anish.io/api/v1/submit'
TELEMETRY_DELTA = 20 * 60 # seconds
SENDGRID_URL = "https://api.sendgrid.com/v3/mail/send"

# Setting
# keys
SETTING_CLOSED = 'closed' # boolean
SETTING_TELEMETRY_LAST_SENT = 'telemetry_sent_time' # integer
# values
SETTING_TRUE = 'true'
SETTING_FALSE = 'false'

# Defaults
# these can be overridden via the config file
DEFAULT_WELCOME_MESSAGE = '''
Welcome to Gavel.

**Please read this important message carefully before continuing.**

Gavel is a fully automated expo judging system that both tells you where to go
and collects your votes.

Gavel uses the model of pairwise comparison. You'll start by
confirming that you have seen a particular project, and then for every submission after that, you'll decide whether it's better or worse than the one you looked **immediately beforehand**.

During the judging process, if you encounter a project which you haven't seen please contact the organizer immediately.

Gavel makes it simple for you to submit votes, but please think hard
before you vote. **Once you make a decision, you can't take it back**.
'''.strip()

DEFAULT_EMAIL_SUBJECT = 'Hack for Impact Judges Access'

DEFAULT_EMAIL_BODY = '''
Hello {name},

This email contains your access link to the Judging System for Hack for Impact event.

DO NOT SHARE this email with others.

We are using the Gavel Judging System for this event.

Once you are in, please take the time to read the welcome message and instructions before continuing.

To access the system, visit {link}.

Thanks
HackCU| University of Colorado Boulder

'''.strip()

DEFAULT_CLOSED_MESSAGE = '''
The judging system is currently closed. Reload the page to try again.
'''.strip():

DEFAULT_DISABLED_MESSAGE = '''
Your account is currently disabled. Reload the page to try again.
'''.strip()

DEFAULT_LOGGED_OUT_MESSAGE = '''
You are currently logged out. Open your magic link to get started.
'''.strip()

DEFAULT_WAIT_MESSAGE = '''
Wait for a little bit and reload the page to try again.

If you've looked at all the projects already, then you're done.
'''.strip()
