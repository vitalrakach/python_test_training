import json
import requests

url = "https://test-pgo.h4h.io/pgo/user-management/patients?size=20"

payload={}
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJZMk1kWksxd1lsOXRwbnJwdUVCSnlYelZzaUNFT1ZocEE2blFsTXR2bGVRIn0.eyJleHAiOjE2NDM5NjUzNTQsImlhdCI6MTY0Mzg3ODk1NCwianRpIjoiZTkxMTI4ODEtNWJlMy00NmIwLWEwNDYtYzdlNGFiMWIwODE2IiwiaXNzIjoiaHR0cHM6Ly90ZXN0LXBnby5oNGguaW8vYXV0aC9yZWFsbXMvcGdvLWNjbiIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiI3OWE1MzFjMS04OTA0LTRkYTUtOGI1OS1iMjYzYWNmNDAwYzIiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJwZ28tYmFja2VuZCIsInNlc3Npb25fc3RhdGUiOiJmMWE1MWExNC1mNDJhLTQxODAtYWJhMi03YjExNWNhZDE5NGMiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwiQURNSU4iLCJ1bWFfYXV0aG9yaXphdGlvbiIsIlVTRVIiXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbIm1hbmFnZS1hY2NvdW50IiwibWFuYWdlLWFjY291bnQtbGlua3MiLCJ2aWV3LXByb2ZpbGUiXX19LCJzY29wZSI6Im9wZW5pZCBlbWFpbCBwcm9maWxlIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInByZWZlcnJlZF91c2VybmFtZSI6InYucmFrYWNoK2RldnBnb0BoZWFydGZvcmhlYWx0aC5jb20iLCJsb2NhbGUiOiJubCIsImVtYWlsIjoidi5yYWthY2grZGV2cGdvQGhlYXJ0Zm9yaGVhbHRoLmNvbSJ9.UfqdJsRxhISbCXrBvv8duZu_q3oDElol6k3hfWfVDyK2v-KE1NVW_ttDRoo5f4sEHTsph-IJABd72-stcDlrJSO2-gzY5G6J4y9MVNpkLdRkecup4fz9RXgekCmlUlGuOJ0cjElvBYTfJY0gjYjj6Jgh4X__5ePmq9oxWu2UdQ3yo_l3RXF133i5CWcSNiv6C3ctUn2_rNQpHIxmj0qnwH8KEKln-PoRoVfkG7XElaYPpMV1jLUNd-cq5b86NWv9acvV7gfN7TiFrhlDdZww6KofybpDzXWZStvxT4M1w9PcIvoba7lgCVbTEwTaeu2ynhotmtJ7uhgmfFUQ4PCSvw',
  'Cookie': 'JSESSIONID=BBF806375A76F2DF861F4317CA4B5DB7'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.status_code)

if response.status_code == 200:
  #response to python object
  jsonDataResp = response.json()
  print(type(jsonDataResp))
  print(len(jsonDataResp))
  # print(json.dumps(jsonDataResp, indent=3))
  #convert to text
  jsonData = json.dumps(jsonDataResp)
  print(type(jsonData))

  a='asd'
  print(a.__contains__('sd'))

  count_notFound = 0
  for i in jsonDataResp['content']:
    #set id =100 if condition is true (firstName contains substring)
    if str(i['firstName']).__contains__("qwerty") and i['dateOfBirth'] == "1957-07-08":
      print("Found match: " + "'" + i['firstName'] + " " + i['dateOfBirth'] + "'.")
      print(i['firstName'])
      i['id'] = '100'
      break
    else:
      count_notFound +=1
  if count_notFound > 0:
    print("Patient with lastName 'qwerty' is no found")
  #print(jsonDataResp['content'])

  #json to string (like json stringfy Where indent is количество отступов)
  jsonDataString = json.dumps(jsonDataResp, indent=3)
  # print(jsonDataString)

  idArr = []
  for i in jsonDataResp['content']:
    idArr.append(i['firstName'])

  jsonDataResp['content'] = idArr
  arr = [1, 2, 3, 4, None]
  arr2 = [None, 2, 3, 4, 1]



  print(type(jsonDataResp['content']))
  #for k in jsonDataResp['content']:
  #set id =100 if condition
  #jsonDataResp['content']
  # print(k)
  #   i['id'] = '100'
  #   break
  print(jsonDataResp['content'][0])


  #print(jsonDataResp)
else:
  print("Response is: " + str(response.status_code))



