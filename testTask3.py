import requests

word = requests.get('https://www.python.org').text

d = {}

for i in range(len(word)):
    if word[i] in d.keys():
        d[word[i]]+=1
    else:
        d[word[i]]=1

with open('readme.md','w') as f:
    for key, value in d.items():
        f.write(f'{key}, {value}\n')

# print(d)