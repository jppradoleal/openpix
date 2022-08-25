from openpix.core import OPBase
from openpix.core.entities import RefundObject


class Refund(OPBase):
    def search(self, filters=None, request_options=None):
        return self._get(
            "/api/openpix/v1/refund", filters=filters, request_options=request_options
        )

    def get(self, refund_id, request_options=None):
        return self._get(
            "/api/openpix/v1/refund/" + str(refund_id), request_options=request_options
        )

    def create(self, refund: RefundObject, request_options=None):
        return self._post(
            "/api/openpix/v1/refund",
            data=refund.to_json_dict(),
            request_options=request_options,
        )
