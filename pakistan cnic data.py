      
import tkinter as tk
from tkinter import messagebox

class CNICRecord:
    def __init__(self, cnic_number, name, father_name, address):
        self.cnic_number = cnic_number
        self.name = name
        self.father_name = father_name
        self.address = address

    def __str__(self):
        return f"CNIC Number: {self.cnic_number}\nName: {self.name}\nFather's Name: {self.father_name}\nAddress: {self.address}"

class CNICValidator:
    def __init__(self):
        self.records = {}

    def add_record(self, cnic_number, name, father_name, address):
        self.records[cnic_number] = CNICRecord(cnic_number, name, father_name, address)

    def validate_cnic(self, cnic_number):
        if cnic_number in self.records:
            return self.records[cnic_number]
        else:
            return None

def main():
    validator = CNICValidator()
    validator.add_record("42101-1234567-8", "John Doe", "Jane Doe", "Lahore, Pakistan")

    def search_cnic():
        cnic_number = entry.get()
        record = validator.validate_cnic(cnic_number)
        if record:
            result_text.delete('1.0', tk.END)
            result_text.insert(tk.END, str(record))
        else:
            messagebox.showerror("Invalid CNIC", "No record found for the given CNIC number.")

    root = tk.Tk()
    root.title("Pakistan CNIC Record")

    label = tk.Label(root, text="Enter CNIC Number:")
    label.pack()

    entry = tk.Entry(root, width=50)
    entry.pack()

    button = tk.Button(root, text="Search", command=search_cnic)
    button.pack()

    result_text = tk.Text(root, height=10, width=50)
    result_text.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
      
    