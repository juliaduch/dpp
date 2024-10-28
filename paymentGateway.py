from enum import Enum


class TransactionStatus(Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class TransactionResult:
    def __init__(self, success: bool, transaction_id: str, transaction_status: TransactionStatus, message: str = ""):
        self.success = success
        self.transaction_id = transaction_id
        self.message = message
        self.transaction_status = transaction_status


class PaymentException(Exception):
    pass


class NetworkException(Exception):
    pass


class RefundException(Exception):
    pass


class PaymentGateway:
    def charge(self, user_id: str, amount: float):
        # testowy return
        return TransactionResult(success=True, transaction_id="test123", transaction_status=TransactionStatus.COMPLETED)

    def refund(self, transaction_id: str) -> TransactionResult:
        raise NotImplementedError(
            "This method should be overridden in a subclass or mocked.")

    def get_status(self, transaction_id: str) -> TransactionStatus:
        raise NotImplementedError(
            "This method should be overridden in a subclass or mocked.")
