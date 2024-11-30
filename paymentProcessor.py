import logging
from paymentGateway import (
    PaymentGateway,
    TransactionResult,
    TransactionStatus,
    PaymentException,
    NetworkException,
    RefundException,
)


class PaymentProcessor:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway
        self.logger = logging.getLogger(__name__)

    def process_payment(self, user_id: str,
                        amount: float) -> TransactionResult:
        if not user_id or amount <= 0:
            raise ValueError("Invalid user ID or amount.")
        try:
            result = self.gateway.charge(user_id, amount)
            self.logger.info(f"Processed payment for {user_id}: {result}")
            return result
        except NetworkException:
            self.logger.error("Network error during payment processing.")
            raise
        except PaymentException:
            self.logger.error("Payment error occurred.")
            raise

    def refund_payment(self, transaction_id: str) -> TransactionResult:
        if not transaction_id:
            raise ValueError("Invalid transaction ID.")
        try:
            result = self.gateway.refund(transaction_id)
            self.logger.info(
                f"Processed refund for transaction {transaction_id}: {result}"
            )
            return result
        except NetworkException:
            self.logger.error("Network error during refund.")
            raise
        except RefundException:
            self.logger.error("Refund error")
            raise

    def get_payment_status(self, transaction_id: str) -> TransactionStatus:
        if not transaction_id:
            raise ValueError("Invalid transaction ID.")
        try:
            status = self.gateway.get_status(
                transaction_id)
            self.logger.info(
                f"Fetched payment status for {transaction_id}: {status}")
            return status
        except NetworkException:
            self.logger.error("Network error when fetching payment status.")
            raise
