password=input("enter a password -")
if password>="1" and password<="8":
    if "$,_,%"in password or "@,&" in password or "#,*" in password:
        if "0"or"9"in password :
            if "A"or"Z" in password:
                print ("strong password")
            else:
            	print("weak password")
        else:
        	print("wrong password")
    else:
    	print("wrong")
else:
	print("nothing")