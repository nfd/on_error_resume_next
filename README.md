Implementing ON ERROR RESUME NEXT in Python
===========================================

This implements the BASIC command ON ERROR RESUME NEXT in Python. When an exception is raised, the code is resumed at
the next line. Exception information can be retrieved using the `err()` function.

A full discussion is at [https://code.lardcave.net/2020/12/29/1/](code.lardcave.net).

Yes, this is a joke.

Pull requests welcomed.

Usage
-----

    from basic import on_error_resume_next
    
    on_error_resume_next()

    value = 1 / 0

Also see `demo.py`.
