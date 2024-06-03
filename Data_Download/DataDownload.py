import key, pathlib

AFL= 'Data_Download/'+'AFL'

p = pathlib.Path(AFL)

p.mkdir(parents=True, exist_ok=True)

fn = "test.txt"

result = str([1,2,3])

filepath = p / fn
with filepath.open("w", encoding ="utf-8") as f:
    f.write(result)