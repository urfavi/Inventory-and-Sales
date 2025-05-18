from models.user_model import get_user_by_username, update_user_password
import bcrypt

def authenticate_user(username, password):
    user = get_user_by_username(username)
    if user is None:
        return False

    try:
        stored_hash = user[1]  # Assuming the second column is the hashed password
        
        password_bytes = password.encode('utf-8')
        stored_hash_bytes = stored_hash.encode('utf-8') if isinstance(stored_hash, str) else stored_hash

        print(f"Comparing password for {username}")
        print(f"Input password: {password}")
        print(f"Stored hash: {stored_hash}")
        
        if bcrypt.checkpw(password_bytes, stored_hash_bytes):
            return True
        else:

            return False
    except Exception as e:
        print("[AUTH ERROR]:", e)
        return False

def check_username_exists(username):
    user = get_user_by_username(username)
    return user is not None

def forgot_password(username, new_password):
    user = get_user_by_username(username)
    if user is None:
        return False

    try:
        # Hash the new password
        hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        hashed_password_str = hashed_password.decode('utf-8')  # Convert to string for storage
        
        print(f"Updating password for user: {username}")
        print(f"New hashed password (string): {hashed_password_str}")
        
        if update_user_password(username, hashed_password_str):
            print("Password updated successfully.")
            return True
        else:
            print("Password update failed.")
            return False
    except Exception as e:
        print(f"ERROR: {e}")
        return False