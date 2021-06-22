from baxi_api.betremit_airtime import Airtime
from baxi_api.betremit_base import BetremitBase
from baxi_api.billers import Billers
from baxi_api.transactions import AgentTransaction
from baxi_api.verify_account import VerifyAccount


class Betremit:

    def __init__(self, apiKey):
        """
        This is main organizing object. It contains the following:\n
        betremit.Airtime -- For Airtime Transactions\n
        betremit.Billers -- For TV subscription \n
        betremit.VerifyAccount -- Preauth class to verify account details before transaction\n
        betremit.AgentTransaction -- for super users to carry out agent transactions\n
        """

        self.Airtime = Airtime(apiKey)
        self.Billers = Billers(apiKey)
        self.AgentTransaction = AgentTransaction(apiKey)
        self.VerifyAccount = VerifyAccount(apiKey)
