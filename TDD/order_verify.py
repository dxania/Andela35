delivered_orders = [1,2,3,4,5]
pending_orders = [7,8,9,10]


def check_order_status_delivered(order_id):
    # for order in delivered_orders:
    #     if order_id:
    #         return True
    #     else:
    #         return False
    return delivered_orders.__contains__(order_id)
    # return order_id in delivered_orders   

def check_order_status_pending(order_id):
    return pending_orders.__contains__(order_id)

def check_none_existent_order(order_id):
    if order_id in delivered_orders or order_id in pending_orders:
        print("Details:", order_id)
        # print("Details {order_id}".format(order_id))
        # print("f"{order_id} is funny."")
        # print(f"I have {order_id} dogs")
        return True
    else:
        print("Order with that ID doesn't exist" )
        return False

def add_new_order(order_id):
    if not isinstance(order_id,int):
        print("Order_id must be a number") 
        return False
    else:
        pending_orders.append(order_id)
        print("Order", order_id, "has successfully been added")
        return True

def change_order_status(order_id):
    if order_id in pending_orders:
        delivered_orders.append(order_id)
        pending_orders.remove(order_id)
        print(order_id, "is now delivered")
        return True
    else:
        print("The order is not in the pending list")
        return False