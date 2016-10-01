# python_tkinter
Absolutely useless, first piece of code I wrote using tkinter.
Throwback, two years ago I tried to replicate one of my childhood's most used program called **CWK**. The main function of the program allowed you to *turn off your computer after certain amount of time* or even *shutting it after closing certain running program.*

First thing was pretty easy, the second part though.. I'll be back here later.

Note: if anyone want to add that second function ie. turning off computer after exiting program this is how you might want to achieve it (**probably not!!**)

1. Use tasklist to get list of running applications ie. ```TASKLIST /v /fi "STATUS eq running"```
2. Delete everything WHERE UserName = unknown
3. Strip and save NAME and the PID to two arrays
4. Display to user possible options of application which could be executed (array with names)
5. Once user choose the name, use ```TASKKILL /PID <number> /F``` or alternatively ```TASKKILL /IM <name.exe> /F```
6. ```Run TASKLIST /v /fi "STATUS eq running"``` again and check if it contains removed PID or NAME
7. Add if statement checking if that PID was actually deleted and just turn off computer using ```call("shutdown -s -f")```

but ehm.. there's probably some library which allows you to get names and PIDs of running processes so.. I'm out..:runner::runner:
