from openpix.core import OPBase
from openpix.core.entities import CustomerObject


class Customer(OPBase):
    def search(self, filters=None, request_options=None):
        return self._get(
            "/api/openpix/v1/customer", filters=filters, request_options=request_options
        )

    def get(self, customer_id, request_options=None):
        return self._get(
            "/api/openpix/v1/customer/" + str(customer_id),
            request_options=request_options,
        )

    def create(self, customer: CustomerObject, request_options=None):
        return self._post(
            "/api/openpix/v1/customer",
            data=customer.to_json_dict(),
            request_options=request_options,
        )
