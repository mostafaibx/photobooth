# Photo Booth Application

A touchscreen-friendly photo booth application built with Python and PyQt5.

## Features

- Touchscreen-friendly interface
- Live camera feed
- Capture & save photos
- Multi-language support
- Printing support
- Future-ready for payments

## Application Flow

1. **Selection Screen**: User selects the number of images and layout
2. **Dummy Payment**: User "pays" (can be skipped in testing)
3. **Face Alignment Guide**: Helps position the user's face correctly
4. **Countdown & Photo Capture**: Starts a countdown and takes a photo
5. **Review & Print**: User sees the captured images and prints them

## Setup

1. Install Python 3.8 or higher
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python photobooth/main.py
   ```

## Architecture

- **Event-Driven Architecture**: Each step triggers the next using signals and state transitions
- **MVC Pattern**: Clear separation of UI, business logic, and data
- **Asynchronous Processing**: Camera operations, countdown, and printing run in separate threads
- **Language Support**: Uses Qt Linguist for multi-language text files
- **Future-Proofing for Payments**: Payment logic is in a separate module for easy integration

## Development

- UI components are in the `ui` directory
- Business logic is in the `controllers` directory
- Data models are in the `models` directory
- Utility functions are in the `utils` directory
- Resources (images, language files) are in the `resources` directory 