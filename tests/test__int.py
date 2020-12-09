import unittest
from flask import url_for
from flask_testing import TestCase
from app import app
from application import models, routes

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test registree
        sample1 = Tasks(name="Testing Unit Testing")

        # save users to database
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

# Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
class TestViews(TestBase):

    def test_home_get(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_update_get(self):
        response = self.client.get(url_for('update'))
        self.assertEqual(response.status_code,405)

    def test_delete_get(self):
        response = self.client.get(url_for('delete'))
        self.assertEqual(response.status_code,405)

# Test adding 
class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data = dict(name="TestingUnittesting2")
        )
        self.assertIn(b'TestingUnittesting2',response.data)

# Test updating

class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(
            url_for('update'),
            data = dict(oldname="Testing Unit testing", newname="Not Testing Unit Testing"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)
# Test Deleting

class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(
            url_for('delete'),
            data = dict(name="MissWoman"),
            follow_redirects=True
            )
        self.assertEqual(response.status_code,200)