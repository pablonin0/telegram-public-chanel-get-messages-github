from telethon.sync import TelegramClient
import datetime
import pandas as pd
import configparser
import re


config = configparser.ConfigParser()
config.read("telethon.config")


api_id = 12345 
api_hash = "#"


chats = ['#'] #name of the chanel to analyze


#client =  TelegramClient('test', api_id, api_hash)


df = pd.DataFrame()


for chat in chats:
    with TelegramClient('test', api_id, api_hash) as client:    
        for message in client.iter_messages(chat, offset_date=datetime.date.today() , reverse=True):
            print(message)
        
            def PVPresult(): 
                PVP = re.search(r"(?<=\:\s)\d+", message.text)
                
                if PVP is None:
                    return "None"
                else:
                    return PVP.group(0)
                
            def EurResult(): 
                priceeur = re.search(r"([1-9][0-9]{,2}(,[0-9]{3})*|[0-9]+)(\.[0-9]{1,9})?[€|$]", message.text)
                
                if priceeur is None:
                    return "None"
                else:
                    return priceeur.group(0)
                   


            data = { "group" : chat, "sender" : message.sender_id, "text" : message.text, "date" : message.date ,"PVP" : PVPresult(), "PrecioFinal": EurResult() }

            temp_df = pd.DataFrame(data, index=[1])
            df = df._append(temp_df)

#something i could do to avoid scrapeing to all the messages to add to the data sheet is to 
# check the date of prevoius message and form that point 

#agarra lo que esta antes de euro o moneda \d+(?=[€|$])
#solo agarra lo que esta depues de PVP

#regex para PVP:  es \PVP:(\s|\d)\d{1,5}(\€|\$)   
#regex para precio del descuento es \d{1,5}(\€|\$)\*\*
df['date'] = df['date'].dt.tz_localize(None)

print(df)

df.to_excel("C:\\..\\..\\..\\telegram public chanel get messages github\\data7_{}.xlsx".format(datetime.date.today()), index=False)


