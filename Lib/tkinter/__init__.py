import tkinter as tk

def click(event):
    # Get current and new input
    current = str(entry.get())
    new = str(event.widget["text"])
    if new == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif new == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, new)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 18), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row = 1
col = 0
for button in buttons:
    b = tk.Button(root, text=button, font=('Arial', 18), width=5, height=2)
    b.grid(row=row, column=col)
    b.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
