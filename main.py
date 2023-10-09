import pygsheets
import pandas as pd
#main_json is just an example of what the dictionnairy should look like
main_json={
    "login":{

    },
    "Teams":{
        "Emanuel":{
            "name":"Karim",
            "last_name":"lazghab",
            "pres":True,
            "cin":12345678,
        },
        "Tactic":{
            "name":"Melek",
            "last_name":"Khdira",
            "pres":False,
            "cin":87654321,
        },
        "Mazinos":{
            "name": "Mazen",
            "last_name": "aaouini",
            "pres": True,
            "cin": 54632178,

        }
    }
}

# the service_file should be a path to a json file that is made using this video(from  to 5:05):https://www.youtube.com/watch?v=ZVfzDOWiOQ0

gc = pygsheets.authorize(service_file='silicon-garage-278511-bf125cd90f67.json')# 'silicon-garage-278511-bf125cd90f67.json' is my path to the json file

sh = gc.open('robocup test') #the parameter MUST be the same name that you fixed in the google sheet 

wks = sh[0] #this selects the first worksheet

df=pd.DataFrame(data=main_json["Teams"])

wks.set_dataframe(df,(1,2)) #(1,2) means :start from column 1 row 2
#the google sheet should be closed 
