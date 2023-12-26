import tkinter , pyfiglet
import subprocess


#fonction pour excecuter le script virus
def execut_virus():
    print(pyfiglet.figlet_format("Virus is infected you "))
    subprocess.call("python virus.py", shell=True)
#fonction pour excecuter le script vers
def execut_vers():
    print(pyfiglet.figlet_format("Ver is infected you "))
    subprocess.call("python vers.py", shell=True)

#creation de la fenetre + parametrage

app = tkinter.Tk()
#app.geometry("620x240")
app.title("Creation")

#Widgets
mainframe = tkinter.Label(app,text="Bienvenue dans mon programme!!!",font="Algerian",foreground="white",background="blue",borderwidth=0)
mainframe.grid(row=0, column=0,columnspan=2)

label = tkinter.Label(app, text="Hello! À votre choix lancer un lancer un malware en cliquant sur votre choix :",foreground="white",background="brown",font="STHupo 15 underline",borderwidth=0)
label.grid(row=1,column=0,pady=50)

btn1 = tkinter.Button(app,text="virus",font=("Berlin Sans FB",15),background="orange",command=execut_virus)
btn1.grid()

btn2 = tkinter.Button(app,text="ver",font=("Berlin Sans FB",15),background="red",command=execut_vers)
btn2.grid(pady=10)


#boucle principale 

app.mainloop()


