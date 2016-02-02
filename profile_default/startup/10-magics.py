from IPython.core.magic import register_line_magic

@register_line_magic
def editprof(line):
    import os
    ipy = get_ipython()
    os.system('%s %s' % (
        ipy.editor,
	ipy.profile_dir.location
    ))

del editprof


