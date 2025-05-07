import tkinter as tk
from tkinter import simpledialog
from datetime import datetime

class TagebuchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tagebuch")
        
        # Textfeld für die Anzeige der Einträge
        self.text_area = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, width=50, height=20)
        self.text_area.pack(pady=10)
        
        # Button für neuen Eintrag
        self.new_entry_button = tk.Button(root, text="+ Neuer Eintrag", command=self.neuer_eintrag)
        self.new_entry_button.pack(pady=5)
        
        # Lade bestehende Einträge
        self.load_entries()

    def neuer_eintrag(self):
        # Dialog für neuen Eintrag
        neuer_text = simpledialog.askstring("Neuer Eintrag", "Schreibe deinen Eintrag:")
        if neuer_text:
            # Zeitstempel hinzufügen
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            eintrag = f"{timestamp}\n{neuer_text}\n\n"
            
            # Speichere den Eintrag in der Datei
            with open("tagebuch.txt", "a", encoding="utf-8") as file:
                file.write(eintrag)
            
            # Zeige den Eintrag in der Textbox
            self.text_area.config(state=tk.NORMAL)
            self.text_area.insert(tk.END, eintrag)
            self.text_area.config(state=tk.DISABLED)

    def load_entries(self):
        try:
            # Lade bestehende Einträge aus der Datei
            with open("tagebuch.txt", "r", encoding="utf-8") as file:
                eintraege = file.read()
                self.text_area.config(state=tk.NORMAL)
                self.text_area.insert(tk.END, eintraege)
                self.text_area.config(state=tk.DISABLED)
        except FileNotFoundError:
            # Falls die Datei nicht existiert, nichts tun
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TagebuchApp(root)
    root.mainloop()