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


# @pytest.mark.skip(reason='misunderstood the API')
@pytest.mark.xfail(tasks.__version__ < '0.2.0', reason='not supported until version')
def test_unique_id():
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()
    assert id_1 != id_2


def test_unique_id_2():
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))

    uid = tasks.unique_id()

    assert uid not in ids
