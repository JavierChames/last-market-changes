from googlesheet import googlesheet as retrievegs
import logging
import os

sh = retrievegs.googlesheetconnection()
sheet = sh.worksheet("Filters")
sites = sheet.col_values(1)[1:]
filterenabled = sheet.col_values(2)[1:]
filtercontent = sheet.col_values(3)[1:]
logpath=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Logs'))



def filterposts(data):#filter post by text,the text retireved from google sheets
    if len(data) >1:
        try:
            filtered_array = [data[:1]]
            index = sites.index(data[0].upper())


            if (len(filtercontent) == 0):
                for i in range(len(filterenabled)):
                    filtercontent.append("")
            else:
                for i in range(len(filterenabled))[len(filtercontent):]:
                    filtercontent.append("")

            tmp_arr = sites[index], filterenabled[index], filtercontent[index]

            if (tmp_arr[1]) == "TRUE" and (filtercontent[index] != ''):
                if(len(tmp_arr[2].split(",")) == 1):
                    for words in data[1:]:
                        if (filtercontent[index].upper() in words['post'].upper()):
                            filtered_array.append(words)
                    return filtered_array

                if(len(tmp_arr[2].split(",")) >= 2):
                    for words in data[1:]:
                        for filters in tmp_arr[2].split(","):
                            if (filters.upper() in words['post'].upper()):
                                filtered_array.append(words)
                        return filtered_array
            else:
                return data
        except Exception :
                            logger = logging.getLogger()
                            logging.basicConfig(filename=logpath+"\\error.log", format='%(filename)s: %(message)s', filemode='w')
                            logger.exception("Problem retriving filter")
                            data.append("Problem retrieving filter")
                            return data
    return data

