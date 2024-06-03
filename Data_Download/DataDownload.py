import key, pathlib, requests

url = "https://v1.afl.api-sports.io/status"

payload={}
headers = {
        'x-apisports-key': key.API_key
    }

response = requests.request("GET", url, headers=headers, data=payload).json()

print(response)

# AFL= 'Data_Download/'+'AFL'

# p = pathlib.Path(AFL)

# p.mkdir(parents=True, exist_ok=True)

# fn = "test.txt"

# result = str([1,2,3])

# filepath = p / fn
# with filepath.open("w", encoding ="utf-8") as f:
#     f.write(result)