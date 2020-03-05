def display_gif(fn):
    '''Source: https://github.com/ipython/ipython/issues/10045'''
    from IPython import display
    return display.HTML('<img src="{}">'.format(fn))