from database import Database  # adjust if your path is different

def main():
    db = Database()
    db.connect()

    test_query = "SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"
    result = db.execute_query(test_query)

    if result:
        print("✅ Connected! Here are your tables:")
        for row in result:
            print(" -", row[0])
    else:
        print("❌ Connection succeeded, but no tables found or error running query.")

    db.close_connection()

if __name__ == "__main__":
    main()
