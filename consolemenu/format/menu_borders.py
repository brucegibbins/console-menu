class MenuBorderStyle(object):
    """
    Base class for console menu border. Each propery should be overridden by a subclass.
    """
    @property
    def bottom_left_corner(self): raise NotImplementedError()

    @property
    def bottom_right_corner(self): raise NotImplementedError()

    @property
    def inner_horizontal(self): raise NotImplementedError()

    @property
    def inner_vertical(self): raise NotImplementedError()

    @property
    def intersection(self): raise NotImplementedError()

    @property
    def outer_horizontal(self): raise NotImplementedError()

    @property
    def outer_horizontal_inner_up(self): raise NotImplementedError()

    @property
    def outer_horizontal_inner_down(self): raise NotImplementedError()

    @property
    def top_left_corner(self): raise NotImplementedError()

    @property
    def top_right_corner(self): raise NotImplementedError()

    @property
    def outer_vertical(self): raise NotImplementedError()

    @property
    def outer_vertical_inner_left(self): raise NotImplementedError()

    @property
    def outer_vertical_inner_right(self): raise NotImplementedError()


class AsciiBorderStyle(MenuBorderStyle):

    @property
    def bottom_left_corner(self): return '+'

    @property
    def bottom_right_corner(self): return '+'

    @property
    def inner_horizontal(self): return '-'

    @property
    def inner_vertical(self): return '|'

    @property
    def outer_horizontal(self): return '-'

    @property
    def outer_horizontal_inner_up(self): return '+'

    @property
    def outer_horizontal_inner_down(self): return '+'

    @property
    def intersection(self): return '+'

    @property
    def top_left_corner(self): return '+'

    @property
    def top_right_corner(self): return '+'

    @property
    def outer_vertical(self): return '|'

    @property
    def outer_vertical_inner_left(self): return '|'

    @property
    def outer_vertical_inner_right(self): return '|'


class UnicodeLightBorderStyle(MenuBorderStyle):
    """
    MenuBorderStyle class using Unicode "light" line characters.
    """
    @property
    def bottom_left_corner(self): return u'\u2514'

    @property
    def bottom_right_corner(self): return u'\u2518'

    @property
    def inner_horizontal(self): return u'\u2500'

    @property
    def inner_vertical(self): return u'\u2502'

    @property
    def intersection(self): return u'\u253C'

    @property
    def outer_horizontal(self): return u'\u2500'

    @property
    def outer_horizontal_inner_up(self): return u'\u2534'

    @property
    def outer_horizontal_inner_down(self): return u'\u252C'

    @property
    def top_left_corner(self): return u'\u250C'

    @property
    def top_right_corner(self): return u'\u2510'

    @property
    def outer_vertical(self): return u'\u2502'

    @property
    def outer_vertical_inner_left(self): return u'\u2524'

    @property
    def outer_vertical_inner_right(self): return u'\u251C'


class UnicodeHeavyBorderStyle(MenuBorderStyle):
    """
    MenuBorderStyle class using Unicode "heavy" line characters.
    """
    @property
    def bottom_left_corner(self): return u'\u2517'

    @property
    def bottom_right_corner(self): return u'\u251B'

    @property
    def inner_horizontal(self): return u'\u2501'

    @property
    def inner_vertical(self): return u'\u2503'

    @property
    def intersection(self): return u'\u254B'

    @property
    def outer_horizontal(self): return u'\u2501'

    @property
    def outer_horizontal_inner_up(self): return u'\u253B'

    @property
    def outer_horizontal_inner_down(self): return u'\u2533'

    @property
    def top_left_corner(self): return u'\u250F'

    @property
    def top_right_corner(self): return u'\u2513'

    @property
    def outer_vertical(self): return u'\u2503'

    @property
    def outer_vertical_inner_left(self): return u'\u2520'

    @property
    def outer_vertical_inner_right(self): return u'\u252B'