# IOTaskManager

## 项目简介

`IOTaskManager` 是一个基于 FastAPI 构建的任务管理系统，支持使用 API Key 认证的 REST API 服务。该系统允许用户动态启动和停止 I/O 密集型任务，适合多线程任务管理。用户可以通过 HTTP 请求管理任务，支持任务的启动、停止、查询等操作。

## 功能特点

- **任务管理**：支持启动、停止和列出任务。
- **多线程支持**：每个任务以独立的线程运行，互不干扰。
- **API Key 认证**：通过 API Key 保护接口，确保系统安全。
- **REST API**：提供标准的 REST API 接口，方便集成和扩展。

## 安装指南

### 环境要求

- Python 3.7+
- FastAPI
- Uvicorn

### 安装步骤

1. **克隆仓库**

```bash
git clone <仓库地址>
cd IOTaskManager
```

2. **创建虚拟环境（可选）**

```bash
python3 -m venv .venv
source .venv/bin/activate
which python3

# 退出
deactivate
```

3. **安装依赖**

```bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 使用方法

### 启动 API 服务
在项目根目录下运行以下命令启动 FastAPI 服务器：

```bash
uvicorn api:app --reload
```
API 服务将会在 http://127.0.0.1:8000 上运行。

更换端口

```bash
uvicorn api:app --reload --port 8001
```

后台运行

```bash
nohup uvicorn api:app --reload --port 8001 > uvicorn.log 2>&1 &
```

### API 端点

•	启动任务
	•	URL: /start/{task_name}
	•	方法: POST
	•	参数:
	  •	task_name: 任务类的完整路径（如 IOTaskManager.task.IOTask）
	  •	interval: 任务执行间隔（秒）
	•	Headers:
	  •	x-api-key: 1234567abcdefg（需要替换为实际的 API Key）
	•	示例:
```bash
curl -X POST "http://127.0.0.1:8000/start/IOTaskManager.task.IOTask?interval=2" \
    -H "x-api-key: 1234567abcdefg"
```

•	停止任务
	•	URL: /stop/{task_name}
	•	方法: POST
	•	参数:
	  •	task_name: 任务类的完整路径
	•	Headers:
	  •	x-api-key: 1234567abcdefg
	•	示例:

```bash
curl -X POST "http://127.0.0.1:8000/stop/IOTaskManager.task.IOTask" \
    -H "x-api-key: 1234567abcdefg"
```

•	列出所有运行中的任务
	•	URL: /list
	•	方法: GET
	•	Headers:
	  •	x-api-key: 1234567abcdefg
	•	示例:
```bash
curl -X GET "http://127.0.0.1:8000/list" \
    -H "x-api-key: 1234567abcdefg"
```

•	停止所有任务
	•	URL: /stop_all
	•	方法: POST
	•	Headers:
	  •	x-api-key: 1234567abcdefg
	•	示例:
```bash
curl -X POST "http://127.0.0.1:8000/stop_all" \
    -H "x-api-key: 1234567abcdefg"
```