class Instagram:
    __password ="nishant1234"
    __follower = 100
    def change_password(self,old ,new):
        if old ==self.__password:
           self.__password= new
           print("change the password ")
        else:
            print("Wrong password")
    def add_follower(self):
        self.__follower +=1
        print(self.__follower)
    def get_follower(self):
        print(f"{self.__follower}")
    
I=Instagram()
I.change_password("nishant1234","Nishant1234")
I.add_follower()
I.get_follower()