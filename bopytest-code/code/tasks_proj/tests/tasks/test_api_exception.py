import pytest
import tasks

from tasks.api import UninitializedDatabase


def test_raises():
    with pytest.raises(TypeError):
        tasks.add(task='Not a Task object')


def test_start_tasks_db():
    with pytest.raises(ValueError) as execinfo:
        tasks.start_tasks_db('some/great/path', 'mysql')
    # execinfo.value.args[0]で例外の値を取得
    # またはstr(execinfo.value)
    # exception_msg = execinfo.value.args[0]
    exception_msg = str(execinfo.value)
    assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


@pytest.mark.smoke
def test_list_tasks_raises():
    # smokeとgetというマーカーは独自に作成したもの
    with pytest.raises(TypeError):
        tasks.list_tasks(owner=123)


@pytest.mark.get
@pytest.mark.smoke
def test_get_raises():
    with pytest.raises(TypeError) as execinfo:
        tasks.get(task_id='123')

    exception_msg = str(execinfo.value)
    assert exception_msg == 'task_id must be an int'


def test_count_raise():
    with pytest.raises(UninitializedDatabase):
        tasks.count()
