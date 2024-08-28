from flask import Flask, request, jsonify, Response
import json

app = Flask(__name__)
all_tasks = list()


@app.post("/tasks")
def tasks_post():
    response = request.json
    new_task = {
        "title": response["title"],
        "task_id": len(all_tasks) + 1,
        "description": response["description"],
    }
    all_tasks.append(new_task)

    return (new_task, 200, {"content-type": "application/json"})


@app.delete("/tasks/<id>")
def tasks_delete(id):
    if len(all_tasks) < int(id):
        return f"{all_tasks}"
    else:
        for item in all_tasks:
            if item["task_id"] == int(id):
                all_tasks.remove(item)
                return jsonify({"message": "Задача успешно удалена"}), 200


@app.get("/tasks")
def tasks_ger():
    r = Response()
    r.minetype = "application/json"
    my_dict = dict()
    my_dict["tasks"] = all_tasks
    r.response = json.dumps(my_dict)
    return r


if __name__ == "__main__":
    app.run(debug=True)
