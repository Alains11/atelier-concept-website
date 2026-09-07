# Roper Studio Booking Clone

## Description of the project
This project is a custom studio-booking concept app built around the Roper experience: explore studios, review listings, and reserve a session.

The app includes a Flask frontend and API, a custom file-backed storage layer, and a simple booking flow for users.

### General concepts in review
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Files and Directories
- `models` directory contains the domain models.
- `tests` contains the project test suite.
- `console.py` is the local command interpreter entry point.
- `models/base_model.py` contains the common base model logic.
- `models/engine` contains the file storage implementation.

## General Execution
Your shell should work like this in interactive mode:
```
$ ./console.py
(roper) help

Documented commands (type help <topic>):
========================================
EOF  help  quit
(roper)
(roper)
(roper) quit
$
But also in non-interactive mode:

$ echo "help" | ./console.py
(roper)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(roper)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(roper)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(roper)
$
```

## Final Product
This project is designed as a studio-booking landing page and reservation flow for the Roper brand.
<<<<<<< HEAD
(hbnb)
=======
(roper)
>>>>>>> 3049fcd (Initial commit for Roper studio booking app)
$
```
## Final Product
![alt](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/fe2e3e7701dec72ce612472dab9bb55fe0e9f6d4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU65GPZGY3%2F20210226%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210226T091352Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=8ad0ced94d77d100be587f30d4af3734acf12d2b05b803b084cd11ce51bf68f4)
## Data Diagram
![alt](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/9/99e1a8f2be8c09d5ce5ac321e8cf39f0917f8db5.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU65GPZGY3%2F20210226%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20210226T091352Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=a4013a9239416a982d703d1ac725e63a9b35593900d197534d087b71f813441c)