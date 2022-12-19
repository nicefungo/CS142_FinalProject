from datetime import datetime
import networkx as nx

#-------------------------------------------------

def Test(begin_time, end_time, test_num = 100):


  ans = None
  return ans



#-------------------------------------------------

def time_gap(a, b):
    '''
        a and b are timestamp strings
        return the gap (sec)
    '''
    fmt = '%Y-%m-%d %H:%M:%S'
    tstamp1 = datetime.strptime(a, fmt)
    tstamp2 = datetime.strptime(b, fmt)
    return abs(tstamp1-tstamp2)


def estimation(G, nodeA, nodeB, e=7):
  '''
      G is the partial order relationship network,
      (nodeA, nodeB) is queried node pair,
      return True iff nodeA.price > nodeB.price,
      False otherwise

      Version1: think of a path from x to y 
      with length n contributing e**(-n) confidence
      to the fact that x.price>y.price
  '''
  if G.nodes[nodeA]==None or G.nodes[nodeB]==None:
    print("Nodes don't exist!!!!!!")

  A_score = 0
  B_score = 0

  paths = nx.all_simple_paths(G, source=nodeA, target=nodeB, cutoff=5)
  for p in paths:
    A_score += e**(-len(p))
  paths = nx.all_simple_paths(G, source=nodeB, target=nodeA, cutoff=5)
  for p in paths:
    B_score += e**(-len(p))
  
  return A_score>B_score


def price_from_reputation(G, rep_dic, trans):
  '''
       G is the trade participant network, 
       rep_dic is the reputation dictionaries [dic1, dic2],
       trans is the dic mapping all nodes to its transaction
       [node1, node2, ..., noden]
       return the rating dictionary for NFTs

       TODO: Currently only the first transaction and the 
       last is taken into consideration, maybe add the 
       intermediate ones with weight.
  '''
  dic1, dic2 = rep_dic

  ans = dict()
  for i in G.nodes:
    ans[i] = dic1[G.nodes[trans[i][0]]] + dic2[G.nodes[trans[i][-1]]]

  return ans

def data_by_time(df, time):
  '''
      return the data of transactions no later than `time`
      as a new dataFrame
  '''
  return None
  
