import os
import shutil
import zipfile

class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = "unzipped-{}".format(zipname[:-4])

    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)

    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.zipname)
        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()

    def zip_files(self):
        file = zipfile.ZipFile(self.zipname, 'w')
        for filename in os.listdir(self.temp_directory):
            file.write(self._full_filename(filename), filename)
        shutil.rmtree(self.temp_directory)
        
    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()
