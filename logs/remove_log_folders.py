import os
import shutil

# Function to remove folder
def remove_folder(folder_path: str) -> None:
    """
    Function to remove a folder and all its contents.

    Args:
        folder_path (str): Path to the folder to be removed.

    Returns:
        None
    """
    try:
        # Remove the folder and all its contents
        shutil.rmtree(folder_path)
        print(f"🗑️  - Removed folder {folder_path}")
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"❌ Error removing folder {folder_path}: {e}")


# Define the root log directory
log_root_dir: str = 'logs'

# Remove the 'info' directory
info_log_dir = os.path.join(log_root_dir, 'info')
remove_folder(info_log_dir)

# Remove the 'error' directory
error_log_dir = os.path.join(log_root_dir, 'error')
remove_folder(error_log_dir)

# Remove the 'debug' directory
debug_log_dir = os.path.join(log_root_dir, 'debug')
remove_folder(debug_log_dir)

# Remove the 'warning' directory
warning_log_dir = os.path.join(log_root_dir, 'warning')
remove_folder(warning_log_dir)
