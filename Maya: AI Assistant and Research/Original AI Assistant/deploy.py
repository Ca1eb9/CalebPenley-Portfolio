import requests
import os
dir = 'deploy'
if len(os.listdir(dir)) <= 2:
    print('check files')
    input('Yes? type: y')
for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    if os.path.isfile(f):
        file = open(f, "rb")
        try:
            res = requests.post("http://23.239.9.14:5375/send", files = {"file": file})
        except:
            file = open(f, "rb")
            res = requests.post("http://207.255.166.140:5375/send", files = {"file": file})
        if res.ok:
            print('Response: ' + res.text)
        else:
            print("Something went wrong!")