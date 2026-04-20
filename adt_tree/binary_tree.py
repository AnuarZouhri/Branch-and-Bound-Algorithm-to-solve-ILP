from adt_tree.tree import Tree


class BinaryTree(Tree):
    """Abstract class implementing the ADT BinaryTree that inheritates form Tree."""

    def left(self,p):
        """Return a Position representing the left child  p and None otherwise."""
        raise NotImplementedError('must be implemented by subclass')

    def right(self,p):
        """Return a Position representing the left child  p and None otherwise."""
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self,p):
        """Return the Position representing the sibling  p and None otherwise."""
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

