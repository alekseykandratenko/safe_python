import base64

with open('secret.key', 'rb') as key_file:
    key = key_file.read()
key_encoded = base64.b64encode(key)
print(f"key_encoded = {key_encoded}")
