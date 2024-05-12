#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name = "Reginald", job = "Admin"):
        self.name = name
        self.job = job

    def getname(self):
        return self._name

    def setname(self, name):
        if type(name) is str and 1 <= len(name) <= 25:
            self._name = name.title()

        else:
            print("Name must be string between 1 and 25 characters.") 

    name = property(getname, setname)  

    def get_job(self):
        return self._job

    def set_job(self, job):
        if job in APPROVED_JOBS:
            self._job = job

        else:
            print("Job must be in list of approved jobs.")
    
    job = property(get_job, set_job)                                 
    
