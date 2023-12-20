import ckan.plugins.toolkit as tk
from ckan import types


@tk.auth_allow_anonymous_access
def rocdatahub_get_sum(context, data_dict):
    return {"success": True}


def get_auth_functions():
    return {
        "rocdatahub_get_sum": rocdatahub_get_sum,
    }

# @tk.auth_allow_anonymous_access
# @tk.chained_auth_function
# def user_create(
#     next_func: types.AuthFunction,
#     context: types.Context,
#     data_dict: types.DataDict | None,
# ) -> types.AuthResult:
#     return {"success": True}