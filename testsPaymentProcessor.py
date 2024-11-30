import unittest
from unittest.mock import Mock
from paymentGateway import (
    PaymentGateway,
    TransactionResult,
    TransactionStatus,
)
from paymentProcessor import PaymentProcessor


class TestPaymentProcessor(unittest.TestCase):
    def setUp(self):
        # Inicjalizacja mocka PaymentGateway
        self.gateway_mock = Mock(spec=PaymentGateway)
        # Inicjalizacja PaymentProcessor z mockiem
        self.processor = PaymentProcessor(gateway=self.gateway_mock)

    # Testy dla processPayment
    def test_process_payment_success(self):
        """Prawidłowe przetworzenie płatności."""
        # Konfiguracja mocka, aby symulował sukces transakcji
        self.gateway_mock.charge.return_value = TransactionResult(
            success=True,
            transaction_id="123",
            message="Payment successful",
            transaction_status=TransactionStatus.COMPLETED,
        )

        # Wywołanie testowanej metody
        result = self.processor.process_payment("user_1", 100.0)

        # Sprawdzanie oczekiwań
        self.assertTrue(result.success)
        self.assertEqual(result.transaction_id, "123")
        self.assertEqual(result.message, "Payment successful")
        self.assertEqual(result.transaction_status,
                         TransactionStatus.COMPLETED)
        self.gateway_mock.charge.assert_called_once_with("user_1", 100.0)

    def test_process_payment_insufficient_funds(self):
        """Niepowodzenie płatności z powodu braku środków."""
        # Konfiguracja mocka, aby symulował niepowodzenie transakcji
        self.gateway_mock.charge.return_value = TransactionResult(
            success=False,
            transaction_id="456",
            message="Insufficient funds",
            transaction_status=TransactionStatus.FAILED,
        )

        result = self.processor.process_payment("user_1", 100.0)

        self.assertFalse(result.success)
        self.assertEqual(result.transaction_id, "456")
        self.assertEqual(result.message, "Insufficient funds")
        self.assertEqual(result.transaction_status, TransactionStatus.FAILED)

    # def test_process_payment_network_exception(self):
    #     """Obsługa wyjątku NetworkException przy przetwarzaniu płatności."""
    #     self.gateway_mock.charge.side_effect = NetworkException(
    #         "Network error")

    #     result = self.processor.process_payment("user_1", 100.0)

    #     self.assertFalse(result.success)
    #     self.assertEqual(result.message, "Network error")
    #     self.gateway_mock.charge.assert_called_once_with("user_1", 100.0)

    # def test_process_payment_invalid_amount(self):
    #     """Walidacja nieprawidłowej kwoty (ujemna kwota)."""
    #     result = self.processor.process_payment("user_1", -50.0)
    #     self.assertFalse(result.success)
    #     self.assertEqual(result.message, "Invalid amount")

    # Testy dla refundPayment
    def test_refund_payment_success(self):
        """Prawidłowe dokonanie zwrotu."""
        self.gateway_mock.refund.return_value = TransactionResult(
            success=True,
            transaction_id="789",
            message="Refund successful",
            transaction_status=TransactionStatus.COMPLETED,
        )

        result = self.processor.refund_payment("789")

        self.assertTrue(result.success)
        self.assertEqual(result.transaction_id, "789")
        self.assertEqual(result.message, "Refund successful")
        self.gateway_mock.refund.assert_called_once_with("789")

    def test_refund_payment_nonexistent_transaction(self):
        """Niepowodzenie zwrotu z powodu nieistniejącej transakcji."""
        self.gateway_mock.refund.return_value = TransactionResult(
            success=False,
            transaction_id="000",
            message="Transaction not found",
            transaction_status=TransactionStatus.FAILED,
        )

        result = self.processor.refund_payment("000")

        self.assertFalse(result.success)
        self.assertEqual(result.transaction_id, "000")
        self.assertEqual(result.message, "Transaction not found")
        self.gateway_mock.refund.assert_called_once_with("000")

    # def test_refund_payment_network_exception(self):
    #     """Obsługa wyjątku NetworkException przy dokonywaniu zwrotu."""
    #     self.gateway_mock.refund.side_effect = NetworkException(
    #         "Network error")

    #     result = self.processor.refund_payment("123")

    #     self.assertFalse(result.success)
    #     self.assertEqual(result.message, "Network error")
    #     self.gateway_mock.refund.assert_called_once_with("123")

    # Testy dla getPaymentStatus
    def test_get_payment_status_completed(self):
        """Pobranie poprawnego statusu transakcji."""
        self.gateway_mock.get_status.return_value = TransactionStatus.COMPLETED

        status = self.processor.get_payment_status("123")

        self.assertEqual(status, TransactionStatus.COMPLETED)
        self.gateway_mock.get_status.assert_called_once_with("123")

    def test_get_payment_status_nonexistent_transaction(self):
        """Obsługa nieistniejącej transakcji."""
        self.gateway_mock.get_status.return_value = None

        status = self.processor.get_payment_status("000")

        self.assertIsNone(status)
        self.gateway_mock.get_status.assert_called_once_with("000")

    # def test_get_payment_status_network_exception(self):
    #     self.gateway_mock.get_status.side_effect = NetworkException(
    #         "Network error")

    #     status = self.processor.get_payment_status("123")

    #     self.assertIsNone(status)
    #     self.gateway_mock.get_status.assert_called_once_with("123")


if __name__ == "__main__":
    unittest.main()
