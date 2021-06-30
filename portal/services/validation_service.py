from numbers import Number


def validate_requirements_data(attrs):
    if "title" in attrs and len(attrs.get("title")) < 1:
        return "title field is required"
    elif "options" in attrs and len(attrs["options"]) > 0:
        options = attrs.get("options")
        for option in options:
            if option.get("name", None) is None or option.get("price") is None:
                return "Provide valid options value"
    else:
        return "Please provide valid options"


def validate_addons_data(attrs):
    if "title" in attrs and len(attrs.get("title")) < 1:
        return "title field is required"
    if "price" in attrs and len(attrs.get("price")) < 1:
        return "price field is required"
    elif "options" in attrs and len(attrs["options"]) > 0:
        options = attrs.get("options")
        for option in options:
            if option.get("name", None) is None:
                return "Provide valid options value"
    else:
        return "Please provide valid options"


def validate_order_data(attrs):
    if "job_title" in attrs and len(attrs.get("job_title")) < 1:
        return "Job title field is required"
    if "image_type" in attrs and attrs.get("image_type", None) is not None and attrs.get("image_type") not in [1, 2, 3]:
        return "Please provide a valid image type"
    if "image" in attrs and len(attrs.get("image")) < 0 and "image_path" in attrs and attrs.get("image_path", None) is not None:
        if "image_path" in attrs and len(attrs.get("image_path")) < 1:
            return "Please provide a valid image path"
        if "image_quantity" in attrs and attrs.get("image_quantity", None) is None and attrs.get("image_quantity", None) is not Number:
            return "Please provide valid number quantity"
        pass


def validate_quotation_data(attrs):
    if "job_title" in attrs and len(attrs.get("job_title")) < 1:
        return "Job title field is required"
    if "image_type" in attrs and attrs.get("image_type", None) is not None and attrs.get("image_type") not in [1, 2, 3]:
        return "Please provide a valid image type"
    if "image" in attrs and len(attrs.get("image")) < 0 and "image_path" in attrs and attrs.get("image_path", None) is not None:
        if "image_path" in attrs and len(attrs.get("image_path")) < 1:
            return "Please provide a valid image path"
        if "image_quantity" in attrs and attrs.get("image_quantity", None) is None and attrs.get("image_quantity", None) is not Number:
            return "Please provide valid number quantity"
        pass
