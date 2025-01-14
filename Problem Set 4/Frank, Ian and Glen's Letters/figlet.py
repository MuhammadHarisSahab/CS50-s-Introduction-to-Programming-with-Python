from pyfiglet import Figlet  # type: ignore
import sys
import random
figlet = Figlet()
k = 'Invalid usage'

def randomformat():
    x = figlet.getFonts()
    figlet.setFont(font = random.choice(x))

def takeformat(q):
        j = figlet.getFonts()
        if q in j:
            figlet.setFont(font = q)
        else:
            
            sys.exit(k)
    

if len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        takeformat(sys.argv[2])
        x = str(input('Input: '))
        print(figlet.renderText(x))
    else:   
        sys.exit(k)        
elif len(sys.argv) == 1:
    randomformat()
    x = str(input('Input: '))
    print(figlet.renderText(x))
else:    
    sys.exit(k)


