import matplotlib.pyplot as plt

# Define the points
points = [(1, 1), (4, 1), (2.5, 4)]

# Plot the points
plt.figure(figsize=(6, 6))
plt.scatter(*zip(*points), marker='o', color='black', s=200)
plt.axis('off')
plt.savefig('../outputs/poster-diagrams/plot_of_three_points.pdf', dpi=300, bbox_inches='tight')

# Plot the points joined to make a triangle
plt.figure(figsize=(6, 6))
plt.scatter(*zip(*points), marker='o', color='black', s=200)
plt.plot(*zip(*points, points[0]), marker='o', color='black')
plt.axis('off')
plt.savefig('../outputs/poster-diagrams/plot_of_three_edges.pdf', dpi=300, bbox_inches='tight')

# Plot the filled triangle
plt.figure(figsize=(6, 6))
plt.scatter(*zip(*points), marker='o', color='black', s=200)
plt.fill(*zip(*points), color='orange', edgecolor='black')
plt.axis('off')
plt.savefig('../outputs/poster-diagrams/plot_of_triangle.pdf', dpi=300, bbox_inches='tight')

# Create a single plot with three subplots: points, triangle, and filled triangle
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Plot of three points
axs[0].scatter(*zip(*points), marker='o', color='blue', s=200)
axs[0].axis('off')

# Plot the points joined to make a triangle
axs[1].plot(*zip(*points, points[0]), color='red')
axs[1].scatter(*zip(*points), marker='o', color='blue', s=200)
axs[1].axis('off')

# Plot the filled triangle
axs[2].fill(*zip(*points), color='orange', alpha=0.75, edgecolor='red')
axs[2].scatter(*zip(*points), marker='o', color='blue', s=200)
axs[2].axis('off')

# Save the combined plot as a high dpi PDF
plt.savefig('../outputs/poster-diagrams/plot_of_simplices.pdf', dpi=300, bbox_inches='tight')
