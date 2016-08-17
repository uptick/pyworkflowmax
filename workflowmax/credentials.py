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
        return 'Credentials(api_key={apiKey}, accountKey={accountKey})'.format(**self.as_params())
