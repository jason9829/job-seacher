class JobStreet:
    CURRENCY_LIST= ['MYR', 'SGD', 'USD']
    @classmethod
    def is_salary(self, str):
        for currency in self.CURRENCY_LIST:
            if currency in str:
                return True
        return False