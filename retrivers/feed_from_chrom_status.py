import urllib.request, json 
import dateutil.parser
from googlesheet import googlesheet as retrievegs
sh=retrievegs.googlesheetconnection()

def getposts(site):
    data=[]
    data.append("Chromestatus")
    try:
        with urllib.request.urlopen(site) as url:
            jsondata = json.loads(url.read().decode())
        

        for post in jsondata:
                    data.append({'date':str(dateutil.parser.parse(post['updated']['when']).date().strftime('%d/%m/%Y')),
                        'post':post['name'],
                        'link': "https://www.chromestatus.com/feature" + "/" + str(post['id'])})
        return data
    except:
        data.append("Failed to retrieve posts")
        return data
        
        