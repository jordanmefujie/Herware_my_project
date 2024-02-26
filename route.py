#!/usr/bin/python3

"""
Flask app for managing users and devices.

All modules and classes should be properly documented.
"""

from flask import Flask, render_template, request
from device import DeviceManager
from user import UserManager

app = Flask(__name__)

# Define routes for the Herware project

@app.route('/')
def index():
    """
    Renders the index.html template.
    """
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    """
    Creates a new user.
    """
    data = request.get_json()
    user_manager = UserManager(data['username'])
    return user_manager.create(data)

@app.route('/devices', methods=['POST'])
def create_device():
    """
    Creates a new device.
    """
    data = request.get_json()
    device_manager = DeviceManager(
        data['device_id'],
        data['name'],
        data['user_id'])
    return device_manager.create()

@app.route('/users/<string:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieves information about a specific user.
    """
    user_manager = UserManager(user_id)
    return user_manager.read(user_id)

@app.route('/devices/<string:device_id>', methods=['GET'])
def get_device(device_id):
    """
    Retrieves information about a specific device.
    """
    device_manager = DeviceManager(device_id)
    return device_manager.read(device_id)

@app.route('/users/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Updates information about a specific user.
    """
    data = request.get_json()
    user_manager = UserManager(user_id)
    return user_manager.update(user_id, data)

@app.route('/devices/<string:device_id>', methods=['PUT'])
def update_device(device_id):
    """
    Updates information about a specific device.
    """
    data = request.get_json()
    device_manager = DeviceManager(device_id)
    return device_manager.update(device_id, data)

@app.route('/users/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Deletes a specific user.
    """
    user_manager = UserManager(user_id)
    return user_manager.delete(user_id)

@app.route('/devices/<string:device_id>', methods=['DELETE'])
def delete_device(device_id):
    """
    Deletes a specific device.
    """
    device_manager = DeviceManager(device_id)
    return device_manager.delete(device_id)
