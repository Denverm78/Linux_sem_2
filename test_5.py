import subprocess


def check_out(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def check_out_crc(cmd):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout


def check_error(cmd, text):
    result = subprocess.run(cmd, shell=True, stderr=subprocess.PIPE, encoding='utf-8')
    print(result.stderr)
    if text in result.stderr and result.returncode != 0:
        return True
    else:
        return False


def test_step1():
    assert check_out(f'cd {folder_out}; 7z a {folder_arh}/arh1', 'Everything is Ok'), 'test_1 FAIL'
    # assert checkout(f'ls {folder_arh}', 'arh1.7z'), 'test_1 FAIL'


def test_step2():
    assert check_out(f'cd {folder_out}; 7z u {folder_arh}/arh1', 'Everything is Ok'), 'test_2 FAIL'


def test_step3():
    assert check_out(f'cd {folder_arh}; 7z d {folder_arh}/arh1 3.txt', 'Everything is Ok'), 'test_3 FAIL'


def test_step4():
    assert check_error(f'cd {folder_arh}; 7z e {folder_arh}/bad_arh.7z', 'No more files'), 'test_4 FAIL'


def test_step5():
    assert check_error(f'cd {folder_arh}; 7z t {folder_arh}/bad_arh1.7z', 'No more files'), 'test_5 FAIL'


def test_step6():
    assert check_out(f'cd {folder_arh}; 7z l {folder_arh}/arh1.7z', '1.txt'), 'test_6 FAIL'
    assert check_out(f'cd {folder_arh}; 7z l {folder_arh}/arh1.7z', '2.txt'), 'test_6 FAIL'


def test_step7():
    assert check_out(f'cd {folder_arh}; 7z e {folder_arh}/arh1.7z', 'Everything is Ok'), 'test_7 FAIL'


def test_step8():
    file_hash = check_out_crc(f'cd {folder_out}; crc32 {folder_out}1.txt')
    print(file_hash)
    assert check_out(f'cd {folder_out}; 7z h {folder_out}/1.txt', file_hash), 'test_8 FAIL'


folder_out = '/home/user/tst/tst_out'
folder_arh = '/home/user/tst/tst_arh'
