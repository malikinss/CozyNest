import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import UserRoles, Genders, UserSettings, UserInfos, Users
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL", "*")

# Initialize the database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def add_test_users():
    try:
        # Add test data to UserRoles
        user_role_admin = UserRoles(role="Admin", description="Administrator role")
        user_role_owner = UserRoles(role="Owner", description="Owner of the property role")
        user_role_user = UserRoles(role="User", description="Regular user role")
        session.add(user_role_admin)
        session.add(user_role_owner)
        session.add(user_role_user)
        session.commit() # Commit to generate IDs
        logging.info("Test data added to UserRoles")
                     
        # Add test data to Genders
        gender_male = Genders(gender="Male", description="Male gender")
        gender_female = Genders(gender="Female", description="Female gender")
        session.add(gender_male)
        session.add(gender_female)
        session.commit() # Commit to generate IDs
        logging.info("Test data added to Genders")
        
        # Add test data to UserSettings
        user_setting_usd_eng = UserSettings(currency="USD", language="ENG")
        user_setting_eur_ru = UserSettings(currency="EUR", language="RU")
        session.add(user_setting_usd_eng)
        session.add(user_setting_eur_ru)
        session.commit() # Commit to generate IDs
        logging.info("Test data added to UserSettings")

        # Add test data to UserInfos
        user_info_john = UserInfos(gender_id=gender_male.id,
                                   user_settings_id=user_setting_usd_eng.id,
                                   first_name="John", last_name="Smith",
                                   birthdate="1980-01-20")
        user_info_jane = UserInfos(gender_id=gender_female.id,
                                   user_settings_id=user_setting_usd_eng.id,
                                   first_name="Sarah", last_name="Connor",
                                   birthdate="1970-01-30")
        user_info_user = UserInfos(gender_id=gender_male.id,
                                   user_settings_id=user_setting_usd_eng.id,
                                   first_name="Donald", last_name="Trump",
                                   birthdate="1960-01-22")
        session.add(user_info_john)
        session.add(user_info_jane)
        session.add(user_info_user)
        session.commit() # Commit to generate IDs
        logging.info("Test data added to UserInfos")

        # Add test data to Users
        user_john = Users(role_id=user_role_admin.id,
                          info_id=user_info_john.id,
                          email="john@ma.il",
                          password="qweQWE1!",
                          phone="123-456-7890")
        user_jane = Users(role_id=user_role_owner.id,
                          info_id=user_info_jane.id,
                          email="sarah@ma.il",
                          password="qweQWE1!",
                          phone="098-765-4321")
        user_user = Users(role_id=user_role_user.id,
                          info_id=user_info_user.id,
                          email="donaldh@ma.il",
                          password="qweQWE1!",
                          phone="123-777-5555")
        session.add(user_john)
        session.add(user_jane)
        session.add(user_user)
        logging.info("Test data added to Users")

        # Commit the session to save changes
        session.commit()
        print("Test data added successfully")
    except Exception as e:
        session.rollback()
        print(f"Failed to add test data: {str(e)}")
    finally:
        session.close()
if __name__ == "__main__":
    add_test_users()
