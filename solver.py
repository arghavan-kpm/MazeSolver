# depth-limited dfs
def dls_solver(maze, limit):
	par={};
	seen = {};
	depth = {};
	stack = [];
	stack.append(maze.start);
	depth[maze.start] = 0;
	while(len(stack) != 0):
		node = stack[len(stack)-1];
		flag = 0;
		for i in maze.get_neighbors(node) :
			if(((i not in seen) or (seen[i] != True) ) and depth[node] + 1 <= limit ):
				seen[i] = True;
				par[i] = node;
				depth[i] = depth[node] + 1;
				stack.append(i);
				flag = 1;
		if(flag == 0):
			stack.pop();

	path = [];
	tmp = maze.goal;
	if( tmp not in par):
		return [];
	path.append(tmp);
	while tmp != maze.start:
		tmp = par[tmp];
		path.append(tmp);

	path.append(tmp);
	path.reverse();
	return path;



def iterative_dfs_solver(maze):
	for l in range(0,maze.nrows*maze.ncols + 1):
		if(len(dls_solver(maze,l) ) != 0):
			return dls_solver(maze,l);


def dfs_solver(maze):
	par={};
	seen = {};
	stack = [];
	stack.append(maze.start);
	while(len(stack) != 0):
		node = stack[len(stack)-1];
		flag = 0;
		for i in maze.get_neighbors(node) :
			if((i not in seen) or (seen[i] != True) ):
				seen[i] = True;
				par[i] = node;
				stack.append(i);
				flag = 1;
		if(flag == 0):
			stack.pop();

	path = [];
	tmp = maze.goal;
	path.append(tmp);
	while tmp != maze.start:
		tmp = par[tmp];
		path.append(tmp);

	path.append(tmp);
	path.reverse();
	return path;


def bfs_solver(maze):
	par={};
	seen={};
	queue = [];
	queue.append(maze.start);
	while(len(queue) != 0):
		node = queue[0];
		for i in maze.get_neighbors(node) :
			if((i not in seen) or (seen[i] != True) ):
				seen[i] = True;
				par[i] = node;
				queue.append(i);
		queue.pop(0);
	
	path = [];
	tmp = maze.goal;
	path.append(tmp);
	while tmp != maze.start:
		tmp = par[tmp];
		path.append(tmp);

	path.append(tmp);
	path.reverse();
	return path;


def astar_heuristic(maze, cell):
	x = cell[0] - maze.goal[0];
	y = cell[1] - maze.goal[1];


	return x**2 + y**2;


def astar_solver(maze):
	
	g = {};
	seen = {};
	par = {};
	stack = [];

	g[maze.start] = 0;
	stack.append(maze.start);

	while(len(stack) != 0):
		node = stack[len(stack)-1];
		min_dist = 10000000;
		tmp_node = (-1,-1);
		flag = 0;
		for i in maze.get_neighbors(node) :
			f = g[node] + 1 + astar_heuristic(maze, i);
			if((i not in seen) or (seen[i] != True) and f < min_dist):
				min_dist = f;
				tmp_node = i;
				flag = 1;
		if(flag == 0):
			stack.pop();
		else:
			seen[tmp_node] = True;
			par[tmp_node] = node;
			g[tmp_node] = g[node] + 1;
			stack.append(tmp_node);
			
		

	path = [];
	tmp = maze.goal;
	path.append(tmp);
	while tmp != maze.start:
		tmp = par[tmp];
		path.append(tmp);

	path.append(tmp);
	path.reverse();
	return path;

