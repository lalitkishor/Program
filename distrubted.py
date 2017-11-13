def ret(each,database):
    ans = []
    for x in database:
        if x != each:
            ans += database[x]
    return sorted(ans)

def distributed(uid,qcPeople):
    database = {}
    medium = {}
    qc = {}
    for i,e in enumerate(uid):
        qc[i] = ''
    for req,name in enumerate(uid):
        if name not in database:
            database[name] = [req]
        else:
            database[name].append(req)
    for each in qcPeople:
        medium[each]=ret(each,database)
    for _ in range(len(uid)):
        for e in medium:
                for y in medium[e]:
                    if qc[y]== '':
                        qc[y] = e
                        medium[e].remove(y)
                        break
    return qc
                
print(distributed(['A','B','A','A','B','A'],['B','A']))
