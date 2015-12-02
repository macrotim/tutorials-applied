"""An exercise to unit test LessWatcher.

   One issue is with Watchdog's FileSystemEventHandler which triggers after
   a significant delay on OSX. I didn't probe further but as is, the
   slowness of this unit test is impractical.
   """

import os
import time
import pytest
from less_watcher import LessWatcher

EVENT_HANDLER_DELAY = 1 # yikes, any less than 1 sec and tests fail on OSX

def osjoin(less_watcher, filename):
    return os.path.join(less_watcher.path, filename)

@pytest.fixture
def less_watcher(request, tmpdir):
    tmpdir = tmpdir.mkdir('watchme')
    lw = LessWatcher(tmpdir.strpath).start()
    time.sleep(EVENT_HANDLER_DELAY)

    def fin():
        lw.stop()
        lw.join()
    request.addfinalizer(fin)

    return lw

def test_has_changed_on_create_edit_delete(less_watcher):
    lw = less_watcher
    with open(osjoin(lw, 'plain.txt'), 'w') as f:
        f.write('v0')
    time.sleep(EVENT_HANDLER_DELAY)
    assert lw.has_changed() is True
    assert lw.has_changed() is False

    with open(osjoin(lw, 'plain.txt'), 'w') as f:
        f.write('v1')
    time.sleep(EVENT_HANDLER_DELAY)
    assert lw.has_changed() is True
    assert lw.has_changed() is False

    os.unlink(osjoin(lw, 'plain.txt'))
    time.sleep(EVENT_HANDLER_DELAY)
    assert lw.has_changed() is True
    assert lw.has_changed() is False
