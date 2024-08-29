import pytest
import Task_1 as cls_module
import datetime


@pytest.fixture
def sample_task():
    def wrapper(description, priority=1, deadline=None):
        return cls_module.Task(description, priority, deadline)

    return wrapper


@pytest.fixture
def task_list():
    return cls_module.TaskList()


def test_task_initialization(sample_task):
    task = sample_task("Sample task")
    assert task.priority == 1
    assert task.deadline is None
    assert task.is_completed is False


def test_mark_completed(sample_task):
    task = sample_task("Sample task")
    task.mark_completed()
    assert task.is_completed is True


def test_set_deadline(sample_task):
    task = sample_task("Sample task")
    deadline = datetime.datetime(2023, 10, 1)
    task.set_deadline(deadline)

    assert task.deadline == deadline


def test_task_string_representation(sample_task):
    task = sample_task("Sample task")
    right_spelling = f"Description: {task.description}\nPriority: {task.priority}\nStatus: Not Completed\nNo Deadline\n"
    assert task.__str__() == right_spelling


def test_tasklist_initialization(task_list):
    assert len(task_list.tasks) == 0


def test_add_task(sample_task, task_list):
    task = sample_task("Sample task")
    task_list.add_task(task)
    assert len(task_list.tasks) == 1
    assert task_list.tasks[0] == task


def test_remove_task(sample_task, task_list):
    task = sample_task("Sample task")
    task_list.add_task(task)
    assert len(task_list.tasks) == 1
    task_list.remove_task(task)
    assert len(task_list.tasks) == 0
    assert task not in task_list.tasks


def test_sort_by_priority(sample_task, task_list):
    task1 = sample_task(description="First sample task", priority=1)
    task_list.add_task(task1)
    task2 = sample_task(description="Second sample task", priority=2)
    task_list.add_task(task2)
    task_list.sort_by_priority()
    assert task_list.tasks[0].priority >= task_list.tasks[1].priority


def test_filter_by_status(sample_task, task_list):
    task1 = sample_task(description="First sample task")
    task1.mark_completed()
    task_list.add_task(task1)

    task2 = sample_task(description="Second sample task")
    task_list.add_task(task2)

    new_task_list = task_list.filter_by_status(completed=True)

    assert len(new_task_list) == 1
