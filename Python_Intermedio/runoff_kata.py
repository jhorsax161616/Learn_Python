def runoff(voters):
    votes = len(voters)
    
    count = {}
    
    for i in voters[0]:
        count[i] = 0
    while True:
        for i in range(votes):
            count[voters[i][0]] += 1
        
        max = 0
        min = votes
        eliminate = []
        for w in count:
            if count[w] > (votes/2):
                return w
            if min > count[w]:
                min = count[w]
            if max < count[w]:
                max = count[w]
        
        if min == max:
            return None
        
        for i in count:
            if count[i] == min:
                eliminate.append(i)
        for i in eliminate:
            del count[i]
            
            for x in voters:
                x.remove(i)
#arreglar 
prueba1 = [['Drake Luft', 'Gihren Zabi', 'Frank Underwood', 'Brian J. Mason', 'Johan Liebert'], ['Johan Liebert', 'Brian J. Mason', 'Drake Luft', 'Frank Underwood', 'Gihren Zabi'], ['Gihren Zabi', 'Frank Underwood', 'Johan Liebert', 'Drake Luft', 'Brian J. Mason'], ['Frank Underwood', 'Drake Luft', 'Johan Liebert', 'Gihren Zabi', 'Brian J. Mason']]
prueba2 = [['Gihren Zabi', 'Frank Underwood', 'Brian J. Mason', 'Drake Luft', 'Reinhard von Musel'], 
['Drake Luft', 'Reinhard von Musel', 'Brian J. Mason', 'Frank Underwood', 'Gihren Zabi'], 
['Brian J. Mason', 'Reinhard von Musel', 'Frank Underwood', 'Gihren Zabi', 'Drake Luft']]
prueba3 = [['Drake Luft', 'Lex Luthor', 'Abelt Dessler', 'Brian J. Mason', 'Daisuke Aramaki'], ['Daisuke Aramaki', 'Lex Luthor', 'Brian J. Mason', 'Drake Luft', 'Abelt Dessler'], ['Lex Luthor', 'Brian J. Mason', 'Daisuke Aramaki', 'Abelt Dessler', 'Drake Luft']]

print(runoff(prueba1))
print(runoff(prueba2))
print(runoff(prueba3))