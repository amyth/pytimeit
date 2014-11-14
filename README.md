###PyTimeit - v 0.1
<br>
####Introduction:
A python module that helps log/print time takes for a particular process. This module can simultaneously record time for multiple processes. This does not use a decorator so can be used even for a single line of python code.

####Usage:
<br>
```
from timeit import TimeLogger

timelog = TimeLogger(debug=True)


db_query = timelog.start_process("Make Database Query", prediction=2)
#some python code here 
timelog.stop_process(db_query)
```

####Contributors
Amyth Arora [<mail@amythsingh.com>]
