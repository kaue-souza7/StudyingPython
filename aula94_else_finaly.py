try:
    print('Open file')
    8/0
except ZeroDivisionError: 
    print('Dividiu Zero')
else: 
    print('not he had error')
finally:
    print('Close file')