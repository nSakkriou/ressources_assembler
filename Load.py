import dropbox
import os, glob

class Dropbox:

    ACCESS_TOKEN = "ACCESS_TOKEN"
    TARGET_PATH = "/_RESSOURCES_/_PRISE_DE_NOTE_/01_INBOX/"

    def __init__(self) -> None:
        try:
            self.dbx = dropbox.Dropbox(Dropbox.ACCESS_TOKEN)
        except:
            print('Error connecting to Dropbox with access token')

    def addFile(self, file_path):
        with open(file_path, "rb") as f:
            self.dbx.files_upload(f.read(), Dropbox.TARGET_PATH + file_path, mute=True)

class Load:

    def __init__(self) -> None:
        self.dropbox = Dropbox()
        self.files = None

    def list_dir(self, path="./files"):
        self.files = glob.glob(path + "/*")
        
    def send_file_to_dropbox(self, path_file):
        self.dropbox.addFile(path_file)

    def send_all_files(self):
        if self.files == None:
            return False

        [self.send_file_to_dropbox(path) for path in self.files]

        return True           


if __name__ == "__main__":
    d = Dropbox()

    d.addFile("init.sql")

