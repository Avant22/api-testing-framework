from locust import HttpUser, task, between

class UsersApiUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_users(self):
        self.client.get("/users")

    @task
    def get_user_not_found(self):
        self.client.get("/users/9999")
