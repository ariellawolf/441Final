#!/usr/bin/python37all
import RPi.GPIO as GPIO
import cgi
import cgitb
import json
cgitb.enable()

print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Online Vending Machine</title>')
print('<meta http-equiv="refresh" content="30">')  # refresh to update LED state
print('</head>')

print('<body>')
print('<div style="width:1200px;background:#7816CF;border:1px;text-align:center">')
print('<br>')
print('<p style="font-size:30px;font-family:verdana;color:white">Please Select Your Snack.</p>')
print('<br>')
print('</body>')

print('<body>')
print('<div style="width:1200px;background:#FFFFFF;border:1px;text-align:left">')
print('<br>')

data = cgi.FieldStorage()
s1 = data.getvalue('option')
data = {"option":s1}
with open('vending.txt', 'w') as f:
    json.dump(data,f)

print('<form action="/cgi-bin/radio.py" method="POST">')
print('<label>')
print('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRAtITLRhcF-gW8Rml2NyaK8SWE-wTtO7Opvg&usqp=CAU"width="200"height="100"/>')
print('<input type="radio" name="option" value="reeces" checked> Reeces - $1.00 <br>')
print('</label>')

print('<label>')
print('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUkNB5UehomUKwJj-VIVrY_xk-N49R8EIJbg&usqp=CAU"width="200"height="100" />')
print('<input type="radio" name="option" value="hersheys" checked> Hersheys - $1.00 <br>')
print('</label>')

print('<label>')
print('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQcR1OnqW4JbB_6CmDV0S6T8XKXodHws7V4g&usqp=CAU"width="200"height="100" />')
print('<input type="radio" name="option" value="kitkat" checked> Kit-Kat - $1.00 <br>')
print('</label>')

print('<input type="submit" value="Purchase">')

if s1 == "hersheys" or s1 == "kitkat":
  print ('<font color="red"> Out of Stock')
else:
  print ('<font color="black"> In Stock')

print('</form>')
print('<br>')
print('</html>')
