import dominate
from dominate.tags import *
from datetime import datetime,timedelta
import os
import logging
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
logpath=os.path.join(THIS_FOLDER, 'Logs')
my_file = os.path.join(THIS_FOLDER, "html/index.html")
googlesheetlink ="https://docs.google.com/spreadsheets/d/12WmWC2CMwu0wS4Ub8dJwh3dikvfK0SpWYvLyCtRhnr8/edit#gid=1121993320"


def create_html_page(resources,days,sites):
    today=datetime.now().date()
    xdaysback=(datetime.now() - timedelta(days=days)).date()
    doc = dominate.document(title='Market Changes Weekly report')

    with doc.head:
        style("""\

body#body {
font-weight: 300;
line-height: 1.42em;
color:#A7A1AE;
}

#body h1 {
font-size:3em; 
font-weight: 300;
line-height:1em;
text-align: center;
}

#body h2 {
font-size:1em; 
font-weight: 300;
text-align: center;
display: block;
line-height:1em;
color: #FB667A;
}

#body h2 a {
font-weight: 700;
text-transform: uppercase;
text-decoration: none;
}


#body .main_table th  {
font-weight: bold;
font-size: 1em;
text-align: center;
color: #6dce12;
}


#body .main_table td {
font-weight: normal;
font-size: 1em;

}
#body .div_logo{
width: 50px;
height:  50px;   
margin-bottom: 20px;
background-size: 100% 100%;
margin-left: auto;
margin-right: auto;
}

#body .source_title{
text-decoration: underline;
display: block;

}

#body .center_logo_Chromeblog{
background-image :url('https://upload.wikimedia.org/wikipedia/commons/thumb/5/5f/Chromium_11_Logo.svg/240px-Chromium_11_Logo.svg.png');

}

#body .center_logo_Chromestatus{
background-image :url('https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Google_Chrome_icon_%28September_2014%29.svg/1200px-Google_Chrome_icon_%28September_2014%29.svg.png');

}

#body .center_logo_opera{
background-image :url('https://www.apnewsng.com/wp-content/uploads/2016/09/opera-mini-06-535x535.png');

}

#body .center_logo_opera_mobile{
background-image :url('http://1.bp.blogspot.com/-ijbpwYD-J4Y/UrfQo4bVpYI/AAAAAAAAABs/dkZWS0-IuJc/s320/Opera-Mobile-logo+(4).png');

}

#body .center_logo_webkit{
background-image :url('https://img.favpng.com/19/15/10/webkit-browser-engine-web-browser-safari-apple-png-favpng-gVu8mv7FjNU6x4FT6G4EcPpjc.jpg');

}

#body .center_logo_DevelopersGoogle
{
background-image :url('https://developers.google.com/web/images/web-fundamentals-icon192x192_96.png');
}


#body .center_logo_GoogleWebmaster
{
background-image :url('https://www.gstatic.com/images/branding/googlelogo/2x/googlelogo_color_150x54dp.png');
}

#body .header{
text-align: center;
padding-top: 55px;
}

#body h3.header.dates{
text-align: center;
padding-top: 0px;
padding-bottom: 20px;
}

#body .center_text{
text-align: center;
}

#body .main_table{
text-align: left;
overflow: hidden;
width: 75%;
margin: 0 auto;
display: table;
margin-bottom: 5%;
}

#body table{
border: 1px solid black;
display: inline-table;
}

#body .test-result-table {
border: 1px solid black;
}

#body .test-result-table-header-cell {

border-bottom: 1px solid black;
}

#body .test-result-step-command-cell {
border-bottom: 1px solid gray;
padding: 10px;

}

#body .main_table td {
font-weight: normal;
font-size: 1em;
}

#body .main_table td, .main_table th {
  padding: 10px;
}


#body .main_table tr {
background-color: rgb(178, 183, 174);
}

#body .main_table th {
background-color: #1F2739;
}

#body .main_table td { 
  color: black;
   }

#body .main_table  th.center_text {
text-align: center;
}

#body .main{
  border: 2px solid;
  margin: auto;
}
""")

    with doc.body:
        with doc:
            print(h1(Class='header').add(
                'Market Changes report for the last: '+ str(days) + ' days'))
            print(h3(Class='header dates').add(str(today) + " to " + str(xdaysback)))                   
        with div(Class="main"):
            for sources in resources:
                try:
                    if not ("twitter" in str(sources)):
                        print(h2(Class="source_title")(a)(sources[0],href=sites[resources.index(sources)], target="_blank"))
                        print(h3(Class='header dates').add(str(len(sources)-1) + " post/s"))
                        if(sources[0] == "Chromeblog"):
                            print(div(Class='div_logo center_logo_Chromeblog'))
                        if(sources[0] == "Chromestatus"):
                            print(div(Class='div_logo center_logo_Chromestatus'))
                        if(sources[0] == "Opera Mobile"):
                            print(div(Class='div_logo center_logo_opera_mobile'))
                        if(sources[0] == "Opera"):
                            print(div(Class='div_logo center_logo_opera'))
                        if(sources[0] == "Webkit"):
                            print(div(Class='div_logo center_logo_webkit'))
                        if(sources[0] == "Developers Google"):
                            print(div(Class='div_logo center_logo_DevelopersGoogle'))
                        if(sources[0] == "Google Webmaster"):
                            print(div(Class='div_logo center_logo_GoogleWebmaster'))

                    else:
                        if(len(sources)>1):
                            if("Failed" not in sources[1]):
                                print(h2(Class="source_title")(a)(sources[0],href="https://"+sources[0], target="_blank"))
                            else:
                                print(h2(Class="source_title").add(sources[0] + " Not found"))
                        elif(len(sources)==1):
                            print(h2(Class="source_title")(a)(sources[0],href="https://"+sources[0], target="_blank"))
                        else:    
                            print(h2(Class="source_title").add(sources[0]))
                        print(h3(Class='header dates').add(str(len(sources)-1) + " post/s"))
    
                    

                    

                    with table(Class='main_table'):
                        with thead():
                                if(len(sources) > 1 and ("Failed" not in sources[1])):
                                    print(th("Date"))
                                    print(th("Summary"))
                                elif (len(sources) == 2 and ("Failed"  in sources[1])) :
                                    print(th(Class='center_text').add("Failed to retrieve posts"))
                                    continue
                                else:
                                    print(th(Class='center_text').add("No Post for the last " + str(days) + " days"))
                                    continue
                                   
                        with tbody():
                            for post in sources:
                                if(isinstance(post, dict)):
                                    with tr():
                                        if not("Twitter" in sources[0] or type(post['date']) == str):
                                            print(td(Class='test-result-step-command-cell').add(
                                                str(post['date'].day)+"/" + str(post['date'].month)+"/" + str(post['date'].year)))
                                        else:
                                            print(td(Class='test-result-step-command-cell').add(post['date']))
                                        print(td(Class='test-result-step-command-cell')(a)(post['post'], href=post['link'], target="_blank"))
                except Exception:
                                 logger = logging.getLogger()
                                 logger.exception("Missing source to create html from") 

                                 
            print(h2('The days to retrieve back,email send to,twitter accounts(number of post) & filters can be changed')(
                a)("here", href=googlesheetlink, target="_blank"))
    t=str(doc).replace("<body>","<body id='body'>")
    f = open(my_file, "w")
    f.write(t)
    f.close()