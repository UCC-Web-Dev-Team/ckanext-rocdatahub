import ckan.plugins.toolkit as tk
import ckanext.rocdatahub.logic.schema as schema


@tk.side_effect_free
def rocdatahub_get_sum(context, data_dict):
    tk.check_access(
        "rocdatahub_get_sum", context, data_dict)
    data, errors = tk.navl_validate(
        data_dict, schema.rocdatahub_get_sum(), context)

    if errors:
        raise tk.ValidationError(errors)

    return {
        "left": data["left"],
        "right": data["right"],
        "sum": data["left"] + data["right"]
    }


def get_actions():
    return {
        'rocdatahub_get_sum': rocdatahub_get_sum,
    }
