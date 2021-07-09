#MODULES FOR ORGANIZER
from watchdog.observers import Observer
import time
from datetime import datetime
from pathlib import Path
from watchdog.events import FileSystemEventHandler
import os
import os.path
import json
import shutil
#MODULES FOR BACKUP
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
#MODULES FOR CLEANER
#DATABASE CONNECTIVITY
import  sqlite3
import hashlib
import os
import stat


FILE_FORMATS={'.html5': 'HTML', '.html': 'HTML', '.htm': 'HTML', '.xhtml': 'HTML', '.jpeg': 'IMAGES', '.jpg': 'IMAGES', '.tiff': 'IMAGES', '.gif': 'IMAGES', '.bmp': 'IMAGES', '.png': 'IMAGES', '.bpg': 'IMAGES', 'svg': 'IMAGES', '.heif': 'IMAGES', '.psd': 'IMAGES', '.avi': 'VIDEOS', '.flv': 'VIDEOS', '.wmv': 'VIDEOS', '.mov': 'VIDEOS', '.mp4': 'VIDEOS', '.webm': 'VIDEOS', '.vob': 'VIDEOS', '.mng': 'VIDEOS', '.qt': 'VIDEOS', '.mpg': 'VIDEOS', '.mpeg': 'VIDEOS', '.3gp': 'VIDEOS', '.oxps': 'DOCUMENTS', '.epub': 'DOCUMENTS', '.pages': 'DOCUMENTS', '.docx': 'DOCUMENTS', '.doc': 'DOCUMENTS', '.fdf': 'DOCUMENTS', '.ods': 'DOCUMENTS', '.odt': 'DOCUMENTS', '.pwi': 'DOCUMENTS', '.xsn': 'DOCUMENTS', '.xps': 'DOCUMENTS', '.dotx': 'DOCUMENTS', '.docm': 'DOCUMENTS', '.dox': 'DOCUMENTS', '.rvg': 'DOCUMENTS', '.rtf': 'DOCUMENTS', '.rtfd': 'DOCUMENTS', '.wpd': 'DOCUMENTS', '.xls': 'DOCUMENTS', '.xlsx': 'DOCUMENTS', '.ppt': 'DOCUMENTS', 'pptx': 'DOCUMENTS', '.a': 'ARCHIVES', '.ar': 'ARCHIVES', '.cpio': 'ARCHIVES', '.iso': 'ARCHIVES', '.tar': 'ARCHIVES', '.gz': 'ARCHIVES', '.rz': 'ARCHIVES', '.7z': 'ARCHIVES', '.dmg': 'ARCHIVES', '.rar': 'ARCHIVES', '.xar': 'ARCHIVES', '.zip': 'ARCHIVES', '.aac': 'AUDIO', '.aa': 'AUDIO', '.dvf': 'AUDIO', '.m4a': 'AUDIO', '.m4b': 'AUDIO', '.m4p': 'AUDIO', '.mp3': 'AUDIO', '.msv': 'AUDIO', 'ogg': 'AUDIO', 'oga': 'AUDIO', '.raw': 'AUDIO', '.vox': 'AUDIO', '.wav': 'AUDIO', '.wma': 'AUDIO', '.txt': 'PLAINTEXT', '.in': 'PLAINTEXT', '.out': 'PLAINTEXT', '.pdf': 'PDF', '.py': 'PYTHON', '.xml': 'XML', '.exe': 'EXE', '.sh': 'SHELL'}
DIRECTORIES = {
        "HTML": [".html5", ".html", ".htm", ".xhtml"],
        "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
                   ".heif", ".psd"],
        "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
                   ".qt", ".mpg", ".mpeg", ".3gp"],
        "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                      ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                      ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                      "pptx"],
        "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                     ".dmg", ".rar", ".xar", ".zip"],
        "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
                  ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
        "PLAINTEXT": [".txt", ".in", ".out"],
        "PDF": [".pdf"],
        "PYTHON": [".py"],
        "XML": [".xml"],
        "EXE": [".exe"],
        "SHELL": [".sh"]

    }
