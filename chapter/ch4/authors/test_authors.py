import json

# author_file_jsonフィクスチャを使用しているが
# どちらのテストも同じJSONファイルが使用される


def test_brian_in_portland(author_file_json):
    with author_file_json.open() as f:
        authors = json.load(f)

    assert authors['Brian']['City'] == 'Tokyo'


def test_all_have_cities(author_file_json):
    with author_file_json.open() as f:
        authors = json.load(f)

    for a in authors:
        assert len(authors[a]['City']) > 0
