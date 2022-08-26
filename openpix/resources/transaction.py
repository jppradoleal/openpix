from openpix.core import OPBase


class Transaction(OPBase):
    def search(self, filters=None, request_options=None):
        return self._get(
            "/api/openpix/v1/transaction",
            filters=filters,
            request_options=request_options,
        )

    def get(self, transaction_id, request_options=None):
        return self._get(
            "/api/openpix/v1/transaction/" + str(transaction_id),
            request_options=request_options,
        )
