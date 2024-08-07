import importlib

def load_task_class(task_name):
    try:
        module_name, class_name = task_name.rsplit('.', 1)
        print(module_name)
        print(class_name)
        module = importlib.import_module(module_name)
        task_class = getattr(module, class_name)
        return task_class
    except (ImportError, AttributeError, ValueError) as e:
        print(f"Error loading task {task_name}: {e}")
        return None