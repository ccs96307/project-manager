# coding: utf-8


class Project(object):
    def __init__(self):
        # Project
        self.project_name = ""
        self.project_is_clear = False

        # Tasks
        self.tasks = []
        self.weights = []
        self.comments = []
        self.is_clear_list = []

    def add_task(self, task="", weight=1, comment="", clear=False):
        # If task field is null
        if task == "":
            task = "temp_{}".format(len(self.tasks))

        # Add
        self.tasks.append(task)
        self.weights.append(weight)
        self.comments.append(comment)
        self.is_clear_list.append(clear)

    def delete_task(self, index: int):
        self.tasks.pop(index)
        self.weights.pop(index)
        self.comments.pop(index)
        self.is_clear_list.pop(index)

    def update_task(self, index, task, weight, comment, clear):
        self.tasks[index] = task
        self.weights[index] = weight
        self.comments[index] = comment
        self.is_clear_list[index] = clear










