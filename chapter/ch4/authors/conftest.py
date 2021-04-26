import json
import pytest


@pytest.fixture(scope='module')
def author_file_json(tmpdir_factory):
    """一時ディレクトリ、ファイルを作成し、
    JSONフォーマットでデータを書き込む
    """

    python_author_data = {
        'Ned': {'City': 'Boston'},
        'Brian': {'City': 'Tokyo'},
        'Lucio': {'City': 'London'},
    }

    file = tmpdir_factory.mktemp('data').join('author_file.json')
    print(f'file:{str(file)}')

    with file.open('w') as f:
        json.dump(python_author_data, f)

    return file
