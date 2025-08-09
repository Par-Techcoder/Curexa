from ..constants.default_values import ResponseMessageType

def success_response(message: str, data: dict = None, redirect: str = None,
                     message_type: str = ResponseMessageType.SUCCESS.value) -> dict:
    """
    Build a JSON-friendly success response.
    """
    if data is None:
        data = {}
    response = {
        "success": True,
        "status": "success",
        "data": data,
        "message_type": message_type,
        "message": message,
    }
    if redirect:
        response["redirect"] = redirect
    return response

def error_response(message: str, data: dict = None, redirect: str = None,
                   message_type: str = ResponseMessageType.ERROR.value, stack_trace: str = "") -> dict:
    """
    Build a JSON-friendly error response.
    """
    if data is None:
        data = {}
    response = {
        "error": True,
        "status": "error",
        "data": data,
        "message": message,
        "message_type": message_type,
        "stack_trace": stack_trace,
    }
    if redirect:
        response["redirect"] = redirect
    return response
