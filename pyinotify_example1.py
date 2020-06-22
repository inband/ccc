import pyinotify


file_position = 0
file_name = '/tmp/test.config'

# The watch manager stores the watches and provides operations on watches
wm = pyinotify.WatchManager()

#mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.ALL_EVENTS  # watched events
mask = pyinotify.IN_MODIFY


def get_file_changes(check_file):
    f = open(check_file)
    global file_position
    print(f'Before: {file_position}')
    i = f.seek(file_position)
    changes = f.read()
    if 'a' in changes:
        print(changes)
    new_pos = f.tell()
    file_position = new_pos
    print(f'After: {file_position}')

class EventHandler(pyinotify.ProcessEvent):
#    def process_IN_CREATE(self, event):
#        print(f'Creating: {event.pathname}')

#   def process_IN_DELETE(self, event):
#        print(f'Removing: {event.pathname}')

    def process_IN_MODIFY(self, event):
        print(f'Modified: {event.pathname}')
        get_file_changes(file_name)



handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)

wdd = wm.add_watch('/tmp/test.config',mask , rec=True) 

notifier.loop()




