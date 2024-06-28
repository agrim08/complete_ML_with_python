with open('example.txt','w+') as file:
    file.write("Hello World \n")
    file.write("Hello Again \n")
    
    #Move the file cursor to the biginning
    file.seek(0)
    
    #reading:
    content = file.read()
    print(content)