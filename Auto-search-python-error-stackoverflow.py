import re
import subprocess
import requests
import json
import webbrowser

def find_error(file_name,num_queries):
    error_key = ""
    call = subprocess.Popen(['python3',file_name], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out,err = call.communicate()
    error = str(err.decode('utf8')).split()
    string = ' '.join(map(str,error))
    match = re.search("Error:",string)
    if match:
        error_message = string[match.end()+1:]
        sp = str(error_message).split(" ")
        error_key1 = error[len(error)-len(sp)-1]
        error_key = error_key1[:len(error_key)-1]
        print(f"{error_key}: {error_message}")
        URL = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&site=stackoverflow"
        PARAMS = {'intitle': [error_message,error_key], 'pagesize': num_queries}
        r = requests.get(url = URL, params = PARAMS)
        data = r.json()

        for i in range(0,num_queries):
            link = str(data["items"][i]["link"])
            webbrowser.open(link)
    else:
        print("No error found")

find_error("sample.py", 2)

