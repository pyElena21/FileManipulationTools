'''
Created on 14 Dec 2017

@author: Elena Koumpli

See more in https://stackoverflow.com/questions/30887979/i-want-to-create-a-script-for-unzip-tar-gz-file-via-python


'''

import tarfile
import os


def unzip_tarfiles(path_to_tarfiles, unzip_where_folder):

    '''
    Fast unzipper for csv.tar.gz files
    
    '''
    files = [f for f in os.listdir(unzip_tarfiles) if f.endswith('.csv.tar.gz')]
    print(files)
    
    for fname in files:
            
        tar = tarfile.open(path_to_tarfiles+fname, "r:gz")
        tar.extractall(unzip_where_folder)
        tar.close()

        
        