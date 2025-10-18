import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

from app.db.database import engine, SessionLocal
from app.models.user import User, UserRole
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user():
    # Create a session
    db = SessionLocal()
    
    try:
        # Check if user already exists
        existing_user = db.query(User).filter(User.username == "testuser").first()
        if existing_user:
            print("User already exists")
        else:
            # Create a test user with hashed password
            hashed_password = pwd_context.hash("testpass")
            
            db_user = User(
                username="testuser",
                email="test@example.com",
                full_name="Test User",
                hashed_password=hashed_password,
                role=UserRole.USER
            )
            
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            print(f"Created user: {db_user.username}")
        
        # Check if admin user already exists
        existing_admin = db.query(User).filter(User.username == "admin").first()
        if existing_admin:
            print("Admin user already exists")
        else:
            # Create an admin user
            hashed_password = pwd_context.hash("admin")
            
            db_admin = User(
                username="admin",
                email="admin@example.com",
                full_name="Admin User",
                hashed_password=hashed_password,
                role=UserRole.ADMIN
            )
            
            db.add(db_admin)
            db.commit()
            db.refresh(db_admin)
            print(f"Created admin user: {db_admin.username}")
        
    except Exception as e:
        print(f"Error creating user: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_user()