import basic 
while True:
    text = input('IDE >')
    result, error = basic.run('shell.py',text)

    if error: print(error.as_string())
    else: print(result)