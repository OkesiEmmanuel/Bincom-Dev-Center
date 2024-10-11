import psycopg2

def save_colors_to_db(color_counter):
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname="", #i don't have postgresql installed on my pc. but this is where database name goes.
            user="", #authorization credential username to access the database 
            password="", #authorization credential password to access the database 
            host="localhost" #run local postgreSQL on local machine
        )
        cursor = conn.cursor()

        # Create table if not exists
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS color_frequencies (
                color VARCHAR(50) PRIMARY KEY,
                frequency INT
            )
        ''')

        # Insert color frequencies
        for color, freq in color_counter.items():
            cursor.execute(
                "INSERT INTO color_frequencies (color, frequency) VALUES (%s, %s) ON CONFLICT (color) DO UPDATE SET frequency = EXCLUDED.frequency",
                (color, freq)
            )

        conn.commit()
        cursor.close()
        conn.close()
        print("Colors saved to PostgreSQL database successfully.")

    except Exception as e:
        print("Error:", e)
