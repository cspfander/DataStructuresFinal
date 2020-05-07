"""
Program: priority_queue_application_pfander.py
Author: Colten pfander
Date last modified: 05/7/20


The purpose of this program is to create a program that will help doctors and nurses easily store patients' info as well
as place them in a proper queue based on their symptoms.
"""


class Patient:
    def __init__(self, name: str, age: int, patient_id: int, priority: int) -> None:  # add more patient info
        self.left = None
        self.right = None
        self.next = None
        self.previous = None
        self.bills = []
        self.name = name
        self.age = age
        self.patient_id = patient_id
        self.priority = priority

    def __str__(self):
        return f"Patient Info:\nName: {self.name}, Age: {self.age}, ID: {self.patient_id}, Priority: {self.priority}"

    def print_bills(self):  # sorting bills by amount due
        pass


class Bills:
    def __init__(self, amount):
        self.amount = amount
        pass


class Tree:  # look up patient, by patient_id (given at time of visit)
    def __init__(self) -> None:
        self.root = None

    def insert(self, name: str, age: int, patient_id: int, priority: int) -> None:
        if self.root is None:
            self.root = Patient(name, age, patient_id, priority)
        else:
            self._insert(self.root, name, age, patient_id, priority)

    def _insert(self, current: object, name: str, age: int, patient_id: int, priority: int) -> None:
        if patient_id > current.patient_id:
            if current.left is None:
                current.left = Patient(name, age, patient_id, priority)
            else:
                self._insert(current.left, name, age, patient_id, priority)
        elif patient_id < current.patient_id:
            if current.right is None:
                current.right = Patient(name, age, patient_id, priority)
            else:
                self._insert(current.right, name, age, patient_id, priority)
        else:
            print("Error could not compare Node.")

    def find(self, patient_id):
        if self.root is None:
            print("There are no patients yet.")
        else:
            self._find(self.root, patient_id)

    def _find(self, current: object, patient_id):
        if patient_id == current.patient_id:
            print(current)
            return
        elif current.left is None and current.right is None:
            print("No patient with ID: ", patient_id)
            return
        if patient_id > current.patient_id and current.left:
            self._find(current.left, patient_id)
            return
        elif patient_id < current.patient_id and current.right:
            self._find(current.right, patient_id)
            return


class Queue:
    def __init__(self):
        pass

    def insert(self):
        pass
    pass


class Database:
    def __init__(self):
        self.tree = Tree()
        self.queue = Queue()

    def insert(self, patient):
        self.tree.insert(patient.name, patient.age, patient.patient_id, patient.priority)
        self.queue.insert(patient)
        pass
