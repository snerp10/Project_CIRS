from tkinter import *
from tkinter import messagebox, font
from tkinter import ttk
from crime_incident import CrimeIncident, CrimeIncidentManager

class dash:
    def __init__(self):
    # Create the incident manager
        self.manager = CrimeIncidentManager()

    # Main window for the dashboard
        self.dashWindow = Tk()
        self.dashWindow.title("Crime Incident Reporting System")
        self.x = (self.dashWindow.winfo_screenwidth() // 2) - (720 // 2)
        self.y = (self.dashWindow.winfo_screenheight() // 2) - (500 // 2)
        self.dashWindow.geometry('{}x{}+{}+{}'.format(750, 500, self.x, self.y))

    # Title
        self.title = Label(self.dashWindow,
                           text="Crime Incident Reporting System",
                           font=("Comic Sans MS", 18, "bold"),
                           pady=20)
        self.title.pack()

    # Frame for the form and buttons
        self.formFrame = Frame(self.dashWindow)
        self.formFrame.config(border=10, highlightbackground="black", highlightcolor="black", highlightthickness=3)
        self.formFrame.pack()

    # Incident Entry Form

    #incidentLabel

        self.incIdLabel = Label(self.formFrame,
                             text="Incident ID")
        self.incIdLabel.config(font=("Comic Sans MS", 12))
        self.incIdLabel.grid(row=0, column=0, padx=10, pady=5)

    #incidentEntry

        self.incidentID = Entry(self.formFrame)
        self.incidentID.config(font=("Arial", 12),
                               width=30)
        self.incidentID.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

    #descriptionLabel

        self.descLabel = Label(self.formFrame,
                            text="Description")
        self.descLabel.config(font=("Comic Sans MS", 12))
        self.descLabel.grid(row=1, column=0, padx=10, pady=5)

    #descriptionEntry

        self.description = Entry(self.formFrame)
        self.description.config(font=("Arial", 12),
                                width=30)
        self.description.grid(row=1, column=1, columnspan=2, padx=10, pady=5)

    #locationLabel

        self.locLabel = Label(self.formFrame,
                            text="Location")
        self.locLabel.config(font=("Comic Sans MS", 12))
        self.locLabel.grid(row=2, column=0, padx=10, pady=5)

    #locationEntry

        self.location = Entry(self.formFrame)
        self.location.config(font=("Arial", 12),
                             width=30)
        self.location.grid(row=2, column=1, columnspan=2, padx=10, pady=5)

    #dateLabel

        self.dateLabel = Label(self.formFrame,
                             text="Date")
        self.dateLabel.config(font=("Comic Sans MS", 12))
        self.dateLabel.grid(row=3, column=0, padx=10, pady=5)

    #dateEntry

        self.date = Entry(self.formFrame)
        self.date.config(font=("Arial", 12),
                         width=30)
        self.date.grid(row=3, column=1, columnspan=2, padx=10, pady=5)

    # Buttons for CRUD operations

        self.addButton = Button(self.formFrame, text="Add",
                                command=self.create,
                                width=10,
                                background = "#333333",
                                foreground= "#FFFFFF")
        self.addButton.config(border=5, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.addButton.config(font=("Comic Sans MS", 12))
        self.addButton.grid(row=4, column=0, pady=10, padx = 30)

        self.updateButton = Button(self.formFrame, text="Update",
                                   command=self.update,
                                   width=10,
                                   background = "#333333",
                                   foreground= "#FFFFFF")
        self.updateButton.config(border=5, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.updateButton.config(font=("Comic Sans MS", 12))
        self.updateButton.grid(row=4, column=1, pady=10, padx = 30)

        self.deleteButton = Button(self.formFrame, text="Delete",
                                   command=self.delete,
                                   width=10,
                                   background = "#333333",
                                   foreground= "#FFA07A")
        self.deleteButton.config(font=("Comic Sans MS", 12))
        self.deleteButton.config(border=5, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.deleteButton.grid(row=4, column=2, pady=10, padx = 30)

        self.deleteAllButton = Button(self.formFrame, text="Delete All",
                                      command=self.deleteAll,
                                      width=10,
                                      background = "#333333",
                                      foreground = "#FFA07A")
        self.deleteAllButton.config(font=("Comic Sans MS", 12))
        self.deleteAllButton.config(border=5, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.deleteAllButton.grid(row=4, column=3, pady=10, padx = 30)

    # Treeview (table) for displaying the crime incident records
        self.tree = ttk.Treeview(self.dashWindow,
                                 columns=("ID", "Description", "Location", "Date"),
                                 show='headings')
        self.tree.config(height = 50)
        self.tree.column("ID", width = 50, anchor = 'center')
        self.tree.column("Description", width=200, anchor='center')
        self.tree.column("Location", width=200, anchor='center')
        self.tree.column("Date", width=100, anchor='center')

        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Comic Sans MS', 12), foreground='black')
        style.configure("Treeview", font=('Arial', 10))

        style.map("Treeview",
              background=[("selected", "#FFA07A")],  # Orange Red highlight when clicked
              foreground=[("selected", "black")])  # White text when clicked

        self.tree.tag_configure('evenrow', background="lightgreen")
        self.tree.heading("ID", text="Incident ID")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Location", text="Location")
        self.tree.heading("Date", text="Date")
        self.tree.pack(pady = 20, expand = False, fill = 'both')

    #load functions
        self.load_data()
        self.dashWindow.mainloop()

    # Create a new crime report
    # Functions
    def create(self):
        incident_id = self.incidentID.get()
        description = self.description.get()
        location = self.location.get()
        date = self.date.get()

        if incident_id and description and location and date:
            new_incident = CrimeIncident(incident_id, description, location, date)
            self.manager.add_incident(new_incident)
            self.tree.insert('', 'end', values=(incident_id, description, location, date),tags = ('evenrow'))
            self.clear_form()
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields!")

    # Update an existing crime report
    def update(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_id = self.tree.item(selected_item, 'values')[0]
            updated_incident = CrimeIncident(
                self.incidentID.get(),
                self.description.get(),
                self.location.get(),
                self.date.get()
            )
            if self.manager.update_incident(selected_id, updated_incident):
                incident_id = self.incidentID.get()
                description = self.description.get()
                location = self.location.get()
                date = self.date.get()
                if incident_id and description and location and date:
                    self.tree.item(selected_item, values=(
                        self.incidentID.get(),
                        self.description.get(),
                        self.location.get(),
                        self.date.get()
                    ))
                else:messagebox.showwarning("Input Error", "Please fill out all fields!")
                self.clear_form()
            else:
                messagebox.showwarning("Error", "Incident not found!")
        else:
            messagebox.showwarning("Selection Error", "Please select an incident to update!")

    # Delete a crime report
    def delete(self):
        selected_item = self.tree.selection()
        if selected_item:
            selected_id = self.tree.item(selected_item, 'values')[0]
            if self.manager.delete_incident(selected_id):
                    self.tree.delete(selected_item)
                    self.clear_form()
            else:
                messagebox.showwarning("Error", "Incident not found!")
        else:
            messagebox.showwarning("Selection Error", "Please select an incident to delete!")

    def deleteAll(self):
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete all incidents?")
        if confirm:
            self.manager.delete_all_incidents()
            for item in self.tree.get_children():
                self.tree.delete(item)
                self.clear_form()

            messagebox.showinfo("Deleted", "All incidents have been deleted.")
        else:
            messagebox.showinfo("Cancelled", "Deletion cancelled.")


    # Load existing crime data
    def load_data(self):
        incidents = self.manager.get_all_incidents()

        for incident in incidents:
            # Insert each incident into the Treeview
            self.tree.insert('', 'end',
                             values=(incident.incident_id, incident.description, incident.location, incident.date))

    # Clear the form after creating or updating
    def clear_form(self):
        self.incidentID.delete(0, END)
        self.description.delete(0, END)
        self.location.delete(0, END)
        self.date.delete(0, END)


if __name__ == "__main__":
    dash()
