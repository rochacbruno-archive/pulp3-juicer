import os
import unittest
import juicer
from time import sleep
from uuid import uuid4
from juicer import (
    Repository,
    Task,
    FileRemote,
    RepositorySyncURL
)

TASK_COMPLETED = ['completed', 'failed', 'canceled']


class PulpTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create class-wide variables."""
        configuration = juicer.Configuration()
        configuration.host = "http://{0}".format(
            os.environ.get('PULP3_HOST', 'localhost')
        )
        cls.client = juicer.ApiClient(configuration)
        cls.api = juicer.PulpApi(cls.client)

    def await_task(self, task):
        while task.state not in TASK_COMPLETED:
            sleep(2)
            task = self.api.tasks_read(task.href)
        assert isinstance(task, Task)
        return task

    def test_positive_update_repo_description(self):
        # create Repo
        repo = self.api.repositories_create(Repository(name=uuid4().hex))

        # Update repo description to generate an async task
        async_response = self.api.repositories_update(
            repo.href,
            {'name': repo.name, 'description': 'This is a repo'}
        )

        # read the task
        task = self.await_task(self.api.tasks_read(async_response.task))

        # Assert task is completed
        self.assertIn(task.state, 'completed')

        # Read repo again
        repo = self.api.repositories_read(repo.href)

        # assert description is there
        self.assertEqual(repo.description, 'This is a repo')

    def test_positive_sync_repo(self):
        # create Repo
        repo = self.api.repositories_create(Repository(name=uuid4().hex))

        # Create a File Remote
        remote_url = (
            'https://repos.fedorapeople.org/pulp/pulp/demo_repos'
            '/test_file_repo/PULP_MANIFEST'
        )

        file_remote = self.api.remotes_file_file_create(
            FileRemote(name=uuid4().hex, url=remote_url)
        )

        # Sync
        async_response = self.api.remotes_file_file_sync(
            file_remote.href,
            RepositorySyncURL(repository=repo.href)
        )

        #read the task
        task = self.await_task(self.api.tasks_read(async_response.task))

        # Assert task is completed
        self.assertIn(task.state, 'completed')

        # Check version created
        repo_version_1 = self.api.repositories_versions_read(
            task.created_resources[0]
        )

        # Assert the version is the first
        self.assertEqual(repo_version_1.number, 1)

