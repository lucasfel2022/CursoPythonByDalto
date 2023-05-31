class MiException(Exception):
    def __init__(self, err):
        print(f'Que boludazo que sos, mira loq ue hiciste: {err}')
        

raise MiException("AAAAAAAAAAAAAAACHUUUUUUUUUU")