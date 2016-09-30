from ford import *

fn = FlowNetwork()
fn.addVertex('s', True, False)
fn.addVertex('t', False, True)
map(fn.addVertex, ['a', 'b','c','d'])
fn.addEdge('s', 'a', 4)
fn.addEdge('a', 'b', 4)
fn.addEdge('b', 't', 2)
fn.addEdge('s', 'c', 3)
fn.addEdge('c', 'd', 6)
fn.addEdge('d', 't', 6)
fn.addEdge('b', 'c', 3)

print(fn.calculateMaxFlow())
