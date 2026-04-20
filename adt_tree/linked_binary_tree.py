from adt_tree.binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):


    class _Node:
        """nested class _Node"""
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent, left, right):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """Public class that wraps a node."""

        def __init__(self, container, node):
            """Constructor should not be invoked by the user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element contained in the Position."""
            return self._node._element

        def __eq__(self, other):
            """Return True if other refers to the same Position."""
            return type(other) is type(self) and other._node is self._node

    def _validate(self,p):
        """Return the node contained in p if the Position is valid."""
        if not isinstance(p,self.Position):
            raise TypeError('p must be a Position instance')
        if p._container is not self:
            raise ValueError('p must be a Position instance')
        if p._node._parent is p._node:
            raise ValueError('p is not valid')
        return p._node

    def _make_position(self,node):
        """Return a Position that works as a wrapper for node (None if there is no node)."""
        return self.Position(self,node) if node is not None else None

    def __init__(self):
        """Create an empty tree."""
        self._root = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the tree."""
        return self._size

    def root(self):
        """Return the Position representing the root of the tree (or None if the Tree is empty)."""
        return self._make_position(self.root)

    def parent(self,p):
        """Return the Position representing the parent of p (or None if p is the root)."""
        node = self._validate(p)
        return self._make_position(node)

    def left(self, p):
        """Return the Position representing the left child of p (or None if p has no left child)."""
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """Return the Position representing the right child of p (or None if p has no right child)."""
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """Return the number of children of p."""
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def _add_root(self,e):
        """Insert e in the root of an empty tree and return a new Position.
        Raise ValueError if the tree is not empty."""
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self,e):
        """Add a left child to p containing the element e and return the Position of
        the new node. Raise ValueError if p is not valid, or it has already a left child."""
        node = self._validate(e)
        if node._left is not None:
            raise ValueError('Left child already exists')
        self._size += 1
        node._left = self._Node(e,node)
        return self._make_position(node._left)

    def _add_right(self,e):
        """Add a right child to p containing the element e and return the Position of
        the new node. Raise ValueError if p is not valid, or it has already a right child."""
        node = self._validate(e)
        if node._right is not None:
            raise ValueError('Left child already exists')
        self._size += 1
        node._right = self._Node(e,node)
        return self._make_position(node._right)

    def _replace(self,p,e):
        """Substitute the element contained in p and return the old value."""
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _attach(self, p, t1, t2):
        """Attach t1 and t2 to p as left and right subtrees, respectively.
        Raise TypeError if t1 and t2 are not of the correct type.
        Raise ValueError if p is not valid, or it has children.
        """
        node = self._validate(p)  # recovers the node incapsulated in p
        if not self.is_leaf(p):
            raise ValueError('position must be a leaf')
        if not type(self) is type(t1) is type(t2):  # all the trees must be of the same type
            raise TypeError('trees must be of the same type')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # if t1 is not empty, attach t1 as left subtree
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # after the attachment t1 refers to an empty subtree
            t1._size = 0
        if not t2.is_empty():  # if t2 is not empty, attach t2 as right subtree
            t2._root._parent = node
            node._right = t2._root
            t2._root = None  # after the attachment t2 refers to an empty subtree
            t2._size = 0

        def _delete(self, p):
            """Delete node contained in Position p and replaces it with one of its children, if there is one.
            Return the element saved in Position p.
            Raise ValueError if p is either not valid or it has two children."""
            node = self._validate(p)
            if self.num_children(p) == 2:
                raise ValueError('Position has two children')
            child = node._left if node._left else node._right
            if child is not None:
                child._parent = node._parent  # attach the child to its grand-parent
            if node is self._root:
                self._root = child  # if node is the root its child becomes the new root
            else:
                parent = node._parent
                if node is parent._left:
                    parent._left = child
                else:
                    parent._right = child
            self._size -= 1
            node._parent = node  # convention for not valid nodes
            return node._element

        def preorder(self):
            """Generate a preorder iterator over all the Position in the tree. Defined for Tree."""
            if not self.is_empty():
                for p in self._subtree_preorder(self.root()):
                    yield p

        def _subtree_preorder(self, p):
            """Generate a preorder iterator over all the Position in the subtree rooted in p."""
            yield p  # visit p before visiting its subtrees
            for c in self.children(p):  # for each child c
                for other in self._subtree_preorder(c):  # make a preorder visit of the subtree rooted at c
                    yield other

        def positions(self):
            """Generates an iterator over all the Position in the tree."""
            return self.preorder()

        def __iter__(self):
            """Generates an iterator over all the elements in the tree."""
            for p in self.positions():  # use same order as positions()
                yield p.element()  # but return elements instead of Position


