

def build_graph(words):
    indegree = {}
    for word in words:
        for c in word:
            indegree[c] = 0


    edges = {}
    for i in range(len(words)-1):
        f = words[i]
        s = words[i+1]
        for j in range(min(len(f), len(s))):
            if f[j] == s[j]:
                continue
            else:
                if f[j] in edges:
                    edges[f[j]].append(s[j])
                else:
                    edges[f[j]] = [s[j]]
                if s[j] in indegree:
                    indegree[s[j]] += 1
                else:
                    indegree[s[j]] = 1
                break

    return edges, indegree

def alien_order(dict):
    edges, indegree = build_graph(dict)
    stack = []
    result = ''

    for key, value in indegree.iteritems():
        if value == 0:
            stack.append(key)

    while stack:
        val = stack.pop()
        result += val
        if val in edges:
            for edge in edges[val]:
                indegree[edge] -= 1
                if indegree[edge] == 0:
                    stack.append(edge)

    return result


test = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
a, b = build_graph(test)
print a
print b

print alien_order(test)