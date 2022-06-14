contact={}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
 choice= int(input("1.Add New Person\n 2.Search Contact\n 3.Display Contact\n 4.Edit Contact\n 6.Exit\n Enter Your Choice:"))
 if choice ==1:
     name = input("Enter Name:")
     phone= input("Enter Phone Number:")
     address = input("Enter Address:")
     email = input("Enter Email:")
     contact[name]=phone
 elif choice == 2:
     search_name= input("Enter the Name:")
     if search_name in contact:
         print(search_name,", contact number is",contact[search_name])
     else:
         print("Name wasn't found")
 elif choice==3:
      if not contact:print("Contact Book is Empty")
      else:
          display_contact()
 elif choice==4:
      edit_contact=input("Enter the contact you want to edit:")
      if edit_contact in contact:
          phone=input("Enter Mobile Number:")
          contact[edit_contact]=phone
          display_contact()
      else:
          print("Name isn't found in your contact book")
 elif choice==5:
        del_contact = input("Enter the contact you want to delete:")
        if del_contact in contact:
            confirm=input("Are you sure you want to delete this y/n?")
            if confirm=='y' or confirm=='Y':
                contact.pop(del_contact)
                display_contact()
            else:
                print("Name isn't found in your contact book")
        else:
            break







