from fastapi import FastAPI

app = FastAPI()

my_tasks = ["go for a run", "make dinner", "write some code"]


# read all tasks
@app.get("/")
def get_all_tasks():  # root?
    return my_tasks


# read specific task
@app.get("/tasks/{id}")
def get_task(id: int):
    return my_tasks[id]


# add new task
@app.post("/")
def add_task(new_task: str):
    my_tasks.append(new_task)
    return my_tasks


# update task
@app.put("/tasks/{id}")
def update_task(id: int, new_task: str):
    my_tasks[id] = new_task
    return my_tasks


# delete task
@app.delete("/tasks/{id}")
def delete_task(id: int):
    del my_tasks[id]
    return my_tasks
