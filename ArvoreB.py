# coding=utf-8


from __future__ import (nested_scopes, generators, division, absolute_import, with_statement,
                        print_function, unicode_literals)


class BTree(object):
  """A BTree implementation with search and insert functions. Capable of any order t."""

  class Node(object):
    """Nó simples da arvore B."""

    def search(self, value, node=None):
    """Retorna verdade se a ArvoreB contem os valores."""
    if node is None:
      node = self.root
    if value in node.keys:
      return True
    elif node.leaf:
      # Condição de chegar na ponta do nó.
      return False
    else:
      i = 0
      while i < node.size and value > node.keys[i]:
        i += 1
      return self.search(value, node.children[i])

  def print_order(self):
    """Print an level-order representation."""
    this_level = [self.root]
    while this_level:
      next_level = []
      output = ""
      for node in this_level:
        if node.children:
          next_level.extend(node.children)
        output += str(node.keys) + " "
      print(output)
      this_level = next_level
 


    def split(self, parent, payload):
      """Dividir a arvore e passar os nós  """
      new_node = self.__class__(self._t)

      mid_point = self.size//2
      split_value = self.keys[mid_point]
      parent.add_key(split_value)

      # Add chaves nos nós
      new_node.children = self.children[mid_point + 1:]
      self.children = self.children[:mid_point + 1]
      new_node.keys = self.keys[mid_point+1:]
      self.keys = self.keys[:mid_point]

      #  new_node filho, setando o no interno
      if len(new_node.children) > 0:
        new_node.leaf = False

      parent.children = parent.add_child(new_node)
      if payload < split_value:
        return self
      else:
        return new_node

    @property
    def _is_full(self):
      return self.size == 2 * self._t - 1

    @property
    def size(self):
      return len(self.keys)
    
      def __init__(self, t):
      self.keys = []
      self.children = []
      self.leaf = True
      # t é a ordem que define o tamanho da arvore.
      self._t = t

    def add_key(self, value):
      """Add uma chave para o nó."""
      self.keys.append(value)
      self.keys.sort()

    def add_child(self, new_node):
      """
      Adicionando ligação ao nó.

      returns: a lista dos nós
      """
      i = len(self.children) - 1
      while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
        i -= 1
      return self.children[:i + 1]+ [new_node] + self.children[i + 1:]


  def __init__(self, t):
    """
    Criando a årvoreB. T é a ordem da arvore. ela n tem chaves crianda ainda. A implementaão duplica as chaves e é checada simultaneamente.
    """
    self._t = t
    if self._t <= 1:
      raise ValueError("ArvoreB Deve ser de grau 2 ou maior.")
    self.root = self.Node(t)

  def insert(self, payload):
    """Insira uma nova chave e valor para ArvoreB."""
    node = self.root
    # Raiz cria a referencia para outros dois nos.
    if node._is_full:
      new_root = self.Node(self._t)
      new_root.children.append(self.root)
      new_root.leaf = False
      # node is being set to the node containing the ranges we want for payload insertion.
      node = node.split(new_root, payload)
      self.root = new_root
    while not node.leaf:
      i = node.size - 1
      while i > 0 and payload < node.keys[i] :
        i -= 1
      if payload > node.keys[i]:
        i += 1

      next = node.children[i]
      if next._is_full:
        node = next.split(node, payload)
      else:
        node = next
    # Quando divide os nos para baixo e insere formando a folha.
    node.add_key(payload)

    def add_child(self, new_node):
      """
      Adicionando ligação ao nó.

      returns: a lista dos nós
      """
      i = len(self.children) - 1
      while i >= 0 and self.children[i].keys[0] > new_node.keys[0]:
        i -= 1
      return self.children[:i + 1]+ [new_node] + self.children[i + 1:]

    
  def search(self, value, node=None):
    """Retorna verdade se a ArvoreB contem os valores."""
    if node is None:
      node = self.root
    if value in node.keys:
      return True
    elif node.leaf:
      # Condição de chegar na ponta do nó.
      return False
    else:
      i = 0
      while i < node.size and value > node.keys[i]:
        i += 1
      return self.search(value, node.children[i])

  def print_order(self):
    """Print an level-order representation."""
    this_level = [self.root]
    while this_level:
      next_level = []
      output = ""
      for node in this_level:
        if node.children:
          next_level.extend(node.children)
        output += str(node.keys) + " "
      print(output)
      this_level = next_level
