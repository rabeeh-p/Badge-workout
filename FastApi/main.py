from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# In-memory data store
tasks = []
task_id_counter = 1

# Pydantic model
class Task(BaseModel):
    title: str
    completed: bool = False

class TaskOut(Task):
    id: int

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to FastAPI ToDo App"}

@app.get("/tasks", response_model=List[TaskOut], tags=["Tasks"])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=TaskOut, tags=["Tasks"])
def create_task(task: Task):
    global task_id_counter
    new_task = {"id": task_id_counter, **task.dict()}
    tasks.append(new_task)
    task_id_counter += 1
    return new_task

@app.put("/tasks/{task_id}", response_model=TaskOut, tags=["Tasks"])
def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task.dict())
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", tags=["Tasks"])
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")



