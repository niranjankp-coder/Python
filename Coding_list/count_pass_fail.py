# Count PASS and FAIL from Logs
logs = ["PASS","FAIL","PASS","PASS"]

data = {}
for res in logs:
  if res not in data:
    data[res] = logs.count(res)
print(f" Result is: {data}")

'''
Result is: {'PASS': 3, 'FAIL': 1}

'''
