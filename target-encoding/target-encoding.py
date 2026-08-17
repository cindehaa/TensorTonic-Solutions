from collections import defaultdict

def target_encoding(categories, targets):
    """
    Replace each category with the mean target value for that category.
    """
    # Write code here

    d = defaultdict(list)
    
    for i, category in enumerate(categories):
        d[category].append(targets[i])
    
    for k, v in d.items():
        d[k] = sum(v)/len(v)

    means = []
    
    for i, category in enumerate(categories):
        means.append(d[category])
        
    return means