from __future__  import annotations
from dataclasses import dataclass

from src.Entities.Entity import Entity

from src.Entities.Collections.EventTypeCollection import EventTypeCollection

from src.Entities.NotificationSettings.NotificationSettingType import NotificationSettingType


@dataclass
class NotificationSetting(Entity):
    id:                       str
    description:              str
    type:                     NotificationSettingType
    destination:              str
    active:                   bool
    api_version:              int
    include_sensitive_fields: bool
    subscribed_events:        EventTypeCollection
    endpoint_secret_key:      str


    @classmethod
    def from_dict(cls, data: dict) -> NotificationSetting:
        return NotificationSetting(
            id                       = data['id'],
            description              = data['description'],
            type                     = NotificationSettingType(data['type']),
            destination              = data['destination'],
            active                   = data['active'],
            api_version              = data['api_version'],
            include_sensitive_fields = data['include_sensitive_fields'],
            subscribed_events        = EventTypeCollection.from_list(data['subscribed_events']),
            endpoint_secret_key      = data['endpoint_secret_key'],
        )
