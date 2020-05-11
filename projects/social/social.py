import random
from util import Queue

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def get_friends(self, user_id):
        return self.friendships[user_id]

    def populate_graph(self, num_users, avg_friendships):
        
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(num_users):
            self.add_user(i)

        friendship_count = 0
        while friendship_count < num_users*avg_friendships:
            user_id = random.randint(1, num_users)
            friend_id = random.randint(1, num_users)
            if user_id != friend_id and friend_id not in self.friendships[user_id]:
                self.add_friendship(user_id, friend_id)
                friendship_count += 2

    def get_all_social_paths(self, user_id):
        visited = {user_id: [user_id]}  
        queue = Queue()
        queue.enqueue(user_id)

        while queue.size() > 0:
            u = queue.dequeue()
            for v in self.get_friends(u):
                if v not in visited:
                    visited[v] = visited[u] + [v]
                    queue.enqueue(v)

        return visited

    def get_avg_deg_sep(self, user_id):
        total = 0
        connections = self.get_all_social_paths(user_id).values()
        for path in connections:
            total += len(path)
        return total / len(connections)


if __name__ == '__main__':
    sg = SocialGraph()
    num_users = 10
    sg.populate_graph(num_users, 2)
    print('\n')
    print(sg.friendships)
    print('\n')
    connections = sg.get_all_social_paths(1)
    print(connections)
    # print(len(connections.keys()) / num_users)
    # print(sg.get_avg_deg_sep(1))
    print('\n')

