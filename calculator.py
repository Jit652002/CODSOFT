
#make a simple calculator:
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()
        
        # Entry widget to display the result
        result_entry = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        result_entry.grid(row=0, column=0, columnspan=4)

        # Button texts
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        
        # Creating buttons and placing them in grid
        row_val = 1
        col_val = 0
        for text in button_texts:
            button = tk.Button(self, text=text, padx=20, pady=20, font=('Arial', 18), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Making grid cells expand equally
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.result_var.set('')
        elif char == '=':
            try:
                expression = self.result_var.get()
                result = eval(expression)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set('Error')
        else:
            current_text = self.result_var.get()
            new_text = current_text + char
            self.result_var.set(new_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
