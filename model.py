import inspect, attr, attrs
from attr import define, frozen, field, validators
from typing import Optional
from datetime import date

@frozen
class OrderLine:
    orderid: str
    sku: str
    qty: int

@define
class Batch:
    reference: str
    sku: str
    qty: int
    eta: Optional[date] = field(validator=validators.optional(validators.instance_of(date)), default=None)
    
    def can_allocate(self, line: OrderLine):
        return self.sku == line.sku and self.qty >= line.qty

    def allocate(self, line: OrderLine):
        if self.can_allocate
        self.qty -= line.qty

