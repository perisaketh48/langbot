import requests
import numpy as np
import re
import json

# URL That has all the urls of MD file
url="https://docs.langchain.com/llms.txt"

try:
    # Line to Get the Data from the response
    response = requests.get(url)

    # To Know all the objects that are present in the response
    # print(dir(response)) 

    # we have all the text in the response.text
    #store the text in a variable

    data=response.text

    matches = re.findall(r"https://docs\.langchain\.com/(.*?)\.md", str(data))

    data_object=[]
    count=0

    for i in matches:
        url=f"https://docs.langchain.com/{i}.md"
        response=requests.get(url)

        data_object.append({"url":response.url,"content":response.text})
        count+=1
        print(count)

    with open(r"C:\GenAi\LangBot\langchain_document.json", 'w') as json_file:
        json.dump(data_object,json_file,indent=4)


except Exception as err:
    print("ERROR",err)
