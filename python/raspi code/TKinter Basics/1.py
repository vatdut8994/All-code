from tkinter import *
import Crystal

root = Tk()
root.geometry("{0}x{1}+1+1".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.minsize("200", "200")
root.configure(bg="#1e243d")
root.title("Crystal AI")


def back_func():
    global set_set_set
    language.pack_forget()
    gender.pack_forget()
    color.pack_forget()
    assis_name.pack_forget()
    appearance.pack_forget()
    people.pack_forget()
    phrase.pack_forget()
    back.pack_forget()
    label_2.pack(fill=X, pady=10, side=BOTTOM)
    crystal_speech.pack(pady=15, side=BOTTOM)
    time_l.pack(anchor="w", side=TOP)
    settings.pack(anchor="se", pady=1, padx=1)
    set_set_set = False


def set_func():
    global language
    global gender
    global color
    global assis_name
    global appearance
    global people
    global phrase
    global back
    label_2.pack_forget()
    crystal_speech.pack_forget()
    time_l.pack_forget()
    settings.pack_forget()
    language = Button(text="LANGUAGE", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=20, padx=500)
    language.pack(pady=15, side=BOTTOM)
    gender = Button(text="GENDER", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=20, padx=515)
    gender.pack(pady=15, side=BOTTOM)
    color = Button(text="COLOR", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=20, padx=520)
    color.pack(pady=15, side=BOTTOM)
    assis_name = Button(text="NAME", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=20, padx=525)
    assis_name.pack(pady=15, side=BOTTOM)
    appearance = Button(text="APPEARANCE", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=20, padx=480)
    appearance.pack(pady=15, side=BOTTOM)
    people = Button(text="PEOPLE", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=20, padx=515)
    people.pack(pady=15, side=BOTTOM)
    phrase = Button(text="WISH PHRASE", bg='#1e243d', fg="black", font="comicsansms 25 bold", pady=20, padx=477)
    phrase.pack(pady=15, side=BOTTOM)
    back = Button(text="BACK", bg='red', fg="black", font="comicsansms 15 bold", pady=20, command=back_func)
    back.pack(pady=20, side=BOTTOM)
    set_set_set = True


label_2 = Label(text="You said:", bg='#1e243d', fg="green", font="comicsansms 20 bold")
label_2.pack(fill=X, pady=10, side=BOTTOM)
crystal_speech = Label(text="Hello!", bg='#1e243d', fg="white", font="comicsansms 25 bold")
crystal_speech.pack(pady=15, side=BOTTOM)
time_l = Label(text="", bg='#1e243d', fg="yellow", font="comicsansms 25 bold")
time_l.pack(anchor="w", side=TOP)
settings_image = PhotoImage(file="New settings.png")
settings = Button(image=settings_image, anchor="se", command=set_func)
settings.pack(anchor="se", pady=1, padx=1)

print(len(crystal_speech['text']))

crystal_speech['text'] = crystal_speech['text'][0:100] + '-\n' + crystal_speech['text'][100:200]\
    + '-\n' + crystal_speech['text'][200:300]+'-\n' + crystal_speech['text'][300:400]\
    + '-\n' + crystal_speech['text'][400:500]+'-\n' + crystal_speech['text'][500:600]

root.mainloop()
