def xau(n):
    t = ""
    '''
    for i in n:#"Trương"
        if len(i) > len(t):
            t = i#t = "Trương"
            
    '''
    t = max(n, key = len)
    #'''
    return t

n = input("Nhập xâu n: ").split()#Trương Thị Minh Kiều
#-> ["Trương", "Thị", "Minh", "Kiều"]
print(f"Xâu dài nhất là: {xau(n)}")
