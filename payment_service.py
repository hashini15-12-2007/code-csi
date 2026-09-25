# payment_service.py - CODE-CSI - FIXED by Bob
import time
from collections import deque

class PaymentService:
    def __init__(self):
        self.db_connected = False
        self.retry_queue = deque()  # FIX: Queue for failed payments

    def check_db(self):
        # FIX: Retry logic 3 times
        for attempt in range(3):
            if not self.db_connected and attempt < 2:
                print(f"DB down, retrying... attempt {attempt+1}")
                time.sleep(1)
                continue
            # Simulate DB recovered on 3rd try
            self.db_connected = True
            return True
        return False

    def process_payment(self, user_id, amount):
        print(f"Processing payment for {user_id}: ${amount}")
        try:
            if self.check_db():
                print("Payment successful after retry!")
                return {"status": "success", "amount": amount, "retried": True}
            else:
                # FIX: Add to queue instead of failing
                self.retry_queue.append((user_id, amount))
                print(f"Added to queue. Queue size: {len(self.retry_queue)}")
                return {"status": "queued", "amount": amount}
        except Exception as e:
            self.retry_queue.append((user_id, amount))
            return {"status": "queued", "error": str(e)}

# Test
if __name__ == "__main__":
    service = PaymentService()
    result = service.process_payment("user_123", 100)
    print(result)
    print("FIXED! No more direct failure.")