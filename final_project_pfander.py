"""
Program: priority_queue_application_pfander.py
Author: Colten pfander
Date last modified: 05/7/20


The purpose of this program is to create a program that will help doctors and nurses easily store patients' info as well
as place them in a proper queue based on their symptoms.
"""


class Patient:
    """
    This will hold all of the patients information.
    """
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
    """
    This class will store the patient in a tree to be accessed any any point.
    """
    def __init__(self) -> None:
        self.root = None

    def insert(self, name: str, age: int, patient_id: int, priority: int) -> None:
        """
        :param name: Patient's name
        :param age: Patient's age
        :param patient_id: Patient's ID
        :param priority: Priority in which the patient is to be seen.
        :return: This function won't return anything, but will actually insert the patient into the tree.
        """
        if self.root is None:
            self.root = Patient(name, age, patient_id, priority)
        else:
            self._insert(self.root, name, age, patient_id, priority)

    def _insert(self, current: object, name: str, age: int, patient_id: int, priority: int) -> None:
        """
        Helper function for insert
        """
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
        """
        :param patient_id: Using the patient's ID we can find their information
        :return:
        """
        if self.root is None:
            print("There are no patients yet.")
        else:
            self._find(self.root, patient_id)

    def _find(self, current: object, patient_id):
        """
        Helper function for find
        """
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

    def enqueue(self, name: str, age: int, patient_id: int, priority: int):
        """
        Enqueue will actually put the patient into queue into the correct spot.
        """
        if self.rear is None and self.front is None:
            self.front = Patient(name, age, patient_id, priority)
            self.rear = self.front
            self.size += 1
            return
        else:
            self._enqueue(self.rear, name, age, patient_id, priority)

    def _enqueue(self, current: object, name: str, age: int, patient_id: int, priority: int):
        """
        Helper function for enqueue.
        """
        if priority > current.priority:
            if current.previous is None:
                current.previous = Patient(name, age, patient_id, priority)
                self.size += 1
            else:
                self._enqueue(current.left, name, age, patient_id, priority)
        elif priority < current.priority:
            if current.next is None:
                current.next = Patient(name, age, patient_id, priority)
                self.size += 1
            else:
                self._enqueue(current.next, name, age, patient_id, priority)
        else:
            print("Error: Patient couldn't be added to queue.")

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
            print("There are currently no patients.")
            return False
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
        self.tree.insert(patient.name, patient.age, patient.patient_id, patient.priority)
        self.queue.enqueue(patient.name, patient.age, patient.patient_id, patient.priority)
        pass
