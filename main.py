import webbrowser as wb
import time
with open('links.txt', 'r') as f:
    for line in f:
        a=line.strip()
        wb.open(a)
        time.sleep(2) #cooldown time in seconds, change as per requirement
        
