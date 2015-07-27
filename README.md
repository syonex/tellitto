# tellitto

This is tellitto - a notification tool for pager, SMS, etc.

Using a tellitto.cfg configuration file, a command like
    echo hello | tellitto bob
will try mutliple methods, in turn, to contact "bob", until
one succeeds, or the possibilities are exhausted.

This is handy if you have multiple modmes, or web interfaces
(or email) for sending text or SMS messages to phones or pagers.

Sample config fragment:

    bob    pageuser bob
    bob    smsgateway 12125551234
    bob    clickatellgate 12125551234
    bob    mail -s tellitto-notification bob@example.com


It was originally written for use with Nagios notifications, but
can be used as a generic (simple) SMS/pager frontend.

It works nicely with genoa.

## Building

You should be able to run "autoreconf" to create a configure
script, and carry on from there.

## Notes

This distribution could use a little improvement.

I wrote this at FreshBooks www.freshbooks.com
    #1 Cloud Accounting Specialist for Small Business Owners

See also
    https://exchange.nagios.org/directory/Addons/Notifications/tellitto/details

Feedback and suggestions greatly appreciated.

John Sellens
info@syonex.com
