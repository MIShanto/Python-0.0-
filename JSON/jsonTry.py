f = open("E://Python-0.0-//JSON//testJson.txt", "r")
s=f.read()
import json as js
fruits = js.loads(s)
print(fruits["quiz"]["sport"]["q1"])