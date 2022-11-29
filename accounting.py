"""
TODO
"""
import sys
lis = sys.argv[1:]
if __name__=="__main__":

        
    from user import authentication

    from transactions import journal
    from banking import reconciliation

    
    for i in lis:
        print(i)
    
    

    authentication.authenticate_user()
    journal.receive_income(100.00)
    journal.pay_expense(100.00)
    reconciliation.do_reconciliation()
        
    





        