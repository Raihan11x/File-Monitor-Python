import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import os

class FileChangeHandler(FileSystemEventHandler):
    """Handler for file system events"""
    
    def __init__(self, log_file):
        super().__init__()

        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=log_file,
            filemode='a'
        )
        self.logger = logging.getLogger(__name__)
    
    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            rel_path = os.path.relpath(file_path, start=os.path.dirname(os.path.abspath(__file__)))
            self.logger.info(f"File Created: {rel_path}")
    
    def on_modified(self, event):
        if not event.is_directory:
            file_path = event.src_path
            rel_path = os.path.relpath(file_path, start=os.path.dirname(os.path.abspath(__file__)))
            # Avoid logging modifications to the log file itself
            if not rel_path.endswith('monitor.log'):
                self.logger.info(f"File Modified: {rel_path}")
    
    def on_deleted(self, event):
        if not event.is_directory:
            file_path = event.src_path
            rel_path = os.path.relpath(file_path, start=os.path.dirname(os.path.abspath(__file__)))
            self.logger.info(f"File Deleted: {rel_path}")

def monitor_directory(path_to_watch, log_file):
    """
    Monitor a directory for changes and log events
    
    Args:
        path_to_watch (str): Directory path to monitor
        log_file (str): Path to the log file
    """
    event_handler = FileChangeHandler(log_file)
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=True)
    
    observer.start()
    print(f"Started monitoring directory: {path_to_watch}")
    print(f"Logging events to: {log_file}")
    print("Press Ctrl+C to stop monitoring...")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("\nMonitoring stopped.")
    
    observer.join()

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    log_file = os.path.join(current_dir, "monitor.log")
    
    monitor_directory(current_dir, log_file)