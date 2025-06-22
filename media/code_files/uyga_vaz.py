import sqlite3

print(
    '''
    Kichik to'lov tizimi!

    1 - Foydalanuvchi qo'shish
    2 - Pul qo'shish (deposit)
    3 - Pul yechish (withdraw)
    4 - Pul o'tkazish (transfer)
    5 - Foydalanuvchilarni ko'rish
    6 - Chiqish
    '''
)


# **Bazaga ulanish funksiyasi**
def open_db():
    global conn, cursor
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Agar USERS jadvali bo‘lmasa, yaratamiz
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USERS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ism TEXT NOT NULL,
            yosh INTEGER NOT NULL,
            karta TEXT NOT NULL UNIQUE,
            balance INTEGER DEFAULT 0
        )
    """)
    conn.commit()


# **Bazani yopish funksiyasi**
def close_db():
    conn.close()


# **Foydalanuvchi qo‘shish**
def add():
    open_db()

    name = input("Ismingizni kiriting: ")
    age = int(input("Yoshingizni kiriting: "))
    card = input("Kartangizni kiriting: ")
    balance = int(input("Balansingizni kiriting: "))

    try:
        cursor.execute("INSERT INTO USERS (ism, yosh, karta, balance) VALUES (?, ?, ?, ?)", (name, age, card, balance))
        conn.commit()
        print("✅ Foydalanuvchi qo‘shildi!")
    except sqlite3.IntegrityError:
        print("❌ Xatolik! Bu karta allaqachon mavjud.")

    close_db()


# **Pul qo‘shish (deposit)**
def deposit():
    open_db()

    user_id = int(input("User ID ni kiriting: "))
    amount = int(input("Qancha summa qo‘shmoqchisiz? "))

    cursor.execute("UPDATE USERS SET balance = balance + ? WHERE id = ?", (amount, user_id))
    conn.commit()

    print(f"✅ {amount} so‘m balansga qo‘shildi!")

    close_db()


# **Pul yechish (withdraw)**
def withdraw():
    open_db()

    user_id = int(input("User ID ni kiriting: "))
    amount = int(input("Qancha summa yechmoqchisiz? "))

    cursor.execute("SELECT balance FROM USERS WHERE id = ?", (user_id,))
    result = cursor.fetchone()

    if result and result[0] >= amount:
        cursor.execute("UPDATE USERS SET balance = balance - ? WHERE id = ?", (amount, user_id))
        conn.commit()
        print(f"✅ {amount} so‘m yechildi!")
    else:
        print("❌ Xatolik! Yetarli mablag‘ mavjud emas.")
    close_db()


# **Pul o'tkazish (transfer)**
def transfer():
    open_db()

    from_id = int(input("Pul jo‘natmoqchi bo‘lgan User ID ni kiriting: "))
    to_id = int(input("Pul qabul qiluvchi User ID ni kiriting: "))
    amount = int(input("Qancha summa o'tkazmoqchisiz? "))

    cursor.execute("SELECT balance FROM USERS WHERE id = ?", (from_id,))
    from_balance = cursor.fetchone()

    if from_balance and from_balance[0] >= amount:
        cursor.execute("UPDATE USERS SET balance = balance - ? WHERE id = ?", (amount, from_id))
        cursor.execute("UPDATE USERS SET balance = balance + ? WHERE id = ?", (amount, to_id))
        conn.commit()
        print(f"✅ {amount} so‘m {from_id} dan {to_id} ga o'tkazildi!")
    else:
        print("❌ Xatolik! Yetarli mablag‘ mavjud emas.")

    close_db()


# **Foydalanuvchilarni ko‘rish**
def see():
    open_db()

    cursor.execute("SELECT * FROM USERS")
    users = cursor.fetchall()

    print("\n📋 Barcha foydalanuvchilar:")
    for user in users:
        print(f"""ID: {user[0]}               
Ism: {user[1]}    
Yosh: {user[2]}   
Karta: {user[3]}  
Balans: {user[4]} So‘m
""")

    close_db()


# **Asosiy menyu**
while True:
    try:
        choice = int(input("Tanlang: "))
        if choice == 1:
            add()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            transfer()
        elif choice == 5:
            see()
        elif choice == 6:
            print("✅ Dasturdan chiqildi!")
            break
        else:
            print("❌ Xatolik! Faqat 1 dan 6 gacha bo‘lgan sonlarni kiriting!")
    except ValueError:
        print("❌ Xatolik! Faqat raqam kiriting!")
