def find_process(pids, ppids, kill):
    if len(pids) != len(ppids):
        return None

    pdicts = {}
    for i in range(len(pids)):
        if ppids[i] in pdicts:
            pdicts[ppids[i]].append(pids[i])
        else:
            pdicts[ppids[i]] = [pids[i]]

    q = [kill]
    result = []
    while q:
        p = q.pop()
        if pdicts.get(p):
            for child in pdicts.get(p):
                q.append(child)
        result.append(p)

    return result

pid = [1, 3, 10, 5, 12, 14]
ppid = [3, 0, 5, 3, 10, 5]
kill = 5
print find_process(pid, ppid, kill)

