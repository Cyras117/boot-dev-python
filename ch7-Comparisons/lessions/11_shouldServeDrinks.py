def should_serve_customer(customer_age, on_break, time):
    return not on_break and  customer_age >= 21 and time>=5 and time <=10
