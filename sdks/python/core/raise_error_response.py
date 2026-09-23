import typing
from json.decoder import JSONDecodeError

import httpx
from .api_error import ApiError


def raise_error_response(response: httpx.Response) -> typing.NoReturn:
    """Raise the typed error for a non-2xx response."""
    from ..errors.bad_request_error import BadRequestError
    from ..errors.forbidden_error import ForbiddenError
    from ..errors.internal_server_error import InternalServerError
    from ..errors.method_failure_error import MethodFailureError
    from ..errors.unauthorized_error import UnauthorizedError

    headers = dict(response.headers)
    try:
        body: typing.Any = response.json()
    except JSONDecodeError:
        body = response.text
    errors: typing.Dict[int, typing.Any] = {
        400: BadRequestError,
        401: UnauthorizedError,
        403: ForbiddenError,
        420: MethodFailureError,
        500: InternalServerError,
    }
    error = errors.get(response.status_code)
    if error is not None:
        raise error(headers=headers, body=body)
    raise ApiError(status_code=response.status_code, headers=headers, body=body)
