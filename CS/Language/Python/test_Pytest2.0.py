# Two issues with this test code
# 1. Code Repetition
# 2. Creating expensive DB connection in every test case
# .................................................
# from Pytest2 import MyDB

# def test_johns_id():
#     db = MyDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
#     id = cur.execute("select id from employee_db where name=John")
#     assert id == 123

# def test_toms_id():
#     db = MyDB()
#     conn = db.connect("server")
#     cur = conn.cursor()
#     id = cur.execute("select id from employee_db where name=toms")
#     assert id == 789

# ---------------------------------------------------------
# Two ways to fix those issues,
# 1. setup and teardown methods(classic xunit style)
# 2. fixtures(recommended)
# ......................................................

# 1) setup and teardown methods(classic xunit style)
# from Pytest2 import MyDB

# conn = None
# cur = None

# def setup_module(module):
#     global conn
#     global cur
#     db = MyDB()
#     conn = db.connect("server")
#     cur = conn.cursor()

# def teardown_module(module):
#     cur.close()
#     conn.close()

# def test_johns_id():
#     cur = conn.cursor()
#     id = cur.execute("select id from employee_db where name=John")
#     assert id == 123

# def test_toms_id():
#     cur = conn.cursor()
#     id = cur.execute("select id from employee_db where name=toms")
#     assert id == 789

........................................................
# 2. fixtures(recommended)
# Fixtures leverage a concept of *dependancy injection*
# 依赖注入方法是：
# 1. 抽象依赖为接口
# 2. 持有接口为变量
# 3. 公有接口设函数
# 这三个步骤，fixture 都具备
# https://www.youtube.com/watch?v=IVrGz8w0H8c&index=36&list=PLeo1K3hjS3usILfyvQlvUBokXkHPSve6S



from Pytest2 import MyDB
import pytest

@pytest.fixture(scope = "module")
def cur():
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    curs.close()
    conn.close()

# 注意这个参数是一个函数名cur
# 这两个函数都依赖 cur
def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

# 注意这个参数是一个函数名cur
def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=toms")
    assert id == 789
