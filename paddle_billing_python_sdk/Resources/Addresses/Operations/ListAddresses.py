from paddle_billing_python_sdk.Entities.Shared.Status      import Status

from paddle_billing_python_sdk.Exceptions.SdkExceptions.InvalidArgumentException import InvalidArgumentException

from paddle_billing_python_sdk.Resources.Shared.Operations.List.Pager import Pager


class ListAddresses:
    def __init__(
            self,
            pager:    Pager = None,
            ids:      dict  = None,
            statuses: dict  = None,
            search:   str   = None,
    ):
        self.pager    = pager
        self.ids      = ids      if ids      is not None else []
        self.statuses = statuses if statuses is not None else []
        self.search   = search

        # Validation
        if any(not isinstance(pid, str) for pid in self.ids):
            raise InvalidArgumentException('ids', 'string')
        if any(not isinstance(status, Status) for status in self.statuses):
            raise InvalidArgumentException('statuses', Status.__name__)


    def get_parameters(self) -> dict:
        enum_stringify = lambda enum: enum.value  # noqa E731

        parameters = {}
        if self.pager:
            parameters.update(self.pager.get_parameters())
        if self.ids:
            parameters['id'] = ','.join(self.ids)
        if self.statuses:
            parameters['status'] = ','.join(map(enum_stringify, self.statuses))
        if self.search:
            parameters['search'] = self.search

        return parameters
