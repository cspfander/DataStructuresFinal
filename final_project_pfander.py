"""
Program: priority_queue_application_pfander.py
Author: Colten pfander
Date last modified: 05/7/20


The purpose of this program is to create a program that will help doctors and nurses easily store patients' info as well
as place them in a proper queue based on their symptoms.
"""
import tkinter as tk

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
                self.rear = current.previous
                self.size += 1
            # if greater, next = current
            if patient.priority < current.priority:
                current.previous = patient
                self.front = current
                self.rear = current.previous
                self.size += 1
            # if less, previous = current

        if patient.priority > current.priority:
            if current.previous is None:
                current.previous = patient
                self.size += 1
            else:
                self._enqueue(current.left, patient)
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


if __name__ == '__main__':
    """test_tree = Tree()
    test_queue = Queue()
    test_patient_one = Patient("Colten", 24, 1, 9)
    test_patient_two = Patient("Tyler", 99, 2, 4)
    test_patient_three = Patient("Luis", 23, 3, 15)
    Database.insert(test_patient_one)
    Database.insert(test_patient_two)
    Database.insert(test_patient_three)"""
    try:

    except ValueError:
        print("This program has been closed due to a value error!")
