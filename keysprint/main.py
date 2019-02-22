import tkinter as tk
import tkinter.messagebox as messagebox
import time

### Variables
startTime = None


### Functions
def getTextFor(item):
    with open(item.lower() + ".txt", "r") as file:
        return file.read()
def setText():
    item = choices.get(choices.curselection())
    print(item)
    text.delete("0.0", tk.END)
    text.insert(tk.END, getTextFor(item))
def getWPM(text):
   return len(text.split(" "))
def getMistakes(text, correctText):
    correct = 0
    text = text.split(" ")
    correctText = correctText.split(" ")
    correctText = correctText[:len(text)]
    for word, wordCorrect in zip(text, correctText):
        if word == wordCorrect:
            correct += 1
    return str(int((correct / len(correctText)) * 100)) + "%"
def checkTime():
    global startTime
    if startTime != None:
        if (time.time() - startTime) > 60:
            startTime = None
            
            wpm = getWPM(typingArea.get("1.0",tk.END))
            mistakes = getMistakes(typingArea.get("1.0",tk.END), text.get("1.0",tk.END))
            messagebox.showinfo("Done!", "You typed at %s WPM and at %s correct" % (wpm, mistakes))
    root.after(500, checkTime)
def start():
    global startTime
    startTime = time.time()

### Main
root = tk.Tk()

choices = tk.Listbox()
choices.insert(tk.END, "Things", "Python_Hello_World")
text = tk.Text(root)
typingArea = tk.Text(root)
setTextBtn = tk.Button(root, text="Set Text", command=setText)
startBtn = tk.Button(root, text="Start", command=start)

choices.pack()
setTextBtn.pack()
startBtn.pack()
text.pack()
typingArea.pack()

checkTime()
root.mainloop()