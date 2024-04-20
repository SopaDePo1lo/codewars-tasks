def make_readable(seconds):
    _seconds = seconds%60
    seconds = int(seconds/60)
    return ('{:02}:{:02}:{:02}').format(int(seconds/60), seconds%60, _seconds)

make_readable(86399)