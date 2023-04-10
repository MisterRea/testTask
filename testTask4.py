import json
import datetime

with open('hh.json') as f:
    jsonStr = json.load(f)

def search(dataStr):
    for key, _ in dataStr.items():
        # print(key)
        if key == 'ID':
            dataStr[key] = datetime.datetime.now().isoformat()
            # print('Updated')
        else:
            try:
                search(dataStr[key])
            except:
                pass
    return dataStr
    
        
a = search(jsonStr)

with open('hb.json','w') as f:
    json.dump(a,f,indent=4)


# print(jsonStr)