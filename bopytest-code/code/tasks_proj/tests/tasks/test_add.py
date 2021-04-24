import pytest
import tasks
from tasks import Task


# @pytest.fixture(autouse=True)
# def initialized_task_db(tmpdir):
#     # Task DBを初期化
#     tasks.start_tasks_db(str(tmpdir), 'tiny')

#     # ここでテストを実行
#     yield

#     # DB接続終了
#     tasks.stop_tasks_db()


def test_add_retruns_valid_id(tasks_db):
    new_task = Task('do something')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)


def test_add_task_increment(db_with_3_tasks):
    tasks.add(Task('add one task'))

    assert tasks.count() == 4


@pytest.mark.smoke
def test_added_task_has_id_set(tasks_db):
    new_task = Task('sit in chair', owner='me', done=True)
    task_id = tasks.add(new_task)

    task_from_db = tasks.get(task_id=task_id)
    assert task_from_db.id == task_id


# def test_unique_id(tasks_db):
#     id_1 = tasks.unique_id()
#     id_2 = tasks.unique_id()
#     assert id_1 != id_2


# @pytest.mark.xfail(tasks.__version__ < '0.2.0', reason='not supported until version')
def test_unique_id_2(tasks_db):
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))

    uid = tasks.unique_id()

    assert uid not in ids
