import Model
class Controller:
    def __init__(self,cred_file):
        self.model = Model.Model()
        self.cred_file = cred_file
        self.gauth=None
    def authenticator(self):
        self.gauth=self.model.authenticator(self.cred_file)
        return self.gauth
    def backup(self,filelist):
        self.model.backup(filelist,self.gauth)
    def setbackup(self,dirname,frequency):
        self.model.log(frequency,dirname)
        self.model.setbackup(dirname,self.gauth)
        
    def organizer(self,path):
        self.model.organizer(path)

    def cleaner(self,path):
        count,dcount=self.model.cleaner(path)
        return count,dcount



        

        
