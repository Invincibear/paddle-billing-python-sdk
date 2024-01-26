from paddle_billing_python_sdk.EnumStringify import enum_stringify

from paddle_billing_python_sdk.Entities.Shared.Status import Status

from paddle_billing_python_sdk.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager import Pager


class ListCustomers:
    def __init__(
        self,
        pager:    Pager        = None,
        ids:      list[str]    = None,
        statuses: list[Status] = None,
        search:   str          = None,
        emails:   list[str]    = None,
    ):
        self.pager    = pager
        self.search   = search
        self.ids      = ids      if ids      is not None else []
        self.statuses = statuses if statuses is not None else []
        self.emails   = emails   if emails   is not None else []

        # Validation
        for field_name, field_value, field_type in [
            ('ids',      self.ids,      str),
            ('statuses', self.statuses, Status),
            ('emails',   self.emails,   str),
        ]:
            invalid_items = [item for item in field_value if not isinstance(item, field_type)]
            if invalid_items:
                raise InvalidArgumentException(field_name, field_type.__name__, invalid_items)


    def get_parameters(self) -> dict:
        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.ids:
            parameters['id'] = ','.join(self.ids)
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))
        if self.search:
            parameters['search'] = self.search
        if self.emails:
            parameters['email'] = ','.join(self.emails)

        return parameters