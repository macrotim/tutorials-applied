import tempfile
import os

import pytest
import sqlite3

"""Use @pytest.fixture instead of setUp."""

client_counter = 0

class Client:
    def __init__(self):
        global client_counter
        self.id = client_counter
        client_counter += 1

    def is_up(self):
        return True

    def is_down(self):
        return not self.is_up()

    def destroy(self):
        pass

# scope=module results in one Client
# cached for all tests in the same module
@pytest.fixture(scope="module")
def client(request):
    """"request is the py.test request object."""
    client = Client()
    def fin():
        client.destroy()
    request.addfinalizer(fin)  # equivalent to "teardown"
    return client

def test_up(client):
    assert client.is_up()
    assert client.id == 0

def test_down(client):
    assert not client.is_down()
    assert client.id == 0

"""Another pytest fixture to demonstrate the use of multiple fixtures."""

@pytest.fixture
def connection(request):
    connection = sqlite3.connect(':memory:')
    connection.execute('''create table user (id integer primary key, username varchar)''')
    return connection

def test_create_user(connection):
    connection.execute('''insert into user (username) values ('ed.sheeran')''')
    count, = connection.execute('''select count(*) from user''').fetchone()
    assert count == 1

"""usefixtures"""

@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)

@pytest.mark.usefixtures("cleandir")
class TestDirectoryInit:
    def test_cwd_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
        with open("myfile", "w") as f:
            f.write("hello")

    def test_cwd_again_starts_empty(self):
        assert os.listdir(os.getcwd()) == []
