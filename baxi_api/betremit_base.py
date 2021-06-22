

class BetremitBase(object):
    """ This is the core of the implementation. It contains the encryption and initialization functions.
    def __init__(self,apiKey)"""

    def __init__(self, apiKey=None):
        self._apiKey = apiKey
        self._baseUrl = "https://payments.baxipay.com.ng/api/baxipay"
        self._endPoint = {
            "superagent": {

                "requery": "/superagent/transaction/requery",
                "retry": '/superagent/transaction/retry',
                "agent_balance": "/superagent/account/balance",
                "refresh": "/superagent/services/refresh",

            },
            "billers": {
                "list_providers": "/billers/providers/list",
                "list_services": "/billers/services/list",
                "list_category": "/billers/category/all",
                "service_in_category": "/billers/services/category",

            },
            "preauth": {

                "verify_account": "/services/namefinder/query",

            },
            "airtime": {

                "list_providers": "/services/airtime/providers",
                "request": "/services/airtime/request"

            },

        }

    def _getApiKey(self):
        return self._apiKey
