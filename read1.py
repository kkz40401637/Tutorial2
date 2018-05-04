import urllib2,json,base64

accesstoken = "MDUXGF429RKLCPA8QLYS"
#url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/10003270.json" (Imperial College London)
#url = "http://data.unistats.ac.uk/api/v4/KIS/Institution/10007800.json" #(University Of The West Of Scotland)

request = urllib2.Request(url)
request.add_header(
	"Authorization",
	"Basic " + base64.encodestring(accesstoken+":").replace('\n','')
	)
response = urllib2.urlopen(request)
data = json.load(response)
print data['Name']
