import dropbox

class Dropbox:

    ACCESS_TOKEN = "sl.BWZV3kO7lQT9Ntsg2rgfUARBnYG971oGMpIZkHgwiffuugy2SjWT7MhpesBl278CcgAkLkyvgh8K7zUrjx_oc_69ED5l8TjX9x3bQh5yIpBAO_x486NMWANIbWNgHCj1PX5ohv8"
    TARGET_PATH = "/_RESSOURCES_/_PRISE_DE_NOTE_/01_INBOX/"

    def __init__(self) -> None:
        try:
            self.dbx = dropbox.Dropbox(Dropbox.ACCESS_TOKEN)
        except:
            print('Error connecting to Dropbox with access token')

    def addFile(self, file_path):
        with open(file_path, "rb") as f:
            self.dbx.files_upload(f.read(), Dropbox.TARGET_PATH + file_path, mute=True)

if __name__ == "__main__":
    d = Dropbox()

    d.addFile("init.sql")