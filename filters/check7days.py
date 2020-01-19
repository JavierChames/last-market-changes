from datetime  import datetime,timedelta
import dateutil.parser

def retrieve_post_from_last_week(last_post,days,site):

    arr_special_date_format=["Chromestatus","twitter"]
    if any(keyword in site for keyword in arr_special_date_format):
        last_post1= datetime.strptime(str(last_post), '%d/%m/%Y').date()
    else:
        last_post1 = dateutil.parser.parse(str(last_post)).date()
    current_date =(datetime.today()- timedelta(days=days)).date()
    if (last_post1 >= current_date):
        return True