PyMailer
========
**Simple python bulk mailer script. Raw python using std libs.**

Send bulk html emails from the commandline or in your python script by specifying a database of recipients in csv form, a html template with var placeholders and a subject line.


Requirements
------------

* python >= 2.4

Usage
-----
Setup
~~~~~
Edit the config file before running the script::

    $ vim config.py

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
    
Examples
--------
HTML
~~~~
Example of using placeholders in your html email::

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    <html lang="en">
        <body>
            <h1>Test HTML Email - <!--name--></h1>
            <p>Hi <!--name-->, This is a test email from Pymailer - <a href="http://github.com:80/qoda/PyMailer/">http://github.com:80/qoda/PyMailer/</a>.</p>
        </body>
    </html>

CSV
~~~
Example of how the csv file should look::

    Someones Name,someone@example.com
    Someone Else,someone.else@example.com
    ,some.nameless.person@example.com
    
Author
------
Jonathan Bydendyk - Edenvale, South Africa
