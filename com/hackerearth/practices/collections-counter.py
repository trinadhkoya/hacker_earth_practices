'''
Created on Nov 5, 2016

@author: trina
'''
from collections import Counter
_ = input()
sizes_displayed_by_shop = input().split()
total = 0
for _ in range(int(input())): 
    customer_prefered_size, customer_paid_charge = input().split()
    if customer_prefered_size in Counter(sizes_displayed_by_shop).keys():
        total += int(customer_paid_charge)
        sizes_displayed_by_shop.remove(customer_prefered_size)
print(total)


        
        
    


