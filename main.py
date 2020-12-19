from datetime import timedelta


class Task:
    def __init__(self, name, hours, end_time):
        self.name = name
        self.hours = hours
        self.end_time = end_time


new_tasks_file = open(file='new_tasks.txt', mode='r', encoding='utf-8')
tasks_file = open(file='tasks.txt', mode='w', encoding='utf-8')

