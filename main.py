import tkinter as tk

kids_detention_list=[]

def detention_list():
    detention = detention_entry.get()
    if detention:
        detention_listbox.insert(tk.END, detention)
        detention_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Detention list")
root.geometry("400x400")

label_prompt = tk.Label(root, text = "Enter the child:")
label_prompt.pack()

detention_entry = tk.Entry(root, width=40)
detention_entry.pack()

add_button = tk.Button(root, text="Add child", command= detention_list)
add_button.pack()

detention_listbox = tk.Listbox(root, width=50, height=10)
detention_listbox.pack()


root.mainloop()

