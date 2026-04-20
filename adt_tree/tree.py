class Tree:

    class Position:
        """Abstraction that represents a node of the tree."""
        def element(self):
            """Return the element of the tree."""

            raise NotImplementedError('must implement by subclass')

        def __eq__(self, other):
            """Return true if self and other are the same position."""

            raise NotImplementedError('must implement by subclass')

        def __ne__(self, other):

            return not self == other

    # ----------- abstract methods that have to be made concrete in the subclass -----------------

    def root(self):
        """Return the Position representing the root or None if the tree is empty."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """Return the Position representing the parent of p or None if p is the root."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children of p."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generates an iterator on the Position representing the children of p."""
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        """Return the number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    # ------------------- some concrete methods implemented in this class -------------------------

    def is_root(self, p):
        """Return True if p represents the root."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if p represents a leaf."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Retturn the depth of p in the tree."""
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def height(self, p = None):
        """Return the height of the subtree rooted in p;
        the height of the tree if p = None."""
        if p is None:
            p = self.root()
        return self._height2(p)

    def _height2(self, p):
        """Return the height of p."""
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height2(c) for c in self.children(p))
