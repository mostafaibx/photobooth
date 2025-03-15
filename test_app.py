#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test script to run the photo booth application.
"""

import sys
import os
import logging
from PyQt5.QtWidgets import QApplication

# Set environment variable to skip camera authorization
os.environ["OPENCV_AVFOUNDATION_SKIP_AUTH"] = "1"

from photobooth.controllers.app_controller import AppController
from photobooth.utils.config import Config
from photobooth.ui.main_window import MainWindow

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('photobooth.log')
        ]
    )

def main():
    """Main function to run the application."""
    # Set up logging
    setup_logging()
    
    # Create logger
    logger = logging.getLogger(__name__)
    logger.info("Starting Photo Booth application")
    
    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Photo Booth")
    app.setApplicationVersion("1.0.0")
    
    # Create config
    config = Config()
    
    # Create controller
    controller = AppController(config)
    
    # Initialize and show the main window
    main_window = MainWindow(controller)
    main_window.show()
    
    # Start the application
    controller.start_application()
    
    # Run application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main() 