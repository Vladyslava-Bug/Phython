from adress import Address
from mailing import Mailing

sent_parsel = Mailing(
    Address("G513SF", "Glasgow", "Harmony pl", "6", "3/2"),
    Address("83062", "Donetsk", "Kuybysheva", "8", "601"), 
    26, "JBY5686154"
    )


sent_parsel.get_mail_info()

