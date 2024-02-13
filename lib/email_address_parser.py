import re
class EmailAddressParser:
    def __init__(self, addresses):
        self.addresses = addresses
    
    def parse(self):
        #regex = re.compile(r'[A-z0-9\-]@[A-z0-9\-].[A-z]')
        regex_to_split = re.compile(r'[\s,]+')
        list = regex_to_split.split(self.addresses)


        nonduplicate_list = []
        regex_to_verify = re.compile(r'[A-z0-9\-.]+@[A-z0-9\-]+.[A-z]+')
        for item in list:
            if item not in nonduplicate_list and regex_to_verify.fullmatch(item):
                nonduplicate_list.append(item)
        return sorted(nonduplicate_list)