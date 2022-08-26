from dataclasses import dataclass
from typing import List, Dict, Optional
from openpix.core.utils import dataclass_to_json_dict


class JsonDict:
    def to_json_dict(self):
        return dataclass_to_json_dict(self)


@dataclass
class CustomerObject(JsonDict):
    name: str
    email: str
    phone: Optional[str] = None
    taxID: Optional[str] = None
    correlationID: Optional[str] = None


@dataclass
class ChargeObject(JsonDict):
    correlationID: str
    value: int
    comment: Optional[str] = None
    identifier: Optional[str] = None
    expiresIn: Optional[int] = None
    customer: Optional[CustomerObject] = None
    additionalInfo: Optional[List[Dict]] = None


@dataclass
class RefundObject(JsonDict):
    value: int
    transactionEndToEndId: str
    correlationID: str
