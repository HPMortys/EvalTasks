```bash
$ pip install -r .\requirements.txt
```

## TASK 1
There was implemented custom Hashmap class which provides basic methods as putting, getting, removing and others.
Specific logic:
  - As buckets representation was chosen 2D list for collision resolution, which allows us to store multiple elements in one bucket.The function "hash" for converting keys into integer hash values is used for creating indexes of buckets.
  - Added num_elemets recording for fast count checking of elements in hashmap and controling oversizing.
  - Adding dynamic resizing with using threshold, to balance between space efficiency and time complexity.

For testing was use unittest, as most suitable lib for simple testing (Nothing special).


## TASK 2
There was implemented class for users db manipulation (add, get, delete) via sessions.
Specific logic:
 - def get_async_session is ussually used while developing web apps with fast api, so I omited its implementation here and just use direcly session variable to reduce implementation conjestions.
 - As basic db for testing I choose sqlite+aiosqlite so I have async interface then (I hope so). Also, I created sql scripts for filling table with data.
 - Was create sqlachemy User model for creating statements for executing and pydentic UserDTO as pericular "serializer".
 - Was trying to mock sessions in unitests but unfortunttely I have not find valid solutions, so I just implement delete function and so after each creation I delete record.
 - 
