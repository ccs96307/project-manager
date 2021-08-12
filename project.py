# coding: utf-8


class Project(object):
    def __init__(self):
        # Attributes
        self.project_name = ""
        self.project_is_clear = False
        self.tasks = []
        self.weights = []
        self.comments = []
        self.is_clear = []

    def add_task(self, task: str):
        if task == str:
            self.tasks.append(task)
        else:
            # TODO
            None

    





