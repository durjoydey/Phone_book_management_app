contact={}
filename='test.txt'
z=0
name = []
phone = []
address = []
email = []
flag=0;
def display_contact():
    i=len(name)
    y=i-z
    print("Name\t\tContact Number\t\tAddress\t\tEmail")
    for x in range(y):
        print(name[x],"\t\t",phone[x],"\t\t",address[x],"\t\t",email[x])

while True:
 choice= int(input("1.Add New Person\n 2.Search Contact\n 3.Display Contact\n 4.Edit Contact\n 5.Delete Contact\n 6.File Open\n 7.Exit\n Enter Your Choice:"))
 
 if choice ==1:
     name.append(str(input("Enter Name: ")))
     phone.append(int(input("Enter Number: ")))
     address.append(str(input("Enter Address: ")))
     email.append(str(input("Enter Email: ")))
     
 elif choice == 2:
     search_name= input("Enter the name:")
     i=len(name)
     for x in range(i):
         if name[x] == search_name:
             print(search_name,"'s contact number is",phone[x], ",address is",address[x], "and email is",email[x])
             flag=1
     if flag == 0:
         print("Name wasn't found")
             
 elif choice==3:
    
          display_contact()
          
 elif choice==4:
    n= int(input("1.Edit name\n 2.Edit number \n 3.Edit address \n 4.Edit email\n Enter Your Choice:"))
    if n == 1: 
       edit_name=input("Enter the name you want to edit:")
       i=len(name)
       for x in range(i):
          if name[x] == edit_name:
             name[x]=str(input("Enter new name:"))
             flag=1
             display_contact()
       if flag == 0:
          print("Name isn't found in your contact book")
    elif n == 2: 
       edit_name=input("Enter the name you want to edit:")
       i=len(name)
       for x in range(i):
          if name[x] == edit_name:
             phone[x]=int(input("Enter new number:"))
             flag=1
             display_contact()
       if flag == 0:
          print("Number isn't found in your contact book")
    elif n == 3: 
       edit_name=input("Enter the name you want to edit:")
       i=len(name)
       for x in range(i):
          if name[x] == edit_name:
             address[x]=str(input("Enter new address:"))
             flag=1
             display_contact()
       if flag == 0:
          print("address isn't found in your contact book") 
    elif n == 4: 
       edit_name=input("Enter the name you want to edit:")
       i=len(name)
       for x in range(i):
          if name[x] == edit_name:
             email[x]=str(input("Enter new email:"))
             flag=1
             display_contact()
       if flag == 0:
          print("Email isn't found in your contact book")
    
 elif choice==5:
        contact = str(input("Enter the contact you want to delete:"))
        i=len(name)
        for x in range(i):
            if name[x] == contact:
                if x == i-1:
                    z+=1
                else:       
                    name[x]=name[x+1]
                    phone[x]=phone[x+1]
                    address[x]=address[x+1]
                    email[x]=email[x+1]
                    z+=1
 elif choice==6:
        with open(filename,'a') as file_object:
             file_object.write("i love Programming")

 else:
    break