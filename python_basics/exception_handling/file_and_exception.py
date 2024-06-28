try:
    file = open('example.txt','r')
    content = file.read()
    a = b
    print(content)
except FileNotFoundError as ex:
    print(ex)
except Exception as ex1:
    print(ex1)
finally:
    if 'file' in locals() or not (file.closed()):
        file.close()
        print("file closed")
    
    