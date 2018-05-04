import urllib2,json,base64
accesstoken="MDUXGF429RKLCPA8QLYS"
institution="10007772"
#page=1 (computing)
#page=4 (software Engineering)
page=0 #(accouting)
url="https://data.unistats.ac.uk/api/v4/KIS/Institution/{}/Courses.json?pageIndex={}".format(
    institution,
    page
    )
request=urllib2.Request(url)
request.add_header(
    "Authorization",
    "Basic "+ base64.encodestring(accesstoken+":").replace('/n','')
    )
response=urllib2.urlopen(request)
data=json.load(response)
for c in data:
    print c["KisCourseId"],c["Title"]
