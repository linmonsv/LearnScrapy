import requests
files = {'uploadFile': open('logo.jpg', 'rb')}
r = requests.post("http://pythonscraping.com/pages/processing2.php",
files=files)
print(r.text)
