import PyInstaller.__main__
import os

def build_executable():
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the main script path
    main_script = os.path.join(current_dir, 'src', 'main.py')
    
    # PyInstaller options
    options = [
        main_script,
        '--name=HostelStudentEntries',
        '--onefile',
        '--windowed',
        '--clean',
        '--add-data=README.md;.',
        '--icon=NONE',  # You can add an icon file later
    ]
    
    # Run PyInstaller
    PyInstaller.__main__.run(options)

if __name__ == "__main__":
    build_executable() 