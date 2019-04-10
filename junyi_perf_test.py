from locust import HttpLocust, TaskSet, task

class UserPerfromTest(TaskSet):
    @task
    def get_all_user(self):
        self.client.get("/user")


class PerformRunner(HttpLocust):
    task_set = UserPerfromTest
    max_wait = 15000
    min_wait = 500
