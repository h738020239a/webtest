#class example

class User:
    #constructor, self ref to instance of class
    def __init__(self, email, name, password, current_job):
        self.email = email
        self.name = name
        self.password = password
        self.current_job = current_job
        
    def job_change(self, new_password):
        self.password = new_password
        
    
    

