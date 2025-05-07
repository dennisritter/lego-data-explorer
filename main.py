from app.utils.test_db_connection import test_db


def main():
    # Test database connection
    if not test_db():
        print("ERROR: Could not connect to the database.")
        exit(1)


if __name__ == "__main__":
    main()
