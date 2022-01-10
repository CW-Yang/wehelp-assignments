import json
import urllib.request as req
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with req.urlopen(src) as response:
    data = json.load(response)

def strSplit(str):
    i = str.find('jpg')
    if(i != -1 and i < 180):    # 圖片檔案 jpg 與 JPG 都有
        str = str[0:i+3]
    else:
        i = str.find('JPG')
        str = str[0:i+3]
    return str

myList = data["result"]["results"]
with open("data.csv", "w", encoding="utf-8") as file:
    for name in myList:
        a = name["stitle"]
        b = name["address"][5:8]
        c = name["longitude"]
        d = name["latitude"]
        e = strSplit(name["file"])
        
        file.write(f"{a},{b},{c},{d},{e}"+"\n")
