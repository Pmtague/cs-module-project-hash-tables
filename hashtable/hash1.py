table = [None] * 8

def find_index(key):
	return key % len(table)

def put(key, value):
	index = find_index(key)  # index should be 0...7
	table[index] = value

def get(key):
	index = find_index(key)
	return table[index]

put(3490, "my value")
put(3492, "another value")

v = get(3490)

if v is not None:
	print(v)
else:
	print("Couldn't find key!")

print(get(3490))
print(get(3492))
print(get(3494))