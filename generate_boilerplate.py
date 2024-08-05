import os
import sys


def create_directory_structure(project_name):
    # Structure
    structure = [
        f"{project_name}/src",
        f"{project_name}/db",
        f"{project_name}/models",
        f"{project_name}/config",
        f"{project_name}/routes",
    ]

    # Directories creation
    for directory in structure:
        os.makedirs(directory, exist_ok=True)
        print(f"Created: {directory}")

    # app.py file creation
    app_file = os.path.join(project_name, 'app.py')
    with open(app_file, 'w') as f:
        f.write("# Entry point for the application\n")
        f.write("from src import app\n\n")
        f.write("if __name__ == '__main__':\n")
        f.write("    app.run()\n")

    print(f"Created: {app_file}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_boilerplate.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    create_directory_structure(project_name)
    print(f"Project {project_name} structure created successfully!")


if __name__ == "__main__":
    main()
