import webbrowser as wb
with open('links.txt', 'r') as f:
    for line in f:
        a=line.strip()
        wb.open(a)