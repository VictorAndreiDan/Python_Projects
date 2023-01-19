import os
import hashlib
import shutil
import time
from createHash import sha1

# get data from user
syncInterval    = input("What is the synchronization interval in seconds? ")
logPath         = input("What is the log file path? ")
originalPath    = input("What is the folder path? ")
replicaPath     = input("What is the replica path? ")

# add proper ending to file paths
originalPath += '/'
replicaPath += '/'
logFile = open(logPath, 'a')

# get a list of files in the original folder
os.chdir(originalPath)
original = os.listdir()

# get a list of files in the replica folder
os.chdir(replicaPath)
clone = os.listdir()

while True:
    try:
        print("Script will run every ", syncInterval, 'seconds. (press CTRL+C to close it)')
        print("Script will run every ", syncInterval, 'seconds. (press CTRL+C to close it)', file = logFile)
        time.sleep(syncInterval)
        # actualize the folder structure for original and replica
        os.chdir(originalPath)
        original = os.listdir()
        os.chdir(replicaPath)
        clone = os.listdir()
        # print differences
        print('Checking for updates...')
        print('Checking for updates...', file = logFile)
        print('files in origin: ', original,'files in clone: ', clone)
        print('files in origin: ', original,'files in clone: ', clone, file = logFile)

        # files added to source
        filesAdded = list(set(original) - set(clone))
        print('files added to origin: ', filesAdded)
        print('files added to origin: ', filesAdded, file  = logFile)
        # add the specified files into replica folder
        for file in filesAdded:
            shutil.copy(originalPath+file, replicaPath)

        # files deleted from source
        filesDeleted = list(set(clone) - set(original))
        print('files deleted from origin: ', filesDeleted)
        print('files deleted from origin: ', filesDeleted, file = logFile)
        #delete the files from the replica folder
        for file in filesDeleted:
            os.remove(replicaPath+file)

        # monitor for any files that were changed but the names are the same

        originalHash = []
        replicaHash = []

        # print('files in original: ', original)
        # print('files in original: ', original, file = logFile)
        for file in original:
            originalHash.append(sha1(originalPath+file))
            # print(originalPath+file)
            # print(originalPath+file, file = logFile)

        for file in original:
            replicaHash.append(sha1(replicaPath+file))
            # print(replicaPath+file)
            # print(replicaPath+file, file = logFile)


        print('hash origin: ', originalHash)
        print('hash origin: ', originalHash, file = logFile)
        print('hash replica: ', replicaHash)
        print('hash replica: ', replicaHash, file = logFile)
        stillSame = True

        for file in original:
            if(originalHash[original.index(file)] != replicaHash[original.index(file)]):
                print('Detected changes to file: ')
                print('Detected changes to file: ', file = logFile)
                print('hash of', file, 'is different')
                print('hash of', file, 'is different', file = logFile)
                os.remove(replicaPath+file)
                print('updated file', file)
                print('updated file', file, file = logFile)
                shutil.copy(originalPath+file, replicaPath)
                stillSame = False

        if(stillSame):
            print('No changes detected!')
            print('No changes detected!', file = logFile)
        print('')
        print('', file=logFile)
    except KeyboardInterrupt:
        print('Script interrupted by user.')
        print('Script interrupted by user.', file = logFile)
        logFile.close()
        break