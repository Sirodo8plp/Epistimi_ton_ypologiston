import urllib.request

pageurl=input("give the url of the page: ")

fp = urllib.request.urlopen(pageurl)
mybytes = fp.read()
mystr = mybytes.decode("utf8")
pagecode = mystr.split('\n')

hrefcounter = 0 #counts hrefs
brcounter = 0  #counts <br>
pcounter = 0 #counts <p>s

for line in pagecode:
    
    if 'href' in line: hrefcounter +=1

    if '<br>' in line: brcounter +=1

    if '<p>' in line: pcounter +=1

print("There are ",hrefcounter," links in this page.")
print("There are ",brcounter," <br> in this page.")
print("There are ",pcounter," <p> in this page.")

fp.close()


