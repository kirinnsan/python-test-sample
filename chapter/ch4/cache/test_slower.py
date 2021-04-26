import datetime
import random
import time

import pytest


@pytest.fixture(autouse=True)
def check_duration(request, cache):
    """テスト時間を記録する"""

    # requestオブジェクトキーで使用されるnodeidの取得に使用
    key = 'duration/' + request.node.nodeid.replace(':', '_')
    # nodeidはコロンが含まれることがある
    # keyは.cacheディレクトリのファイル名になる
    # コロンをファイル名で有効な文字に置き換える

    start_time = datetime.datetime.now()
    yield

    stop_time = datetime.datetime.now()
    this_duration = (stop_time - start_time).total_seconds()
    last_duration = cache.get(key, None)
    cache.set(key, this_duration)

    if last_duration is not None:
        errorstring = 'test duration over 2x last duration'
        assert this_duration <= last_duration * 2, errorstring


@pytest.mark.parametrize('i', range(5))
def test_slow_stuff(i):
    time.sleep(random.random())
