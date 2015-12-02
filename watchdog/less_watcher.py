"""I'm considering a patch to Flask-LessCSS that watches a /css directory
and returns True if any changes were made."""

import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class LessWatcher(object):
    """Watches the specified directory for filesystem changes."""

    def __init__(self, path):
        self.path = path
        self._changed = False

    def has_changed(self):
        v, self._changed = self._changed, False
        return v

    def start(self):
        event_handler = LessWatcher.EventHandler(self)
        observer = Observer()
        observer.schedule(event_handler, self.path, recursive=True)
        observer.start()
        self._observer = observer
        return self

    def stop(self):
        self._observer.stop()

    def join(self):
        self._observer.join()

    class EventHandler(FileSystemEventHandler):
        def __init__(self, less_watcher):
            super(LessWatcher.EventHandler, self).__init__()
            self.less_watcher = less_watcher

        def on_modified(self, event):
            self.less_watcher._changed = True


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    print "Watching directory:", path

    less_watcher = LessWatcher(path).start()
    try:
        while True:
            print
            print 'Hit ENTER.',
            sys.stdin.readline()
            if less_watcher.has_changed():
                print "Files have changed."
            else:
                print "No filesystem changes since last call."
    except KeyboardInterrupt:
        less_watcher.stop()
    less_watcher.join()
