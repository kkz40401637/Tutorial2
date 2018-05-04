import urllib2,json,base64
accesstoken="MDUXGF429RKLCPA8QLYS"
institution="10007772"
course="U56119"
url="https://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Course/{}/FullTime/Statistics.json".format(
    institution,
    course
    )
request=urllib2.Request(url)
request.add_header(
    "Authorization",
    "Basic "+ base64.encodestring(accesstoken+":").replace('/n','')
    )
response=urllib2.urlopen(request)
data=json.load(response)
#print json.dumps(data,indent=2)

def f():
    a=data[6]
    b=a["Details"]
    c=b[4]
    d=c["Value"]
    print d

def g():
    a=data[6]
    b=a["Details"]
    c=b[1]
    d=c["Value"]
    print d
def h():
    a=data[5]["Details"]
    b=a[0]["Value"]
    print b
    
def main():
    f()
    g()
    h()

main()
    





