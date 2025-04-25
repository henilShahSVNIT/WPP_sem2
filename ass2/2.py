ch='y'
d={} #empty dictionary
while ch=='y':
    str=input("Enter product name : ")
    val=int(input("Enter price : "))
    d.update({str:val}) #stored in d (str as key)(value as value)
    ch=input("to enter more press y else n ")
ch='y'
while ch=='y':
    str=input("Enter product name to be searched ")
    if str in d:
        print("Value : ",d[str])
    else:
        print("The product is currently not available ")
    ch=input("to search more press y else n ")