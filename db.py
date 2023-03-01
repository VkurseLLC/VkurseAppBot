from config import *

 
def create_connection():
    connection = None

    try:
        connection = mysql.connector.connect(
            host = '80.78.240.205',
            port = 13306,
            user = 'vkurse_editor', 
            password = 'T6XBwtgQ',
            database = 'vkurse_db')

        print("Подключение к базе данных MySQL прошло успешно")
        return connection

    except Error as e:
        print(f"Произошла ошибка в create_connection'{e}'")
        # bot.send_message(chat_id, f"Произошла ошибка в create_connection'{e}'")
        return connection


def save_auth_dates(connection, phome_number_value, verification_code_value):
    with connection.cursor() as cursor:
        try:
            phome_number_value  = (hashlib.sha256(repr(phome_number_value).encode())).hexdigest()
            verification_code_value  = (hashlib.sha256(repr(verification_code_value).encode())).hexdigest()

            cursor.executemany("INSERT INTO phone_number_verification_codes (id, phone_number, verification_code, dt_create) VALUES (NULL, %s, %s, NOW())", [(str(phome_number_value), str(verification_code_value))])
            connection.commit()
            return 'successful'
        
        except Error as e:
            print(f"Произошла ошибка сheck_user_block'{e}'")
            # bot.send_message(chat_id, f"Произошла ошибка в save_phone_number\n\n{e}")
            return 'error'