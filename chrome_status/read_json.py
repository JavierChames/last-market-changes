import urllib.request, json 
with urllib.request.urlopen("https://www.chromestatus.com/features_v2.json") as url:
    data = json.loads(url.read().decode())
    # print(len(data))
    for post in data:
        print(post['updated']['when'] + " "+  post['name'])
        # print()