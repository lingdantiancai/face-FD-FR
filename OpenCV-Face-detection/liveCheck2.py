import urllib, sys
import ssl
import urllib.request

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=4a9WXWn9VtuX0bTAGDuo0iAF&client_secret=p8O7KCal5A2qmEmBgEjU6Sw6EC32kMXj'
request = urllib.request(host)
request.add_header('Content-Type', 'application/json; charset=UTF-8')
response = urllib2.urlopen(request)
content = response.read()
if (content):
    print(content)