'''class MyHandler(FileSystemEventHandler):
    
    def organizer(self,path):
        for entry in os.scandir(Path(path)):
            print(entry.name)
            if entry.is_dir():
                print("Yes")
                continue
            file_path = Path(entry)
            print(file_path)
            file_format = file_path.suffix.lower()
            print(file_format)
            if file_format in FILE_FORMATS:
                directory_path = Path(path.joinpath(FILE_FORMATS[file_format]))
                print(directory_path)
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path.name))
                print(file_path)

            for dir in os.scandir(path):
                try:
                    os.rmdir(dir)
                except:
                    pass
        pass
	def on_modified(self,event):
        self.organizer(path)

'''
class Model():

    def __init__(self):
        try:
            self.con = sqlite3.connect("fileeazee1.sqlite")
            self.cursor = self.con.cursor()
            print("yup")
            self.cursor.execute("create table IF NOT EXISTS set_backup(fpath varchar2(200),ufrequency integer,last_modified text);")
            print("Table created successfully")
            self.old_files=[]
            self.large_files=[]

        except Exception as E:
            print(E)


        pass

    def organizer(self,path):
        for entry in os.scandir(Path(path)):
            print(entry.name)
            if entry.is_dir():
                print("Yes")
                continue
            file_path = Path(entry)
            print(file_path)
            file_format = file_path.suffix.lower()
            print(file_format)
            if file_format in FILE_FORMATS:
                directory_path = Path(Path(path).joinpath(FILE_FORMATS[file_format]))
                print(directory_path)
                directory_path.mkdir(exist_ok=True)
                file_path.rename(directory_path.joinpath(file_path.name))
                print(file_path)

            for dir in os.scandir(Path(path)):
                try:
                    os.rmdir(dir)
                except:
                    pass

    def backup(self,file_list,gauth):
        drive = GoogleDrive(gauth)
        for file in file_list:
            file2upload = drive.CreateFile()
            if(os.path.isfile(file)):
                filename=os.path.basename(file)
                file2upload.SetContentFile(file)
                file2upload['title'] = filename
                file2upload.Upload()

    def setbackup(self,dir_name,gauth):
        drive = GoogleDrive(gauth)
        file_list = os.listdir(dir_name)
        for file in file_list:
            path = dir_name + '/' + file
            file2upload = drive.CreateFile()
            if(os.path.isfile(path)):
                filename=os.path.basename(path)
                file2upload.SetContentFile(path)
                file2upload['title'] = filename
                file2upload.Upload()
    def log(self,frequency,dir_name):
        print("patel harami")

        curdate = datetime.now()
        # oldate=f.readline(1)
        #           if datetime(oldate).date() < curdate.date():
        #for file in os.listdir(curdir):
        #    if(file=="log.txt"):
        sql = "insert into set_backup values(:path,:frequency,:last_modified)"
        self.cursor.execute(sql,[dir_name,frequency,curdate])
        self.con.commit()
        a=self.cursor.fetchall()
        for i in a:
            print(i)

    def autouploader(self):
        curdir=os.getcwd()
        for file in os.listdir(curdir):
            if(file=="log.txt"):
                pass







        with open("log.txt",'wb') as f:




            pass
    
    def authenticator(self,credfile):#credfile = "filename.txt"
        gauth = GoogleAuth()
        try:
            gauth.LoadCredentialsFile(credfile)
        except:
            pass

        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved creds
            gauth.Authorize()
        # Save the current credentials to a file

        gauth.SaveCredentialsFile("credfile.txt")
        return gauth


    def cleaner(self,path):

        file_list = os.listdir(path)

        unique = dict()
        count = len(file_list)
        ##########
        # for counting the number of files deleted
        ##########
        dcount = 0
        size = 0


        for file in reversed(file_list):
            print("beginning of")

            file_name = Path(os.path.join(path, file))
            print(file_name)
            #file_size = int(os.path.getsize(file_name))
            #if file_size > (2000000000):
            #    self.large_files.append(file_name)
            fileStatsObj = os.stat(file_name)
            accessTime = time.ctime(fileStatsObj[stat.ST_ATIME])


            if int(accessTime[-4:])==int(datetime.now().strftime("%Y")):
                self.old_files.append(file_name)

        try:
            for i in self.old_files:
                print(i)
        except:
            pass



        print(f"Number of existing files:{count}")

        for file in reversed(file_list):
            file_name = Path(os.path.join(path, file))
            file_size = int(os.path.getsize(file_name))

            if file_size < (200000000):
                if file_name.is_file():

                    fileHash = hashlib.md5(open(file_name, 'rb').read()).hexdigest()

                    if fileHash not in unique:
                        unique[fileHash] = file_name

                    else:
                        dcount += 1
                        os.remove(file_name)

                else:
                    print("Operation not Successful")
            else:
                self.large_files.append(file_name)
        file_list = os.listdir(path)

        return count,dcount


