import pytest
import tasks
from tasks import Task


task_to_try = (Task('sleep', done=True),
               Task('wake', 'brian', done=True),
               Task('breathe', 'BRAIN', done=True),
               Task('exercize', 'brlaN', done=False))

task_ids = [Task(t.summary, t.owner, t.done) for t in task_to_try]


def equivalent(t1, t2):
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


@pytest.fixture(params=task_to_try)
def a_task(request):
    # requestは組み込みのフィクスチャ
    # request.paramでtask_to_tryに代入されているリストの1つが設定
    # tasks_to_tryが4件あるため、このフィクスチャも4回呼ばれる
    return request.param


@pytest.fixture(params=task_to_try)
def b_task(request):
    return request.param


def test_add_a(tasks_db, a_task):
    # tasks_to_tryが4件あるため、このテストは4回呼ばれる
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)


def test_add_b(tasks_db, b_task):
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)


@pytest.fixture(autouse=True)
def initialized_task_db(tmpdir):
    # Task DBを初期化
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    # ここでテストを実行
    yield

    # DB接続終了
    tasks.stop_tasks_db()
