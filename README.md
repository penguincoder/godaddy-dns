# DNS updating script

This keeps my goddaddy dns `@` entry pointed to my home IP.

In my crontab, I have this:

    12 * * * * API_KEY=XXXX API_SECRET=XXXX /home/andrew/code/godaddy-dns/run.sh > /dev/null 2>&1

Where `API_KEY` and `API_SECRET` are provided by GoDaddy. The path to the code is specific to my machine, as well.
