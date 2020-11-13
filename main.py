"""
Developed by: L. Smalbil

This tool can be used to quickly compute the NVP of a project or investment.

"""

from npv import NPV

if __name__ == "__main__":

    projected_cash_flows = [-3000, 500, 1000, 1000, 400, 300]
    discount_rate = -0.005

    projected_cash_flows_other_project = [-2000, 500, 1000, 1000, 400, 200]

    NPV_object = NPV(discount_rate, projected_cash_flows)

    print('The estimated NPV for this project is: ', NPV_object.compute_npv())
    print('\nThe machine qualifies the investment as follows: ', NPV_object.advise())
    print('\nWhen comparing the two projects, the machine comes to the following conclusion.', NPV_object.npv_comparison(projected_cash_flows_other_project))

    print(NPV_object.compute_discount_rate(future_value=4000, present_value= 3800, n=5))