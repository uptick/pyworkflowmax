class Credentials():
    def __init__(self, api_key, account_key):
        self.api_key = api_key
        self.account_key = account_key

    def as_params(self):
        return {
            'apiKey': self.api_key,
            'accountKey': self.account_key
        }

    def __repr__(self):
        return '{}:\n    api_key={apiKey}\n    accountKey={accountKey}'.format(
            self.__class__.__name__,
            **self.as_params()
        )
