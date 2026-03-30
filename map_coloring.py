import networkx as nx
import matplotlib.pyplot as plt

districts = [
    'Adilabad','Bhadradri','Hyderabad','Jagtial','Jangaon','Jayashankar',
    'Jogulamba','Kamareddy','Karimnagar','Khammam','Komaram Bheem',
    'Mahabubabad','Mahabubnagar','Mancherial','Medak','Medchal',
    'Mulugu','Nagarkurnool','Nalgonda','Narayanpet','Nirmal',
    'Nizamabad','Peddapalli','Rajanna','Rangareddy','Sangareddy',
    'Siddipet','Suryapet','Vikarabad','Wanaparthy','Warangal Rural',
    'Warangal Urban','Yadadri'
]

colors = ['Red', 'Green', 'Blue', 'Yellow']

neighbors = {
    'Adilabad': ['Komaram Bheem','Nirmal'],
    'Komaram Bheem': ['Adilabad','Mancherial'],
    'Mancherial': ['Komaram Bheem','Peddapalli','Jagtial'],
    'Nirmal': ['Adilabad','Nizamabad'],
    'Nizamabad': ['Nirmal','Kamareddy'],
    'Kamareddy': ['Nizamabad','Medak','Rajanna'],
    'Medak': ['Kamareddy','Sangareddy','Siddipet'],
    'Sangareddy': ['Medak','Vikarabad','Medchal'],
    'Vikarabad': ['Sangareddy','Rangareddy'],
    'Medchal': ['Sangareddy','Hyderabad','Rangareddy'],
    'Hyderabad': ['Medchal','Rangareddy'],
    'Rangareddy': ['Hyderabad','Medchal','Vikarabad','Mahabubnagar'],
    'Mahabubnagar': ['Rangareddy','Narayanpet','Wanaparthy'],
    'Narayanpet': ['Mahabubnagar','Jogulamba'],
    'Jogulamba': ['Narayanpet','Wanaparthy'],
    'Wanaparthy': ['Jogulamba','Nagarkurnool'],
    'Nagarkurnool': ['Wanaparthy','Nalgonda'],
    'Nalgonda': ['Nagarkurnool','Suryapet','Yadadri'],
    'Suryapet': ['Nalgonda','Khammam'],
    'Khammam': ['Suryapet','Bhadradri'],
    'Bhadradri': ['Khammam','Mulugu'],
    'Mulugu': ['Bhadradri','Jayashankar'],
    'Jayashankar': ['Mulugu','Warangal Rural'],
    'Warangal Rural': ['Jayashankar','Warangal Urban'],
    'Warangal Urban': ['Warangal Rural','Jangaon'],
    'Jangaon': ['Warangal Urban','Yadadri','Siddipet'],
    'Yadadri': ['Jangaon','Nalgonda'],
    'Siddipet': ['Medak','Jangaon','Karimnagar'],
    'Karimnagar': ['Siddipet','Rajanna','Peddapalli'],
    'Rajanna': ['Karimnagar','Kamareddy'],
    'Peddapalli': ['Karimnagar','Mancherial'],
    'Jagtial': ['Mancherial','Karimnagar']
}

def is_valid(region, color, assignment):
    for neighbor in neighbors.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(districts):
        return assignment

    unassigned = [r for r in districts if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color
            result = backtrack(assignment)
            if result:
                return result
            del assignment[region]

    return None

solution = backtrack({})

print("Solution:")
for d in districts:
    print(d, "->", solution[d])

def visualize(solution):
    G = nx.Graph()

    for d in districts:
        G.add_node(d)

    for d in neighbors:
        for n in neighbors[d]:
            G.add_edge(d, n)

    color_map = [solution[node].lower() for node in G.nodes()]

    pos = nx.spring_layout(G, seed=42)

    nx.draw(
        G, pos,
        with_labels=True,
        node_color=color_map,
        node_size=1200,
        font_size=7
    )

    plt.title("Telangana District Map Coloring (CSP)")
    plt.show()

visualize(solution)
