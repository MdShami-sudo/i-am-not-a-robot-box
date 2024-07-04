import tkinter as tk
from tkinter import messagebox

class NotARobotVerifier:
    def __init__(self, root):
        self.root = root
        self.root.title("I am not a Robot")
        self.root.geometry("300x150")
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="Please check the box to confirm you are not a robot.", font=("Arial", 12), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.check_var = tk.IntVar()
        self.check_button = tk.Checkbutton(root, text="I am not a Robot", font=("Arial", 12), variable=self.check_var, bg="#f0f0f0", command=self.verify)
        self.check_button.pack(pady=10)

    def verify(self):
        if self.check_var.get() == 1:
            messagebox.showinfo("Verification", "You are verified as not a robot.")
        else:
            messagebox.showwarning("Verification", "Please check the box to confirm you are not a robot.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotARobotVerifier(root)
    root.mainloop()
