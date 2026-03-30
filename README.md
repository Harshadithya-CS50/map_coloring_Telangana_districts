#  Telangana District Map Coloring using CSP

This project implements the **Map Coloring Problem** for the **33 districts of Telangana** using a **Constraint Satisfaction Problem (CSP)** approach with a **backtracking algorithm** and graph-based visualization.

---

##  Problem Description

The objective is to assign colors to each district of Telangana such that:

* Each district is assigned one color
* No two adjacent districts share the same color

This is a classic example of a **Constraint Satisfaction Problem (CSP)**.

---

##  Approach

The problem is modeled as a CSP with:

* **Variables:** 33 districts of Telangana
* **Domains:** {Red, Green, Blue, Yellow}
* **Constraints:** Neighboring districts must have different colors

A **backtracking search algorithm** is used to find a valid assignment.

---

##  Districts Covered

```id="y9m0r3"
Adilabad, Bhadradri, Hyderabad, Jagtial, Jangaon, Jayashankar,
Jogulamba, Kamareddy, Karimnagar, Khammam, Komaram Bheem,
Mahabubabad, Mahabubnagar, Mancherial, Medak, Medchal,
Mulugu, Nagarkurnool, Nalgonda, Narayanpet, Nirmal,
Nizamabad, Peddapalli, Rajanna, Rangareddy, Sangareddy,
Siddipet, Suryapet, Vikarabad, Wanaparthy, Warangal Rural,
Warangal Urban, Yadadri
```

---

##  Constraints (Adjacency)

* Each district has a list of neighboring districts
* Colors must differ between connected nodes

>  Note: The adjacency relationships used in this project are **simplified approximations** and may not perfectly match real geographic boundaries.

---

##  Features

*  CSP-based solution using backtracking
*  Handles 33 variables (districts)
*  Graph visualization using NetworkX and Matplotlib
*  Clean and scalable implementation
*  Uses 4 colors to ensure feasibility

---

##  Example Output

```id="pq1zdx"
Solution:
Adilabad -> Red
Komaram Bheem -> Green
Mancherial -> Blue
...
```

A graph visualization window will open showing the colored districts.

---

##  Visualization

* Districts are represented as nodes
* Borders between districts are edges
* Colors represent assigned values
* Layout is generated using a force-directed graph (`spring_layout`)

---

---

##  Limitations

* Adjacency is approximate, not GIS-accurate
* Visualization is graph-based, not a real map overlay
* Multiple valid solutions may exist

---

##  Concepts Used

* Constraint Satisfaction Problems (CSP)
* Backtracking Search
* Graph Theory
* Data Visualization

source and available under the MIT License.
