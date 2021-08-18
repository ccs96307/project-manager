# coding: utf-8


class Project(object):
    def __init__(self):
        # Project
        self.project_name = ""
        self.project_is_clear = False

        # Tasks
        self.task_id = 0
        self.task = {
            "name": "",
            "weight": 1,
            "comment": "",
            "tags": [],
            "is_clear": False,
        }
        self.tasks = {}

    def add_task(self, name="", weight=1, comment="", is_clear=False):
        # If task field is null
        if name == "":
            name = "temp_{}".format(len(self.tasks))

        # Add
        task = self.task.copy()
        task["name"] = name
        task["weight"] = weight
        task["comment"] = comment
        task["is_clear"] = is_clear
        self.tasks[self.task_id] = task
        self.task_id += 1

    def delete_task(self, task_id: int):
        self.tasks.pop(task_id)

    def update_task(self, task_id, name, weight, comment, is_clear):
        self.tasks[task_id]["name"] = name
        self.tasks[task_id]["weight"] = weight
        self.tasks[task_id]["comment"] = comment
        self.tasks[task_id]["is_clear"] = False










