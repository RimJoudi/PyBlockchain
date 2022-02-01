import hashlib
h = hashlib.sha256()
h.update('a'.encode('utf-8'))
print(h.hexdigest())

h = hashlib.sha256()
i = 0
h.update(str(i).encode('utf-8'))
h.hexdigest()
print(h.hexdigest())
