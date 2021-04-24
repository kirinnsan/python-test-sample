"""Placeholder."""

# nothing here yet
import sys
import os

import pytest
import tasks
from tasks import Task


sys.path.append(os.path.abspath(os.path.dirname(
    os.path.abspath(__file__)) + "/../src/"))


@pytest.fixture(scope='session')
def task_db_session(tmpdir_factory):
    # フィクスチャのセッションスコープで
    # 一時ディレクトリとデータベース接続設定を実行
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    yield
    tasks.stop_tasks_db()


@pytest.fixture()
def tasks_db(task_db_session):
    # セットアップ
    # tasks.start_tasks_db(str(tmpdir), 'tiny')

    # テスト実行
    # yield

    # ティアーダウン
    # tasks.stop_tasks_db()

    # データベースを空にするのみ
    tasks.delete_all()


@pytest.fixture(scope='session')
def tasks_just_a_few():
    return (
        Task('Write some code', 'Brian', True),
        Task('Code review Brian', 'kaite', False),
        Task('Fix what Brian', 'Michelle', False),
    )


@pytest.fixture(scope='session')
def tasks_mult_per_owner():
    return (
        Task('Make cookie', 'Raphael'),
        Task('Use an emoji', 'Raphael'),
        Task('Move to Japan', 'Raphael'),
        Task('Create', 'Michelle'),
        Task('Inspire', 'Michelle'),
        Task('Encourage', 'Michelle'),
        Task('Do a task', 'Daniel'),
        Task('Write some book', 'Daniel'),
        Task('Eat rice', 'Daniel'),
    )


@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    # 複数のフィクスチャを受け取る
    for task in tasks_just_a_few:
        tasks.add(task)


@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_mult_per_owner):
    # 複数のフィクスチャを受け取る
    for task in tasks_mult_per_owner:
        tasks.add(task)
