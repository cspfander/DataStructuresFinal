"""
Program: priority_queue_application_pfander.py
Author: Colten pfander
Date last modified: 05/7/20


The purpose of this program is to create a program that will help doctors and nurses easily store patients' info as well
as place them in a proper queue based on their symptoms.
"""
import tkinter as tk
import tkinter.font as tkFont

patients_seen_today = []


class Patient:
    """
    This will hold all of the patients information.
    """

    def __init__(self, name: str, age: int, patient_id: int, priority: int) -> None:  # add more patient info
        self.left = None
        self.right = None
        self.next = None
        self.previous = None
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.priority = priority

    def __str__(self):
        return f"Patient Info:\nName: {self.name}, Age: {self.age}, ID: {self.patient_id}, Priority: {self.priority}"

    def add_patient(self):
        patients_seen_today.append(self.name + ", " + str(self.patient_id))


class Tree:  # look up patient, by patient_id (given at time of visit)
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

    def find(self, patient):
        """
        patient_id: Using the patient's ID we can find their information
        """
        if self.root is None:
            return "There are no patients yet."
        else:
            self._find(self.root, patient.patient_id)

    def _find(self, current: object, patient):
        """
        Helper function for find
        """
        if patient.patient_id == current.patient_id:
            return current
        elif current.left is None and current.right is None:
            return f"No patient with ID: {patient.patient_id}"
        if patient.patient_id > current.patient_id and current.left:
            self._find(current.left, patient.patient_id)
            return
        elif patient.patient_id < current.patient_id and current.right:
            self._find(current.right, patient.patient_id)
            return


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
        if patient.priority > current.priority:
            if current.previous is None:
                current.previous = current
                current
                self.size += 1
            else:
                self._enqueue(current.next, patient)
        elif patient.priority < current.priority:
            if current.next is None:
                current.next = patient
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

    def print_queue(self):
        """
        This function will show all of the current patients in line.
        """
        if self.is_empty():
            return "There are currently no patients." and False
        self._print_queue(self.front)
        return

    def _print_queue(self, node):
        """
        Helper function for print_queue
        """
        print(node)
        if node.next is not None:
            self._print_queue(node.next)
        return

    def peek(self):
        """
        :return: This will return the next patient to be seen.
        """
        if self.is_empty():
            return "There are currently no patients."
        else:
            return f"The next patient to be seen is {self.front.name}"


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


def sort_patients_seen_today(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(arr)


def create_patient():
    temp_name = patient_name.get()
    temp_age = patient_age.get()
    temp_priority = patient_priority.get()
    if len(patients_seen_today) == 0:
        temp_id = 1
    else:
        temp_id = len(patients_seen_today) + 1
    patient = Patient(temp_name, temp_age, temp_priority, temp_id)
    patient.add_patient()
    Database.insert(new_database, patient)
    new_database_queue.peek()
    patient_name.delete(0)
    patient_age.delete(0)
    patient_priority.delete(0)
    patient_name.focus()
    print(patient)


if __name__ == '__main__':
    try:
        new_database = Database()
        new_database_tree = Tree()
        new_database_queue = Queue()
        m = tk.Tk()
        m.geometry("500x300")
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
        patient_priority_legend = tk.Label(m, text="Add patient symptoms for total priority:\n"
                                                   "Cough = 1\nSneeze = 1\nHeadache = 2 - 4 based on severity\nPain = 2"
                                                   " - 8 depends on severity/location\nRespiratory / Short of breath = "
                                                   "4\nDiarrhea = 5\nBroken bones = 5 - 10\nFever = 7", font=font_style)
        patient_priority_legend.place(x=15, y=125)
        font_style_two = tkFont.Font(family="TkDefaultFont", size=16)
        current_patient_label = tk.Label(m, text="NEXT PATIENT: ", font=font_style_two)
        current_patient_label.place(x=15, y=10)
        current_patient_label_show = tk.Label(m, text=new_database_queue.peek(), font=font_style_two)
        current_patient_label_show.place(x=175, y=10)
        create_patient_button = tk.Button(m, text="Enter", command=lambda: create_patient(), width=14)
        create_patient_button.place(x=350, y=200)
        exit_button = tk.Button(m, text="Exit", command=m.destroy, width=16)
        exit_button.place(x=200, y=270)
        m.bind('<Escape>', lambda event=None: exit_button.invoke())
        m.mainloop()
    except ValueError:
        print("This program has been closed due to a value error!")
