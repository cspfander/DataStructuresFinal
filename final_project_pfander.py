"""
Program: priority_queue_application_pfander.py
Author: Colten pfander
Date last modified: 05/7/20


The purpose of this program is to create a program that will help doctors and nurses easily store patients' info as well
as place them in a proper queue based on their symptoms.
"""
import tkinter as tk
import tkinter.font as tkFont

patients_visited_today = {}


class Patient:
    """
    This will hold all of the patients information.
    """

    def __init__(self, name: str, age: int, patient_id: int, priority: int) -> None:
        self.left = None
        self.right = None
        self.next = None
        self.previous = None
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.priority = priority

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.patient_id}, Priority: {self.priority}\n"

    def add_patient(self):
        patients_visited_today.update({self.name: self.priority})


class Tree:
    """
    This class will store the patient in a tree to be accessed any any point.
    """

    def __init__(self) -> None:
        self.root = None

    def insert(self, patient) -> None:
        """
        This function won't return anything, but will actually insert the patient into the tree.
        """
        if self.root is None:
            self.root = patient
        else:
            self._insert(self.root, patient)

    def _insert(self, current, patient):
        """
        Helper function for insert
        """
        if patient.patient_id > current.patient_id:
            if current.left is None:
                current.left = patient
            else:
                self._insert(current.left, patient)
        elif patient.patient_id < current.patient_id:
            if current.right is None:
                current.right = patient
            else:
                self._insert(current.right, patient)
        else:
            return "Error could not compare Node."

    def bfs(self):
        queue = [self.root]
        temp_list = []
        while len(queue) > 0:
            temp_list.append(queue[0])
            temp = queue.pop(0)
            if temp.right is not None:
                queue.append(temp.right)

            if temp.left is not None:
                queue.append(temp.left)
        return temp_list


class Queue:
    """
    This class will be responsible for actually creating the "line" or order in which the patients will be seen.
    """

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        """
        This checks to see whether any patients are here to be seen yet or not.
        """
        if self.size == 0:
            return True
        return False

    def enqueue(self, patient):
        """
        Enqueue will actually put the patient into queue into the correct spot.
        """
        if self.rear is None and self.front is None:
            self.front = patient
            self.rear = self.front
            self.size += 1
            return
        else:
            self._enqueue(self.rear, patient)

    def _enqueue(self, current: object, patient):
        """
        Helper function for enqueue.
        """
        if self.size == 1:
            if patient.priority > current.priority:
                current.next = patient
                self.front = current.next
                self.rear = current
                self.size += 1
            if patient.priority < current.priority:
                current.next = self.front
                self.front.previous = current.next
                self.rear = current.previous
                self.size += 1
        elif patient.priority > current.priority:
            if current.previous is None:
                after_current = current.next
                current.next = patient
                patient.next = after_current
                after_current.previous = patient
                patient.previous = current
                self.size += 1
            else:
                self._enqueue(current.next, patient)
        elif patient.priority < current.priority:
            if current.next is None:
                before_current = current.previous
                current.previous = patient
                patient.previous = before_current
                before_current.next = patient
                patient.next = current
                self.size += 1
            else:
                self._enqueue(current.next, patient)
        else:
            return "Error: Patient couldn't be added to queue."

    def de_queue(self):
        """
        De_queue is responsible for removing the front of the queue and keeping track of the front accordingly once a
        patient has been seen.
        """
        if self.is_empty():
            return "There are currently no patients."
        temp = self.front
        if self.size > 1:
            self.front = self.front.next
            self.size -= 1
        else:
            self.front = None
            self.rear = None
            self.size -= 1
        return temp

    def peek(self):
        """
        :return: This will return the next patient to be seen.
        """
        if self.is_empty():
            return "There are currently no patients."
        else:
            return f"{self.front.name}"


class Database:
    """
    This class is responsible for inserting the patient into both the tree and queue.
    """

    def __init__(self):
        self.tree = Tree()
        self.queue = Queue()

    def insert(self, patient):
        """
        Insert will place the patient into the tree and queue.
        """
        self.tree.insert(patient)
        self.queue.enqueue(patient)


