import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def create_file(path, content=""):
    with open(path, "w") as file:
        file.write(content)

def create_flutter_project_structure():
    # Create main directories
    create_directory("lib")
    create_directory("lib/animations")
    create_directory("lib/models")
    create_directory("lib/screens")
    create_directory("lib/screens/auth")
    create_directory("lib/screens/home")
    create_directory("lib/services")
    create_directory("lib/utils")
    create_directory("lib/widgets")
    create_directory("test")

    # Create placeholder files
    create_file("lib/animations/.gitkeep")
    create_file("lib/models/.gitkeep")
    create_file("lib/screens/auth/.gitkeep")
    create_file("lib/screens/home/.gitkeep")
    create_file("lib/services/.gitkeep")
    create_file("lib/utils/.gitkeep")
    create_file("lib/widgets/.gitkeep")
    create_file("pubspec.yaml", "name: flutter_starter_kit\ndependencies:\n  flutter:\n    sdk: flutter\n")

    # Optional: Create README.md
    create_file("README.md", "# Flutter Starter Kit\n\nThis is a Flutter starter kit.\n")

if __name__ == "__main__":
    create_flutter_project_structure()
    print("Flutter project structure created successfully!")


