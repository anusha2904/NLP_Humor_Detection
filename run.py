import subprocess
import json
import time

id_tweet_label_new = []
f2 = open("id_tweet_label.txt", "w")
f1 = open("all.txt", "r")

all_d = f1.readlines()
all_d = [x.strip().split(" ") for x in all_d]

for i in all_d:
  x = subprocess.run(["./run.sh", i[0]], capture_output=True)
  y = (x.stdout).decode("utf-8")
  z = json.loads(str(y))
  print(z)
  try:
    s = z['data']
    res = str(i[0]) + " "+ "\""+s['text']+"\""+" "+str(i[1]+"\n")
    f2.write(res) 
    time.sleep(2)
  except:
     print(i[0]," ERROR")
     f2.write("ERROR\n")