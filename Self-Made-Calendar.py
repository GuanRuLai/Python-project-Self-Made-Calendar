import tkinter as tk
from tkinter import messagebox

class CalenderGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Calendar GUI")
        
        # create an empty list to store events
        self.events = []

        # create GUI
        self.create_widgets()

    # method of create_widgets
    def create_widgets(self):
        # create and configure event listbox
        self.event_listbox = tk.Listbox(self.root, selectmode = tk.SINGLE) # single choice
        # place listbox on GUI 
        self.event_listbox.pack(padx = 15, pady = 15)
    
        # create buttons
        self.add_button = tk.Button(self.root, text = "Add Your Event", fg = "black", font = ("helvetica", 10, "bold"), command = self.add_event)
        self.view_button = tk.Button(self.root, text = "View Your Event", fg = "blue", font = ("helvetica", 10, "bold"), command = self.view_event)
        self.delete_button = tk.Button(self.root, text = "Delete Your Event", fg = "red", font = ("helvetica", 10, "bold"), command = self.delete_event)

        # place buttons on GUI
        self.add_button.pack(padx = 10, pady = 5)
        self.view_button.pack(padx = 10, pady = 5)
        self.delete_button.pack(padx = 10, pady = 5)

    # method of add_event
    def add_event(self):
        # Create a new window for adding another event
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Your Event")

        # Create and configure entry fields
        name_label = tk.Label(add_window, text="Event Name:", fg = "black", font = ("helvetica", 10, "bold"))
        date_label = tk.Label(add_window, text="Event Date (YYYY-MM-DD):", fg = "black", font = ("helvetica", 10, "bold"))
        time_label = tk.Label(add_window, text="Event Time:", fg = "black", font = ("helvetica", 10, "bold"))
        location_label = tk.Label(add_window, text="Event Location:", fg = "black", font = ("helvetica", 10, "bold"))
        participants_label = tk.Label(add_window, text="Event Participants (comma-separated):", fg = "black", font = ("helvetica", 10, "bold"))

        name_label.grid(row = 0, column = 0) # left
        date_label.grid(row = 1, column = 0)
        time_label.grid(row = 2, column = 0)
        location_label.grid(row = 3, column = 0)
        participants_label.grid(row = 4, column = 0)

        self.name_entry = tk.Entry(add_window)
        self.date_entry = tk.Entry(add_window)
        self.time_entry = tk.Entry(add_window)
        self.location_entry = tk.Entry(add_window)
        self.participants_entry = tk.Entry(add_window)
        
        self.name_entry.grid(row = 0, column = 1) # right
        self.date_entry.grid(row = 1, column = 1)
        self.time_entry.grid(row = 2, column = 1)
        self.location_entry.grid(row = 3, column = 1)
        self.participants_entry.grid(row = 4, column = 1)

        # Create and configure "Add" button
        add_button = tk.Button(add_window, text = "Add", fg = "black", font = ("helvetica", 10, "bold"), command = self.save_event)
        add_button.grid(row = 5, column = 0, columnspan = 2, pady = 10) # button step over 2 columns

    # method of save_event 
    def save_event(self):
        # Get data from entry fields
        name = self.name_entry.get()
        date = self.date_entry.get()
        time = self.time_entry.get()
        location = self.location_entry.get()
        participants = self.participants_entry.get().split(",")

        # create an event and add it to the listbox
        event = Event(name, date, time, location, participants)
        self.events.append(event)
        # update event_listbox
        self.update_event_listbox()

        # close the "Add Your Event" window
        self.root.focus_set() # Focus on self.root after adding events
        self.name_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.location_entry.delete(0, tk.END)
        self.participants_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Your event has been added successfully!")
    
    # method of view_event
    def view_event(self):
        # Get the selected event from the listbox
        # return index of selected event
        selected_event_index = self.event_listbox.curselection()

        if selected_event_index:
            selected_event = self.events[selected_event_index[0]]
            event_details = (
                f"Event Name: {selected_event.name}\n"
                f"Event Date: {selected_event.date}\n"
                f"Event Time: {selected_event.time}\n"
                f"Event Location: {selected_event.location}\n"
                f"Event Participants: {', '.join(selected_event.participants)}"
            )
            messagebox.showinfo("Event details", event_details)

        else:
            messagebox.showinfo("Error", "No event has been selected.")
    
    # method of delete_event
    def delete_event(self):
        # Get the selected event from the listbox
        # return index of selected event
        selected_event_index = self.event_listbox.curselection()

        if selected_event_index:
            selected_event = self.events[selected_event_index[0]]
            confirmation = messagebox.askyesno("Confirm Deletion", f"Are you sure to delete the event: {selected_event.name}?")  

            if confirmation:
                self.events.remove(selected_event)
                # update event_listbox
                self.update_event_listbox()

        else:
            messagebox.showinfo("Error", "No event has been selected.")

    # method of update_event_listbox
    # close the window
    def update_event_listbox(self):
        self.event_listbox.delete(0, tk.END)
        # insert events into listbox
        for event in self.events:
            self.event_listbox.insert(tk.END, event.name)

class Event:
    def __init__(self, name, date, time, location, participants):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.participants = participants

if __name__ == "__main__":
    root = tk.Tk()
    app = CalenderGUI(root)
    root.mainloop()



         

