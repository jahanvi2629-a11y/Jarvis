import subprocess

command = input("You: ")

if command == "open chrome":
    print("Opening Chrome...")
    subprocess.Popen(["cmd", "/c", "start", "chrome", "--profile-directory=Default"])

elif command == "open calculator":
    print("Opening Calculator...")
    subprocess.Popen(["cmd", "/c", "start", "calc"])

elif command == "open brave":
    print("Opening Brave...")
    subprocess.Popen([
        r"C:\Users\jahan\AppData\Local\BraveSoftware\Brave-Browser\Application\brave.exe"
    ])

elif command == "open spotify":
    print("Opening Spotify...")
    subprocess.Popen(["cmd", "/c", "start", "spotify:"])

elif command == "open vscode":
    print("Opening VS Code...")
    subprocess.Popen(["cmd", "/c", "start", "code"])    

elif command == "open whatsapp":
    print("Opening WhatsApp...")
    subprocess.Popen([
        "explorer.exe",
        r"shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"
    ])

elif command == "open clock":
    print("Opening Clock...")
    subprocess.Popen(["cmd", "/c", "start", "ms-clock:"])

else:
    print("I don't understand that command.")