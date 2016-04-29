import urllib

text = open("/Users/johnkoretoff/code/udacity/programming-foundations-with-python/scan-text.rtf")
content = text.read()

url_place = urllib.urlopen("http://isithackday.com/arrpi.php?text="+content)
response = url_place.read()
print(response)
url_place.close()
text.close
