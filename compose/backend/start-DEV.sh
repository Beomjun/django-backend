#!/bin/bash
python manage.py makemessages --all

make html -C /webapps/django/docs

# launch dev server
python manage.py migrate && python manage.py runserver_plus 0.0.0.0:8000

# when launching failed, watch files and try to launch again
function wait_for_file_change(){
python << END
import sys, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

file_changed = False

class TestEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        global file_changed
        if not file_changed:
            file_changed = True

if __name__ == "__main__":
    event_handler = TestEventHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()
    try:
        while not file_changed:
            print("Currently Django runserver stopped. Wait for file changes...")
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
        file_changed = True
    sys.exit(-1)
    observer.join()
END
}

until wait_for_file_change; do
  echo "Detected file changes. Retry to launch Django dev server..."
  python manage.py makemessages --all
  python manage.py clean_pyc --path /webapps/django && python manage.py clear_cache

  make html -C /webapps/django/docs

  python manage.py runserver_plus 0.0.0.0:8000
done
