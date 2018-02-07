import urllib2

response = urllib2.urlopen("http://www.baidu.com/")
html_content = response.read()

print(html_content)
print("Good boy")
input("")
