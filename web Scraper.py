import requests 

r = requests.get('https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/') 


print(r) 

print(r.content)
