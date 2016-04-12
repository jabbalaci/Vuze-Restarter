Vuze Restarter
==============

Restart vuze automatically if it dies unexpectedly.

Problem
-------
My preferred bittorrent client is Vuze. However, on some of my machines it
crashes after some time. I didn't want to dig in, so I chose a simpler way:
a process is checking if vuze is running and restarts it if it's gone.

Usage
-----
First run the script `start_vuze.sh`. It should start Vuze on your
system. My vuze is installed in the `/opt/vuze` folder, so if your vuze
is somewhere else then modify the script accordingly. You need to adjust
this script just once. Later on use the `keep_alive.py` script.

If `start_vuze.sh` works correctly, then start the monitoring program
with `keep_alive.py`. It will start vuze for you. If vuze dies, this
script will restart vuze automatically. Keep this monitoring program
running as long as you want to keep vuze alive.

Generalization
--------------
Of course, you can replace vuze with something else and the monitoring
script will keep restarting that program.
