#!/usr/bin/python3

"""
"""

import time
import random

class Herware:
    """
    Base class representing a hardware device.

    This class defines basic functionality for a hardware device,
    including starting and stopping processes and retrieving status.
    """

    def __init__(self):
        """
        Initialize a Herware device.

        Attributes:
            name (str): The name of the hardware device.
            status (str): The current status of the hardware device.
        """
        self.name = "Herware Device"
        self.status = "Idle"

    def start_process(self, process_name):
        """
        Start a process on the hardware device.

        Args:
            process_name (str): The name of the process to start.

        Returns:
            str: A message indicating the completion of the process.
        """
        self.status = "Processing"
        time.sleep(random.randint(1, 5))  # Simulate processing time
        self.status = "Idle"
        return f"{process_name} completed"

    def stop_process(self):
        """
        Stop the current process on the hardware device.
        """
        self.status = "Idle"

    def get_status(self):
        """
        Get the current status of the hardware device.

        Returns:
            str: The current status of the hardware device.
        """
        return self.status


class EnhancedHerware(Herware):
    """
    Subclass of Herware with enhanced functionality.

    This class extends the functionality of the Herware class by
    adding a process log to track started and stopped processes.
    """

    def __init__(self):
        """
        Initialize an EnhancedHerware device.

        Attributes:
            process_log (list): A list to store process log entries.
        """
        super().__init__()
        self.process_log = []

    def start_process(self, process_name):
        """
        Start a process on the hardware device and log the process.

        Args:
            process_name (str): The name of the process to start.

        Returns:
            str: A message indicating the completion of the process.
        """
        self.process_log.append(f"{process_name} started")
        return super().start_process(process_name)

    def stop_process(self):
        """
        Stop the current process on the hardware and log the process.
        """
        self.process_log.append("Process stopped")
        return super().stop_process()

    def get_process_log(self):
        """
        Get the process log from the hardware device.

        Returns:
            list: The process log entries.
        """
        return self.process_log


class AdvancedHerware(EnhancedHerware):
    """
    Subclass of EnhancedHerware with additional advanced features.

    This class further extends the functionality of EnhancedHerware
    by adding settings for process timeout.
    """

    def __init__(self):
        """
        Initialize an AdvancedHerware device.

        Attributes:
            settings (dict): A dictionary to store device settings.
        """
        super().__init__()
        self.settings = {"process_timeout": 10}

    def start_process(self, process_name):
        """
        Start a process on the hardware device with timeout settings.

        Args:
            process_name (str): The name of the process to start.

        Returns:
            str: A message indicating the status of the process.
        """
        if self.status == "Processing" and time.time() < self.settings["process_timeout"]:
            return "Processing in progress, please wait"
        return super().start_process(process_name)
