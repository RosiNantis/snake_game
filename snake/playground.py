class Playground:

    def __init__(self,xsize,ysize):
        self.xsize = xsize
        self.ysize = ysize

    @property
    def size(self):
        """instead of self.size attribute"""
        return self.xsize, self.ysize

    def is_obstacle(self,position):
        x, y =position
        if (
            0 < x < self.xsize and
            0 < x < self.ysize
        ):
            return False
        return True