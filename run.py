import subprocess
import json
import time

id_tweet_label_new = []
f2 = open("id_tweet_label.txt", "a")
f1 = open("all.txt", "r")

all_d = f1.readlines()
all_d = [x.strip().split(" ") for x in all_d]

for i in range(len(all_d)):
  if i > 7119:
    x = subprocess.run(["./run.sh", all_d[i][0]], capture_output=True)
    y = (x.stdout).decode("utf-8")
    z = json.loads(str(y))
    print(z)
    try:
      s = z['data']
      res = str(all_d[i][0]) + " "+ "\""+s['text']+"\""+" "+str(all_d[i][1]+"\n")
      f2.write(res) 
      time.sleep(2)
    except:
       print(all_d[i][0]," ERROR")
       f2.write("ERROR\n")