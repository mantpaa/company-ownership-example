from flask import Flask
from collections import defaultdict
import csv

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'

class OwnershipRecord:
    def __init__(self,
                 orgnr,
                 company_name,
                 share_class,
                 owner_name,
                 owner_birth_or_orgnr,
                 owner_postal_address,
                 owner_country,
                 number_of_shares,
                 total_shares):
        self.orgnr = orgnr
        self.company_name = company_name
        self.share_class = share_class
        self.owner_name = owner_name
        self.owner_birth_or_orgnr = owner_birth_or_orgnr
        self.owner_postal_address = owner_postal_address
        self.owner_country = owner_country
        self.number_of_shares = number_of_shares
        self.total_shares = total_shares

def get_holdings(orgnr, data):
    l = []
    for k,v in data.items():
        print(k,v)
        for r in v:
            if r.owner_birth_or_orgnr == orgnr:
                l.append(r)
    return l
                
if __name__=='__main__':
    #app.run(port=9999)
    data = defaultdict(list)

    with open('tests/../data/example.csv','r') as f:
        reader = csv.reader(f,delimiter=';')
        for row in reader:
            (orgnr, company_name, share_class,
             owner_name, owner_birth_or_orgnr,
             owner_postal_address, owner_country,
             number_of_shares, total_shares) = row

            data[orgnr].append(OwnershipRecord(
                orgnr,
                company_name,
                share_class,
                owner_name,
                owner_birth_or_orgnr,
                owner_postal_address,
                owner_country,
                int(number_of_shares),
                int(total_shares))
            )
    l = []
    orgnr = '885648312'
    for k,v in data.items():
        print(k,v)
        for r in v:
            if r.owner_birth_or_orgnr == orgnr:
                l.append(r)
        
    print("holdings: ",l)
    
    l = set([holding.share_class for holding in get_holdings(orgnr, data)])
    print('unique sharesj')
    print(l)
    l = data[orgnr]
    for o in l:
        print(o)
    
