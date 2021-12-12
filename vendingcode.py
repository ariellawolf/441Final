#!/usr/bin/python37all
import cgi
import cgitb
import json
cgitb.enable()

data = cgi.FieldStorage()
snack = data.getvalue('option')
data = {'option':snack}
with open('/usr/lib/cgi-bin/vending.txt', 'w') as f:
    json.dump(data,f)
    
print('Content-type:text/html\n\n')
print('<html>')
print('<head>')
print('<title>Online Vending Machine</title>')
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



print('<form action="/cgi-bin/vendingcode.py" method="POST">')
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

if snack == "hersheys" or snack == "kitkat":
  print ('<font color="red"> %s is out of stock' % snack)
else:
  print ('<font color="black"> %s is in stock' % snack)

print('</form>')
print('<br>')
print('</html>')
