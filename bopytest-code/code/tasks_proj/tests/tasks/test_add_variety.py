import pytest
import tasks
from tasks import Task


def test_add_1():
    task = Task('breath', 'BRAIN', True)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)

    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('task', [Task('sleep', done=True),
                                  Task('wake', 'brian', done=True),
                                  Task('breathe', 'BRAIN', done=True),
                                  Task('exercize', 'brlaN', done=False)])
def test_add_2(task):
    # テストのパラメータ化→@pytest.mark.parametrizeを使う
    # 関数の引数とparametrizeの第一引数は同じにする
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)

    assert equivalent(t_from_db, task)


@pytest.mark.parametrize('summary, owner, done', [('sleep', None, False),
                                                  ('wake', 'brian', False),
                                                  ('breathe', 'BRAIN', True),
                                                  ('exercize', 'brlaN', False)])
def test_add_3(summary, owner, done):
    # テストパラメータが複数の場合のパラメータ化
    # タスクの中身をタプルで渡す

    task = Task(summary, owner, done)
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)

    assert equivalent(t_from_db, task)


def test_count():
    task = Task('breath', 'BRAIN', True)
    task2 = Task('breath1', 'BRAIN1', True)
    tasks.add(task)
    tasks.add(task2)
    task_number = tasks.count()

    assert task_number == 2


def test_conftest_fixture(tasks_just_a_few):
    for task in tasks_just_a_few:
        tasks.add(task)

    task_number = tasks.count()

    assert task_number == 3


def equivalent(t1, t2):
    return ((t1.summary == t2.summary) and
            (t1.owner == t2.owner) and
            (t1.done == t2.done))


@pytest.fixture(autouse=True)
def initialized_task_db(tmpdir):
    # Task DBを初期化
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    # ここでテストを実行
    yield

    # DB接続終了
    tasks.stop_tasks_db()
