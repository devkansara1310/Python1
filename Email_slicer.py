#Email Slicer (Username, Domain) 

email = input("Enter Your Email: ").strip()
username = email[:email.index("@")]
domain=email[email.index("@")+1:]
print("User Name:",username)
print("Domain Name:",domain)
