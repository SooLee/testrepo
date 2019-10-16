import os

haha = os.getenv('HAHA')
if haha:
  print(haha)
else:
  raise Exception("environment variable HAHA not recognied")
