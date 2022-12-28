import csv
file = "names.csv"
rows = []
names = []
with open(file, 'r') as csvfile:
  reader = csv.reader(csvfile)
  for x in reader:
    rows.append(x)

for row in rows:
  name = row[0].lower()
  names.append(name)
  
print("scraped")


def getFem(username):
  lol = username.replace("_", "")
  lol = lol.replace(".", "")
  for x in names:
    if x in lol and x == "":
      pass
    elif x in lol or lol in x:
      print(f"[log] detected {username}")
      return

getFem()
