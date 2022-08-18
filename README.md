# Customer-service
Customer service 

insertCategory
-----------------------------------------
CatID  | CatName | CatDescription
insertProducts  (Pre requisite : Categories should exist)
-----------------------------------------
Pid    | Pname   |   Price     | CategoryId
insertCustomerDetails
------------------------------------------
CustId  |  CustEmail      | CustPhonenumber  |Status_Recieved        | Address      | Location    | Country

                                                                          --------------
                                                                          YES/NO/Return
ordersPlaced
------------------------------------------
OrdId  |  Pid   | Quantity   | TotalPrice    | CustomerId     |  Status
                                                                -------------
                                                                 Delivered
                                                                 Shipping
===============================================================================
Admin : to get the total sales
        a) Based on product ID
        b) Based on category
        c) Based on the price range (low to high )
                                    (high to low)
        d)based on location
