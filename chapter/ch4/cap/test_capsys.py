import sys


def greeting(name):
    print(f'Hi,{name}')


def yikes(problem):
    print(f'Yikes!{problem}', file=sys.stderr)


def test_greeting(capsys):
    """capsysは2つの機能をもつフィクスチャ
    1.コードから標準出力(stdout)、標準エラー(stderr)を取得する
    2.出力のキャプチャを一時的に無効化する
    """
    greeting('HogeHoge')
    # readouterr()で標準出力(stdout)、標準エラー(stderr)を取得できる
    out, err = capsys.readouterr()
    assert out == 'Hi,HogeHoge\n'
    assert err == ''

    greeting('Hoo')
    greeting('Bar')
    greeting('Baz')
    out, err = capsys.readouterr()
    assert out == 'Hi,Hoo\nHi,Bar\nHi,Baz\n'
    assert err == ''


def test_yiles(capsys):
    # 標準エラー(stderr)の確認
    yikes('Out of Hoge')
    out, err = capsys.readouterr()
    assert out == ''
    assert 'Out of Hoge' in err


def test_capsys_disabled(capsys):
    # capsys.disabled()を使用すると-sオプションをつけなくても常に表示される
    with capsys.disabled():
        print('\nalways print this')
    print('normal print, usually captured')
