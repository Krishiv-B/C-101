import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = "LzO8S-zO1JYAAAAAAAAAAQG5ssY9nk7TK03D9elgYNX5-ZA_p8T0VFdMOlf-lCZP"
    transferData = TransferData(access_token)

    file_from = input("Enter the name of the file that you want to store in dropbox: ")
    file_to = input("Enter the full path to which you want to upload the file : ")  
    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()