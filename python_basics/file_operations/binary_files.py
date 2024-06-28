data = b'\x00\x01\x02\x03\x04'
with open('example.bin', 'wb') as file:
    file.write(data)
    
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)