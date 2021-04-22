import pytest
import tasks
from tasks import Task


@pytest.fixture(autouse=True)
def initialized_task_db(tmpdir):
    # Task DBを初期化
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    # ここでテストを実行
    yield

    # DB接続終了
    tasks.stop_tasks_db()


def test_add_retruns_valid_id():
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


@pytest.mark.smoke
def test_added_task_has_id_set():
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    task_from_db = tasks.get(task_id=task_id)
    assert task_from_db.id == task_id
