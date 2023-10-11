class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def get_mail_info(self):
        print(f'Sending {self.track} FROM {self.from_address.post_code}, {self.from_address.city}, {self.from_address.street}, {self.from_address.build} - {self.from_address.flat} TO {self.to_address.post_code}, {self.to_address.city}, {self.to_address.street}, {self.to_address.build} - {self.to_address.flat}. Costs is {self.cost}')



