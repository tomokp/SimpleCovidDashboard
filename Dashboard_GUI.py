import tkinter as tk
import requests
from bs4 import BeautifulSoup
def scrapeCases(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(class_="sc-xjjbbg-1 iXCPOW")
    cases = results.string
    txtfld.configure(state='normal')
    txtfld.delete(0,tk.END)
    txtfld.insert(tk.END, cases)
    txtfld.configure(state='disabled')
    return

def veere():
    btnGet.configure(text = "Coronabesmettingen ophalen van de gemeente Veere", fg='blue', command =lambda: scrapeCases("https://coronadashboard.rijksoverheid.nl/gemeente/GM0717/positief-geteste-mensen"))
    lbl.configure(text="Coronabesmettingen vandaag in de gemeente Veere:")
    btnNederland.configure(state='normal', bg='#ffffff')
    btnZeeland.configure(state='normal', bg='#ffffff')
    btnVeere.configure(state='disabled', bg='#8cff7d', disabledforeground="black")
    return

def zeeland():
    btnGet.configure(text = "Coronabesmettingen ophalen van de provincie Zeeland", fg='blue', command =lambda: scrapeCases("https://coronadashboard.rijksoverheid.nl/veiligheidsregio/VR19/positief-geteste-mensen"))
    lbl.configure(text="Coronabesmettingen vandaag in de provincie Zeeland:")
    btnNederland.configure(state='normal', bg='#ffffff')
    btnVeere.configure(state='normal', bg='#ffffff')
    btnZeeland.configure(state='disabled', bg='#8cff7d', fg='black', disabledforeground="black")
    return

def nederland():
    btnGet.configure(text = "Coronabesmettingen ophalen van Nederland", fg='blue', command =lambda: scrapeCases("https://coronadashboard.rijksoverheid.nl/landelijk/positief-geteste-mensen"))
    lbl.configure(text="Coronabesmettingen vandaag in Nederland:")
    btnVeere.configure(state='normal', bg='#ffffff')
    btnZeeland.configure(state='normal', bg='#ffffff')
    btnNederland.configure(state='disabled', bg='#8cff7d', fg='black', disabledforeground="black")
    return

window=tk.Tk()
lbl=tk.Label(window, text="Coronabesmettingen vandaag in Nederland:", fg='red', font=("Helvetica", 16))
lbl.place(x=120, y=50)
lblTom=tk.Label(window, text="Tom de Bruijn", fg='black', font=("Helvetica", 8), bg='grey')
lblTom.place(x=0, y=330)
txtfld=tk.Entry(window, state='disabled',disabledforeground="black", text="error", bd=5, font=("Helvetica", 24))
txtfld.place(x=150, y=100)
btnGet=tk.Button(window, text="Coronabesmettingen ophalen van Nederland", fg='blue', font=("Helvetica", 10), command =lambda: scrapeCases("https://coronadashboard.rijksoverheid.nl/landelijk/positief-geteste-mensen"))
btnGet.place(x=175, y=150)
btnNederland=tk.Button(window, state='disabled', bg='#8cff7d', fg='black', disabledforeground="black", text="Nederland", command =lambda: nederland())
btnNederland.place(x=0, y=120)
btnZeeland=tk.Button(window, text="Zeeland", fg='black', command =lambda: zeeland())
btnZeeland.place(x=0, y=160)
btnVeere=tk.Button(window, text="Veere", fg='black', command =lambda: veere())
btnVeere.place(x=0, y=200)
window.title('Coronabesmettingen')
window.geometry("650x350+10+10")
window.mainloop()