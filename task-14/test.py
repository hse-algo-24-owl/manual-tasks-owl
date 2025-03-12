from gurobi_optimods.min_cost_flow import min_cost_flow_scipy

# Assuming you have the cost and capacity matrices
cost_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
capacity_matrix = [[10, 5, 8], [2, 12, 7], [6, 4, 11]]

# Define the demands matrix. It's a vector with the same length as the number of vertices.
# For example, if you have 3 vertices, the demands matrix will look like this: [[10], [0], [0]]
demands = [10, 0, 0]

# Call the function to find the minimum cost flow
obj, sol = min_cost_flow_scipy(cost_matrix, capacity_matrix, demands, verbose=False)

# The solution (sol) will contain the flow values for each edge.
# To find the minimum length, you can calculate the sum of the flow values multiplied by their corresponding costs.
min_length = sum(cost_matrix[i][j] * sol[i][j] for i in range(len(cost_matrix)) for j in range(len(cost_matrix[0])) if sol[i][j] > 0)

print("Минимальная длина:", min_length)