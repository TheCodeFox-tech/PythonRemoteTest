import subprocess
print("Ok, for now")
print("It seems like it works.")
print("That's good")
TestBat = open(r'Test.bat', '+w')
TestBat.write('powershell wget https://raw.githubusercontent.com/TheCodeFox-tech/PythonRemoteTest/main/Test.json -o Test.json')
TestBat.close()
subprocess.call([r'Test.bat'])
