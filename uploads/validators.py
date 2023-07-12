from cerberus import Validator
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator


class CustomValidator(Validator):

    def _validate_is_url(self, is_url, field, value):
        """Test if a value is a valid url.
        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if is_url:
            validate_url = URLValidator()

            try:
                validate_url(value)
            except ValidationError:
                self._error(field, 'Invalid url')


def validate_create_image_upload(data):
    schema = {
        'uuid': {'type': 'string', 'required': True},
        'description': {'type': 'string', 'required': True},
        'images': {'type': 'list', 'schema': {'type': 'string', 'is_url': True}, 'empty': False}
    }

    v = CustomValidator(schema)
    v.validate(data)
    if v.errors:
        return v.errors
    
    return None

def validate_update_image_upload(data):
    schema = {
        'description': {'type': 'string', 'required': True}
    }

    v = Validator(schema)
    v.validate(data)

    if v.errors:
        return v.errors

    return None