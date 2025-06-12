class Username:
	name="Venky"
	password=1234
	def login(self):
		print("\n ******WELCOME TO LOGIN PAGE****** \n")
		user=input("Enter the user_name					: ")

		security_code=int(input("enter the pass		 				: "))

		print("password is :",self.password)
		print("you enter password is:",security_code)

		if user==self.name :
			print("you enter password is:",security_code,type(security_code))
			print("password is :",self.password,type(self.password))
			print(security_code==self.password)

			if security_code==self.password:
				print(" you are login is successful")
			else:
				print("your pass is incorrect")
		else:
			self.sign_up()
	@classmethod
	def sign_up(cls):
		print("\n****** WELCOME TO SIGNUP PAGE ******\n") 
		NEW_USER=input("CREATE USERNAME  TO LOGIN        			: ")
		email=input("Enter your email               	 			: ")
		phone_no=(input("enter the your contact number	 			:"))

		user_password=int(input("Create a password for security 	 			:"))

		Confirm_password=int(input("Re-enter the password  		 			:"))	
		if user_password==Confirm_password:
				cls.password=user_password
				#print("password is :",cls.password)
		else:
			print("sorry we con't create")
		cls.name=NEW_USER
		print("password is :",cls.password)

		cls.login(cls)

			
				
		
		
	
l=Username()
l.login()
