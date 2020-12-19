from datetime import timedelta, date, datetime


class Task:
    def __init__(self, name, deadline: date, hours: int):
        self.name = name
        self.deadline = deadline
        self.hours = hours
        self.score = hours / ((deadline - datetime.now().date()).days + 0.5) ** 2


tasks = []

tasks_file = open(file='tasks.txt', mode='r', encoding='utf-8')
lines = tasks_file.readlines()
for line in lines:
    task_name, end_line, do_time = map(str.strip, line.split(','))
    end_line = datetime.strptime(end_line, '%Y-%m-%d').date()
    tasks.append(Task(task_name, end_line, int(do_time)))

tasks_file.close()

new_tasks_file = open(file='new_tasks.txt', mode='r', encoding='utf-8')
tasks_file = open(file='tasks.txt', mode='a', encoding='utf-8')

lines = new_tasks_file.readlines()
for line in lines:
    task_name, timeout, do_time = map(str.strip, line.split(','))
    end_line = datetime.now().date() + timedelta(days=int(timeout))
    tasks.append(Task(task_name, end_line, int(do_time)))
    tasks_file.write('%s, %s, %s\n' % (task_name, str(end_line), do_time))

# make new_tasks file empty
new_tasks_file.close()
new_tasks_file = open(file='new_tasks.txt', mode='w', encoding='utf-8')

score_file = open(file='score.txt', mode='w', encoding='utf-8')
tasks.sort(key=lambda x: x.score, reverse=True)
for task in tasks:
    score_file.write(str(task.score) + '\t\t' + task.name + '\n')
    print("*****************", task.name)
    print('score:', task.score)
    print('days left:', task.deadline - datetime.now().date())
    print('hours to do:', task.hours)