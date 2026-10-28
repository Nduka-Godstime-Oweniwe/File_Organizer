import pathlib
def get_root():
    root=pathlib.Path().cwd()
    while root!=root.parent:
        root=root.parent
    return root