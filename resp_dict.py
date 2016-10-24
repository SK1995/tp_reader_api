# response codes:
# 0 - all OK
# 1 - user alredy authenticated
# 2 - no such user exist
# 3 - error parsing data
# 4 - error during working with database
# 5 - unknown error


response_dictionary = \
    {
        "response":
            {
                "code": 1,
                "message": "error"
            }
    }

def form_response_dictionary(code):
    if code == 0:
        response_dictionary['response']['code'] = 0
        response_dictionary['response']['message'] = "OK"
    if code == 1:
        response_dictionary['response']['code'] = 1
        response_dictionary['response']['message'] = "User alredy authenticated"
    if code == 2:
        response_dictionary['response']['code'] = 2
        response_dictionary['response']['message'] = "User not found"
    if code == 3:
        response_dictionary['response']['code'] = 3
        response_dictionary['response']['message'] = "Error parsing data"
    if code == 4:
        response_dictionary['response']['code'] = 4
        response_dictionary['response']['message'] = "Error during working with database"
    if code == 5:
        response_dictionary['response']['code'] = 5
        response_dictionary['response']['message'] = "Unknown error happened"
    return response_dictionary