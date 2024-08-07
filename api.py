from fastapi import FastAPI, HTTPException, Header
from IOTaskManager.manager import ThreadManager
from IOTaskManager.dynamic_loader import load_task_class

app = FastAPI()
manager = ThreadManager()

# 设定 API Key
VALID_API_KEY = "1234567abcdefg"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != VALID_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

@app.post("/start/{task_name}")
def start_task(task_name: str, interval: float, x_api_key: str = Header(...)):
    verify_api_key(x_api_key)
    task_class = load_task_class(task_name)
    if not task_class:
        raise HTTPException(status_code=404, detail=f"Task {task_name} not found.")
    manager.start_thread(task_name, task_class, interval)
    return {"message": f"Task {task_name} started with interval {interval}"}

@app.post("/stop/{task_name}")
def stop_task(task_name: str, x_api_key: str = Header(...)):
    verify_api_key(x_api_key)
    manager.stop_thread(task_name)
    return {"message": f"Task {task_name} stopped."}

@app.get("/list")
def list_tasks(x_api_key: str = Header(...)):
    verify_api_key(x_api_key)
    running_tasks = manager.list_running_threads()
    return {"running_tasks": running_tasks}

@app.post("/stop_all")
def stop_all_tasks(x_api_key: str = Header(...)):
    verify_api_key(x_api_key)
    manager.stop_all_threads()
    return {"message": "All tasks stopped."}