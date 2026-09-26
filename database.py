
import random
def check_db():
    if random.choice([True, False]):
        raise TimeoutError("Database connection timeout!")
    return True
def save_payment(user_id, amount):
    check_db()
    return {"user": user_id, "amount": amount, "saved": True}
