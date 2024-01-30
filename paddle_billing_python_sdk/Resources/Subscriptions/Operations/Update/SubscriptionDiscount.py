from dataclasses import dataclass

from paddle_billing_python_sdk.Entities.Subscriptions.SubscriptionEffectiveFrom import SubscriptionEffectiveFrom


@dataclass
class SubscriptionDiscount:
    id:             str
    effective_from: SubscriptionEffectiveFrom
