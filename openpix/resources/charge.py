from openpix.core import OPBase
from openpix.core.entities import ChargeObject


class Charge(OPBase):
    def search(self, filters=None, request_options=None):
        return self._get(
            "/api/openpix/v1/charge", filters=filters, request_options=request_options
        )

    def get(self, charge_id, request_options=None):
        return self._get(
            "/api/openpix/v1/charge/" + str(charge_id), request_options=request_options
        )

    def create(self, charge: ChargeObject, idempotent=False, request_options=None):
        return self._post(
            "/api/openpix/v1/charge",
            params={ "return_existing": str(idempotent).lower() },
            data=charge.to_json_dict(),
            request_options=request_options,
        )