def create_patient():
    temp_name = patient_name.get()
    temp_age = patient_age.get()
    temp_priority = int(patient_priority.get())
    if len(patients_visited_today) == 0:
        temp_id = 1
    else:
        temp_id = len(patients_visited_today) + 1
    patient = Patient(temp_name, temp_age, temp_id, int(temp_priority))
    patient.add_patient()
    patients_visited_show.configure(text=patients_visited_today)
    temp_patient = new_database.queue.peek()
    new_database.insert(patient)
    new_temp_patient = new_database.queue.peek()
    if temp_patient != new_temp_patient:
        current_patient_label_show.configure(text=new_database.queue.peek())
    if new_database.queue.size == 1:
        current_patient_label_show.configure(text=new_database.queue.peek())
    patient_name.delete(0, 100)
    patient_age.delete(0, 100)
    patient_priority.delete(0, 100)
    patient_name.focus()


def remove_patient():
    new_database.queue.de_queue()
    current_patient_label_show.configure(text=new_database.queue.peek())


def sort_patients_visited():
    sorted_patients = sorted(patients_visited_today.items(), key=lambda x: x[1], reverse=True)
    patients_visited_show.configure(text=sorted_patients)


def patient_look_up():
    patient_info = new_database.tree.bfs()
    patient_look_up_info.configure(text=patient_info)


if __name__ == '__main__':
    try:
        new_database = Database()
        m = tk.Tk()
        m.geometry("800x300")
        m.title("Patient Queue and Storage for Doctors")
        patient_name = tk.Entry(m)
        patient_name.place(x=350, y=125)
        patient_name.focus()
        patient_name.bind("<Return>", lambda function1: patient_age.focus())
        patient_name_label = tk.Label(m, text="Patients Name:")
        patient_name_label.place(x=250, y=125)
        patient_age = tk.Entry(m)
        patient_age.place(x=350, y=150)
        patient_age.bind("<Return>", lambda function1: patient_priority.focus())
        patient_age_label = tk.Label(m, text="Patients Age:")
        patient_age_label.place(x=250, y=150)
        patient_priority = tk.Entry(m)
        patient_priority.place(x=350, y=175)
        patient_priority.bind("<Return>", lambda function1: create_patient())
        patient_priority_label = tk.Label(m, text="Patients Priority:")
        patient_priority_label.place(x=250, y=175)
        font_style = tkFont.Font(family="TkDefaultFont", size=8)
        patient_priority_legend = tk.Label(m, text="*LEGEND*\nAdd patient symptoms for total priority:\n"
                                                   "Cough = 1\nSneeze = 1\nHeadache = 2 - 4 based on severity\nPain = 2"
                                                   " - 8 depends on severity/location\nRespiratory / Short of breath = "
                                                   "4\nNausea = 4\nDiarrhea = 5\nBroken bones = 5 - 10\nVomitting = 6\n"
                                                   "Fever = 7", font=font_style)
        patient_priority_legend.place(x=15, y=125)
        font_style_two = tkFont.Font(family="TkDefaultFont", size=16)
        current_patient_label = tk.Label(m, text="NEXT PATIENT: ", font=font_style_two)
        current_patient_label.place(x=15, y=10)
        current_patient_label_show = tk.Label(m, text=new_database.queue.peek(), font=font_style_two)
        current_patient_label_show.place(x=175, y=10)
        create_patient_button = tk.Button(m, text="Enter", command=lambda: create_patient(), width=16)
        create_patient_button.place(x=350, y=200)
        next_patient_button = tk.Button(m, text="Deque Patient", command=lambda: remove_patient(), width=16)
        next_patient_button.place(x=350, y=225)
        patients_visited_label = tk.Label(m, text="Patients signed in today:")
        patients_visited_label.place(x=15, y=50)
        patients_visited_show = tk.Label(m, text=patients_visited_today)
        patients_visited_show.place(x=150, y=50)
        sort_patients_button = tk.Button(m, text="Sort by Priority", command=lambda: sort_patients_visited(), width=16)
        sort_patients_button.place(x=350, y=250)
        patient_look_up_button = tk.Button(m, text="Show Patients' Info", command=lambda: patient_look_up(), width=16)
        patient_look_up_button.place(x=15, y=75)
        patient_look_up_info = tk.Label(m, text="")
        patient_look_up_info.place(x=500, y=75)
        exit_button = tk.Button(m, text="Exit", command=m.destroy, width=16)
        exit_button.place(x=200, y=270)
        m.bind('<Escape>', lambda event=None: exit_button.invoke())
        m.mainloop()
    except ValueError:
        print("This program has been closed due to a value error!")
