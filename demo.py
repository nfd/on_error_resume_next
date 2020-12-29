from basic import on_error_resume_next, err

on_error_resume_next()

def awesome(val):
    return val / 0

handle = open("does not exist")
if err():
    print('uh oh!')

value = 42
value += "hi"
value = awesome(value)
print(value)
