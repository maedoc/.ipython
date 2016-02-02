c = get_config()

mods = 'os re shutil sys os.path glob fnmatch zipfile time subprocess'
c.InteractiveShellApp.exec_lines = [
    'import %s' % (mod, )
    for mod in mods.split(' ')
]
print ('imported %r' % (mods, ))

c.InteractiveShell.readline_parse_and_bind = ['set editing-mode vi']

