# Flutter Starter Kit

Flutter Starter Kit is a comprehensive starting point for developing Flutter applications, providing essential features and a structured project setup to accelerate the development process.

## Overview

Flutter Starter Kit includes:

- Firebase Authentication: Seamlessly integrate Firebase Authentication for secure user sign-up, log-in, and password reset.
- Rive Animations: Engage users with captivating animations powered by Rive.
- Structured Project Setup: Maintain code cleanliness and scalability with an organized directory structure.
- Authentication Screens: Pre-built screens for sign-up, login, and password reset, complete with validation and error handling.
- Homepage with Bottom App Bar: Intuitive design for easy navigation between app sections.
- Tutorial Feature: Onboarding tutorial to guide users through app features and functionalities.

## Project Structure

flutter_starter_kit/
|-- android/
|-- build/
|-- ios/
|-- lib/
|   |-- animations/
|   |   |-- startup_animation.riv
|   |-- models/
|   |-- screens/
|   |   |-- auth/
|   |   |   |-- forgot_password_screen.dart
|   |   |   |-- login_screen.dart
|   |   |   |-- signup_screen.dart
|   |   |-- home/
|   |   |   |-- home_screen.dart
|   |-- services/
|   |   |-- authentication_service.dart
|   |-- utils/
|   |   |-- constants.dart
|   |-- widgets/
|   |   |-- tutorial_widget.dart
|-- test/
|-- pubspec.yaml
|-- README.md

## Getting Started

### Clone the repository

git clone <repository_url>

### Navigate to the project directory

cd flutter_starter_kit

### Install dependencies

flutter pub get

### Run the app

flutter run

## Usage

Customize authentication screens and functionality to match your app's requirements. Modify Rive animations or add new ones to create unique and engaging user experiences. Extend the app's features by adding new screens and functionalities within the organized directory structure. Refer to the README.md file for detailed instructions on project setup and customization.

## Contribution

Contributions to Flutter Starter Kit are welcome! Whether it's bug fixes, feature enhancements, or documentation improvements, feel free to contribute by submitting pull requests.

## License

This project is licensed under the MIT License.
