PyMailer
========
**Simple python bulk mailer script. Raw python using std libs.**

Send bulk html emails from the commandline or in your python script by specifying a database of recipients in csv form, a html template with var placeholders and a subject line.


Requirements
------------

* python >= 2.4

Usage
-----

Commandline
~~~~~~~~~~~
The simplest method of sending out a bulk email.

Run a test to predefined test_recipients::

    $ ./pymailer -t /path/to/html/file.html /path/to/csv/file.csv 'Email Subject'

Send the actual email to all recipients::

    $ ./pymailer -s /path/to/html/file.html /path/to/csv/file.csv 'Email Subject'


Module Import
~~~~~~~~~~~~~
Alernatively import the PyMailer class into your own code::

    from pymailer import PyMailer
    
    pymailer = PyMailer('/path/to/html/file.html' '/path/to/csv/file.csv' 'Email Subject')
    
    # send a test email
    pymailer.send_test()
    
    # send bulk mail
    pymailer.send()
    
Author
------
Jonathan Bydendyk - Edenvale, South Africa
