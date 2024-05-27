def email():
    emailid=input("Enter your email ID:")
    emailid=emailid.lower()
    user=""
    if emailid.endswith(".com") and "@" in emailid:
        for i in emailid:
            if i != "@":
                user+=i
            else:
                break
        domain=emailid[len(user)+1:]
        if user!="" and len(domain)>4:
            print()
            print("User name:",user)
            print("Domain name:",domain)
        else:
            print()
            print("Enter a valid email ID!!")
            print()
            email()
    else:
        print()
        print("Enter a valid email ID!!")
        print()
        email()
email()