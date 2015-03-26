import sublime, sublime_plugin

toggle = True

class wowMeCommand(sublime_plugin.EventListener):

	def onLoad(self, view):
		global toggle
		toggle = True

	def on_selection_modified_async(self,view):
		for region in view.sel():
			str = view.substr(view.word(region))
			if str.lower() == 'doge':
				if toggle:	
					view.show_popup("""─────────▄──────────────▄\n
			────────▌▒█───────────▄▀▒▌\n
			──WOW───▌▒▒▀▄───────▄▀▒▒▒▐\n
			───────▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐\n
			─────▄▄▀▒▒▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐\n
			───▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀██▀▒▌\n
			──▐▒▒▒▄▄▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄▒▒▌\n
			──▌▒▒▐▄█▀▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐\n
			─▐▒▒▒▒▒▒▒▒▒▒▒▌██▀▒▒▒▒▒▒▒▒▀▄▌\n
			─▌▒▀▄██▄▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌\n
			─▌▀▐▄█▄█▌▄▒▀▒▒▒▒▒▒░░░░░░▒▒▒▐\n
			▐▒▀▐▀▐▀▒▒▄▄▒▄▒▒▒▒▒░░░░░░▒▒▒▒▌\n
			▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒░░░░░░▒▒▒▐\n
			─▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒▒▒░░░░▒▒▒▒▌\n
			─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐\n
			""", on_navigate=print)

class toggleCommand(sublime_plugin.TextCommand):

	def run(self, edit):
		global toggle
		toggle = not toggle


