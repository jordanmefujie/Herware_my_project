#!/usr/bin/python3

"""
Module: model_manager.py
Description: This module contains the ModelManager class responsible for managing various models and their interactions.
"""

from .user import User
from .data import Data
from .device import Device
from .session import Session
from .settings import Settings
from .insight import Insight
from .prediction import Prediction
from .activity import Activity
from .goal import Goal
from .notification import Notification

# Create your models here.
# Exception classes


class ModelException(Exception):
    """Base exception class for model-related exceptions."""
    pass


class InvalidModelData(ModelException):
    """Exception raised when model data is invalid."""
    pass


class ModelNotFound(ModelException):
    """Exception raised when a model is not found."""
    pass


class ModelManager:
    """
    Class responsible for managing various models.

    Attributes:
    - users (list): List of User objects.
    - devices (list): List of Device objects.
    - data_points (list): List of Data objects.
    - sessions (list): List of Session objects.
    - settings (list): List of Settings objects.
    - insights (list): List of Insight objects.
    - predictions (list): List of Prediction objects.
    - activities (list): List of Activity objects.
    - goals (list): List of Goal objects.
    - notifications (list): List of Notification objects.
    """

    def __init__(self):
        """Initialize ModelManager with empty lists for each model."""
        self.users = []
        self.devices = []
        self.data_points = []
        self.sessions = []
        self.settings = []
        self.insights = []
        self.predictions = []
        self.activities = []
        self.goals = []
        self.notifications = []

    # Methods for adding models to the respective lists
    def add_user(self, user: User):
        """Add a User object to the users list."""
        self.users.append(user)

    def add_device(self, device: Device):
        """Add a Device object to the devices list."""
        self.devices.append(device)

    def add_data_point(self, data_point: Data):
        """Add a Data object to the data_points list."""
        self.data_points.append(data_point)

    def add_session(self, session: Session):
        """Add a Session object to the sessions list."""
        self.sessions.append(session)

    def add_setting(self, setting: Settings):
        """Add a Settings object to the settings list."""
        self.settings.append(setting)

    def add_insight(self, insight: Insight):
        """Add an Insight object to the insights list."""
        self.insights.append(insight)

    def add_prediction(self, prediction: Prediction):
        """Add a Prediction object to the predictions list."""
        self.predictions.append(prediction)

    def add_activity(self, activity: Activity):
        """Add an Activity object to the activities list."""
        self.activities.append(activity)

    def add_goal(self, goal: Goal):
        """Add a Goal object to the goals list."""
        self.goals.append(goal)

    def add_notification(self, notification: Notification):
        """Add a Notification object to the notifications list."""
        self.notifications.append(notification)

    # Methods for retrieving models from the lists
    def get_user(self, user_id: str):
        """
        Retrieve a User object by user ID.

        Args:
        - user_id (str): ID of the user to retrieve.

        Returns:
        - User: The User object corresponding to the provided ID.

        Raises:
        - ModelNotFound: If no User object with the given ID is found.
        """
        for user in self.users:
            if user.id == user_id:
                return user
        raise ModelNotFound(f'User with id {user_id} not found')

    def get_device(self, device_id: str):
        """
        Retrieve a Device object by device ID.

        Args:
        - device_id (str): ID of the device to retrieve.

        Returns:
        - Device: The Device object corresponding to the provided ID.

        Raises:
        - ModelNotFound: If no Device object with the given ID is found.
        """
        for device in self.devices:
            if device.id == device_id:
                return device
        raise ModelNotFound(f'Device with id {device_id} not found')
