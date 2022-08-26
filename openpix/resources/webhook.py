import json
from openpix.core import OPBase
from openpix.core.entities import WebhookObject


class Webhook(OPBase):
    def search(self, filters=None, request_options=None):
        return self._get(
            "/api/openpix/v1/webhook", filters=filters, request_options=request_options
        )

    def delete(self, webhook_id, request_options=None):
        return self._delete(
            "/api/openpix/v1/webhook/" + str(webhook_id),
            request_options=request_options,
        )

    def create(self, webhook: WebhookObject, request_options=None):
        return self._post(
            "/api/openpix/v1/webhook",
            data={"webhook": webhook.to_json_dict()},
            request_options=request_options,
        )
