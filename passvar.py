class PasswordVal:
    def __init__(self,passwd):
        
        self.passwd=passwd



    def validate(self):
        check_length =  self.check_length()
        check_num = self.check_num()
        check_pt = self.check_pt()
        check_space = self.check_space()

    

    def check_length(self):
        if len(self.passwd) < 5:
            print('Password is less than 5--',end='')
            print('True')
            return True

        elif len(self.passwd) >= 10:
            print('Password is more than 10--',end='')
            
            print('True')
            return True

        
    def check_num(self):
        if self.passwd.isalpha():
            print('Password Dont Have at least 1 number--',end='')    
            print('True')
            return True
        
        
    def check_pt(self,):
        import string
        punctuation = list(string.punctuation)
        if any(char in punctuation for char in self.passwd):
            pass
            return False
        else:
            print('Password does not have special Char--',end='')
            print('True')
            return True

    def check_space(self,):
        if ' ' in self.passwd:
            print('Password contain space--',end='')
            
            print('True')
            return True
        # else:
            
        #     print('False')
        #     return False
