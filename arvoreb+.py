class noh(object): ##criação do nó da avore
    def __init__(self, folha=False):
        self.folha = folha ##olha do nó
        self.chave = []  ##lista de chaves internas
        self.c    = []    ## lista de nós filhos
        
    def __str__(self):
        if self.leaf:
            return "Leaf BTreeNode with {0} keys\n\tK:{1}\n\tC:{2}\n".format(len(self.keys), self.keys, self.c)                                         #formatação de print
        else:
            return "Internal BTreeNode with {0} keys, {1} children\n\tK:{2}\n\n".format(len(self.keys), len(self.c), self.keys, self.c)   #formatação de print


class ArvoreB(object):
    def __init__(self, t):
        self.raiz = noh(folha=True)
        self.t    = t
    
    def procura(self, k, x=None):
      #Procure na Árvore B para a chave k.
    
       #k: chave para procurar
       #x: (opcional) Nó para iniciar a pesquisa. Pode ser Nenhum, caso em que toda a árvore é pesquisada.
        
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.chave) and k > x.chave[i]:    #ver se o k esta dentro
                i += 1
            if i < len(x.chave) and k == x.chave[i]:       # found exact match
                return (x, i)
            elif x.folha:                                # no match in keys, and is leaf ==> no match exists
                return None
            else:                                       # search children
                return self.procura(k, x.c[i])
        else:                                           # no node provided, search root of tree
            return self.procura(k, self.raiz)
        
    def inserir(self, k):
        r = self.raiz
        if len(r.chave) == (2*self.t) - 1:     # keys are full, so we must split
            s = noh()
            self.raiz = s
            s.c.inserir(0, r)                  # former root is now 0th child of new root s
            self.dividirfilhos(s, 0)            
            self.inserirnaocheio(s, k)
        else:
            self.inserirnaocheio(r, k)
    
    def inserirnaocheio(self, x, k): 
        i = len(x.chave) - 1
        if x.folha:
            #inserir a chave
            x.chave.append(0)
            while i >= 0 and k < x.chave[i]:
                x.chave[i+1] = x.chave[i]
                i -= 1
            x.chave[i+1] = k
        else:
            # inserir filha
            while i >= 0 and k < x.chave[i]:
                i -= 1
            i += 1
            if len(x.c[i].chave) == (2*self.t) - 1:
                self.dividirfilhos(x, i)
                if k > x.chave[i]:
                    i += 1
            self.inserirnaocheio(x.c[i], k)
        
    def dividirfilhos(self, x, i):
        t = self.t
        y = x.c[i]
        z = noh(folha=y.folha)
        
        # slide all children of x to the right and insert z at i+1.
        x.c.inserir(i+1, z)
        x.chave.inserir(i, y.chave[t-1])
        
        # keys of z are t to 2t - 1,
        # y is then 0 to t-2
        z.chave = y.chave[t:(2*t - 1)]
        y.chave = y.chave[0:(t-1)]
        
        # children of z are t to 2t els of y.c
        if not y.chave:
            z.c = y.c[t:(2*t)]
            y.c = y.c[0:(t-1)]    
        
    def __str__(self):
        r = self.raiz
        return r.__str__() + '\n'.join([child.__str__() for child in r.c])  