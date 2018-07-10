import subprocess

class CardReader:
    python3_command = '/home/pi/Desktop/Revelations/python2Scanner.py'

    def getClueNum(self):
        process = subprocess.Popen(self.python3_command, stdout=subprocess.PIPE)
        output, error = process.communicate()
        clueNum = str(output).split('\\n')[1]
        return clueNum


#scanner = CardReader()

#print(scanner.getClueNum())
