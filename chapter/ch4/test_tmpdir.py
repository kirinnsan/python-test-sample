def test_tmpdir(tmpdir):
    # ★tmpdir(関数スコープ以外は使用できない)
    # 1回のテストだけでファイルの読み取り、書き込み、変更を行うテストをする場合に使用

    # ★tmpdir_factory(クラス、モジュール、セッションスコープ利用可)
    # 複数のテストで使用するディレクトリを準備したい場合に使用

    # tmpdirにはパス名が既に関連づけられている
    # join()はファイル名を含むようにパス名を拡張する
    # ファイルは書き込み時に作成される

    a_file = tmpdir.join('something.txt')

    # ディレクトリを作成
    a_sub_dir = tmpdir.mkdir('anything')

    # ディレクトリにファイルを作成できる
    another_file = a_sub_dir.join('something_else.txt')

    # 書き込み（この時にsomething.txtが作成される）
    a_file.write('content is written')

    # 書き込み（この時にanything/something_else.txtが作成される）
    another_file.write('something another is written')

    # ファイルの読み取り
    assert a_file.read() == 'content is written'
    assert another_file.read() == 'something another is written'


def test_tmpdir_factory(tmpdir_factory):
    # ディレクトリ作成
    a_dir = tmpdir_factory.mktemp('mydir')

    # 親ディレクトリ
    # 親ディレクトリを独自に指定したい場合は、pytest --basetemp=<ディレクトリ名>を指定
    # getbasetemp()を使用するひつようはない
    # この関数が使えることのみ示す
    base_tmp = tmpdir_factory.getbasetemp()
    print('base:', base_tmp)

    a_file = a_dir.join('something.txt')

    # ディレクトリを作成
    a_sub_dir = a_dir.mkdir('anything')

    # ディレクトリにファイルを作成できる
    another_file = a_sub_dir.join('something_else.txt')

    # 書き込み（この時にsomething.txtが作成される）
    a_file.write('content is written')

    # 書き込み（この時にanything/something_else.txtが作成される）
    another_file.write('something another is written')

    # ファイルの読み取り
    assert a_file.read() == 'content is written'
    assert another_file.read() == 'something another is written'
