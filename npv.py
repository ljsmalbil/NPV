import numpy as np

class NPV:
    def __init__(self, discount_rate, cashflows):
        self.discount_rate = discount_rate
        self.cashflows = cashflows

    def compute_npv(self):
        total_values = []
        for value in self.cashflows:
            value_at_time = value / (1 + self.discount_rate)
            total_values.append(value_at_time)

        return np.round(np.sum(total_values),2)

    def advise(self):
        NPV_object = NPV(self.discount_rate, self.cashflows)
        npv = NPV_object.compute_npv()
        if npv < 0:
            return 'Investment is not profitable.'
        elif npv > 0:
            return 'Investment is profitable.'
        else:
            return 'Investment will break even.'

    def npv_comparison(self, second_cashflows):
        investment_one = NPV(self.discount_rate, self.cashflows)
        ivestment_two = NPV(self.discount_rate, second_cashflows)

        if investment_one.compute_npv() > ivestment_two.compute_npv():
            return 'The original investment is more profitable. The difference is: ' + str(abs(np.round(investment_one.compute_npv() - ivestment_two.compute_npv(),2)))
        else:
            return 'The other investment is more profitable. The difference is: ' + str(abs(np.round(investment_one.compute_npv() - ivestment_two.compute_npv(),2)))

    def compute_discount_rate(self, future_value, present_value, n):
        """
        This function can be used to compute the discount rate when the FV and PV are known

        :param FV:
        :param n: time span
        :return:
        """

        return ((future_value / (present_value))**(1/n)) - 1

