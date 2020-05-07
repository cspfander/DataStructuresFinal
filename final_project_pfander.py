"""
Program: priority_queue_application_pfander.py
Author: Colten pfander
Date last modified: 05/7/20


The purpose of this program is to create a program that will help doctors and nurses easily store patients' info as well
as place them in a proper queue based on their symptoms.
"""


class Patient:
    def __init__(self, name, age):  # add more patient info
        self.left = None
        self.right = None
        self.next = None
        self.previous = None
        self.bills = []

    def print_bills(self):  # sorting bills by amount due
        pass


class Bills:
    def __init__(self, amount):
        self.amount = amount
        pass


class Tree:  # look up patient, by name
    def __init__(self):
        pass

    def insert(self):
        pass
    pass


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
        self.tree.insert(patient)
        self.queue.insert(patient)
        pass
