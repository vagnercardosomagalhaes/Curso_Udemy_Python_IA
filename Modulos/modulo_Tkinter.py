import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog  
from tkinter import ttk
from tkinter import font
from tkinter import scrolledtext
from tkinter import PhotoImage
from tkinter import StringVar

window = tk.Tk()
window.title("Modulo Tkinter")
window.geometry("800x600")
window.resizable(False, False)
window.configure(bg="lightblue")

window.attributes("-alpha", 0.9)  # Set transparency level (0.0 to 1.0)
window.attributes("-topmost", True)  # Keep the window on top of other windows

#criando um frame
frame = tk.Frame(window, bg="lightblue")
frame.pack(pady=20)
frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame.config(width=400, height=300)
frame.pack_propagate(False)  # Prevent the frame from resizing to fit its contents
frame.pack(side=tk.TOP, padx=10, pady=10)
frame.config(relief=tk.RAISED, bd=2)

# Criando um botão
def on_button_click():
    messagebox.showinfo("Informação", "Você clicou no botão!")
button = tk.Button(frame, text="Clique aqui", command=on_button_click)
button.pack(pady=10)
button.config(bg="lightgreen", fg="black", font=("Arial", 12, "bold"))
button.bind("<Enter>", lambda e: button.config(bg="green"))
button.bind("<Leave>", lambda e: button.config(bg="lightgreen"))
button.bind("<Button-1>", lambda e: button.config(bg="darkgreen"))
button.bind("<ButtonRelease-1>", lambda e: button.config(bg="lightgreen"))
button.bind("<Button-3>", lambda e: button.config(bg="red"))

#adicionando label
label = tk.Label(frame, text="Este é um exemplo de label", bg="lightblue", font=("Arial", 12))
label.pack(pady=10)

#adicionando input text
entry = tk.Entry(frame, width=30)
entry.pack(pady=10)
entry.config(bg="white", fg="black", font=("Arial", 12))
entry.bind("<FocusIn>", lambda e: entry.config(bg="lightyellow"))
entry.bind("<FocusOut>", lambda e: entry.config(bg="white"))
entry.bind("<Return>", lambda e: messagebox.showinfo("Informação", f"Você digitou: {entry.get()}"))
entry.bind("<Button-1>", lambda e: entry.config(bg="lightblue"))
entry.bind("<ButtonRelease-1>", lambda e: entry.config(bg="white"))
entry.bind("<Button-3>", lambda e: entry.config(bg="red"))
entry.bind("<Double-Button-1>", lambda e: entry.config(bg="blue"))

#adicionando um botão de sair
def on_exit():
    if messagebox.askokcancel("Sair", "Você realmente deseja sair?"):
        window.quit()
exit_button = tk.Button(frame, text="Sair", command=on_exit)
exit_button.pack(pady=10)
exit_button.config(bg="red", fg="white", font=("Arial", 12, "bold"))
exit_button.bind("<Enter>", lambda e: exit_button.config(bg="darkred"))


window.mainloop()