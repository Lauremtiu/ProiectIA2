import tkinter as tk
from tkinter import messagebox

boli_si_simptome = {
    "gripa": ["febra", "tuse", "dureri de cap", "oboseala", "junghi"],
    "raceala": ["tuse", "stranut", "nas infundat", "durere in gat"],
    "migrena": ["dureri de cap", "sensibilitate la lumina", "greata"],
    "alergie": ["stranut", "nas înfundat", "mancarimi", "ochi rosii"],
    "COVID-19": ["febra", "tuse", "pierderea mirosului", "dificultati de respiratie"],
}

def identifica_boala(simptome_introduse):
    rezultate = []
    for boala, simptome in boli_si_simptome.items():
        potriviri = set(simptome_introduse).intersection(simptome)
        if potriviri:
            rezultate.append((boala, len(potriviri)))

    rezultate.sort(key=lambda x: x[1], reverse=True)
    return rezultate


def analiza_simptome():
    input_utilizator = entry_simptome.get()
    if not input_utilizator.strip():
        messagebox.showerror("Eroare", "Te rog sa introduci simptome.")
        return

    simptome_introduse = [s.strip().lower() for s in input_utilizator.split(",")]
    rezultate = identifica_boala(simptome_introduse)

    if rezultate:
        rezultat_text = "Posibile diagnostice:\n"
        for boala, potriviri in rezultate:
            rezultat_text += f"- {boala} (potriviri: {potriviri})\n"
    else:
        rezultat_text = "Nu am gasit o boala care sa corespunda simptomelor introduse."

    messagebox.showinfo("Rezultat", rezultat_text)


root = tk.Tk()
root.title("Analizator de Simptome")

label_titlu = tk.Label(root, text="Analizator de Simptome", font=("Helvetica", 16, "bold"))
label_titlu.pack(pady=10)

label_instr = tk.Label(root, text="Introdu simptomele separate prin virgula:")
label_instr.pack(pady=5)

entry_simptome = tk.Entry(root, width=50)
entry_simptome.pack(pady=5)

button_analyze = tk.Button(root, text="Analizeaza", command=analiza_simptome)
button_analyze.pack(pady=10)

label_nota = tk.Label(root, text="Nota: Consultati un medic pentru un diagnostic corect!", fg="red")
label_nota.pack(pady=10)

root.mainloop()