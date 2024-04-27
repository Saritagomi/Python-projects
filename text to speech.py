import win32com.client
speak = win32com.client.Dispatch("SAPI.Spvoice")
print("Hello, SOUVIK PODDAR\nHow are you? \nThis is a type of assistive technology that reads digital text aloud.\nHow can I help you")
speak.Speak("Hello, SOUVIK PODDAR\nHow are you? \nThis is a type of assistive technology that reads digital text aloud.\nHow can I help you")
while True:
    x = input("Type here :")
    if x == "stop":
        speak.Speak("Thanks for visiting")
        break
    speak.Speak(x)
print("thanks for visiting")
print("If you want to continue plz enter 'yes' here")
while True:
    y = input()
    if y == "yes":
        while True:
            x = input("Type here :")
            if x == "finish":
                speak.Speak("Thank YOU Souvik poddar")
                break
            speak.Speak(x)

    else :
        break
# while True:
#     x = input("Type here :")
#     if x == "finish":
#         speak.Speak("Thank YOU Souvik poddar")
#         break
#     speak.Speak(x)









