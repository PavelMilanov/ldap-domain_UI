from typing import List
from urllib import response
from ldap3 import Server, Connection, ALL, NTLM
from environs import Env
import json
from datetime import datetime
from typing import List
from models.ldap3 import Customer

env = Env()
env.read_env()



class Ldap3Connector:
    
    server = Server(env('DC'), get_info=ALL)
    conn = Connection(server, user=env('domain_user'), password=env('domain_password') , auto_bind=True, authentication=NTLM)


    def get_domain_user(self, name: str) -> None:
        self.conn.search(env('customer_forest'), f'(&(objectclass=person)(cn={name}))', attributes=['*'])
        data = json.loads(self.conn.entries[0].entry_to_json())
        logoff = datetime.strptime(data['attributes']['lastLogoff'][0], '%Y-%m-%d %H:%M:%S.%f%z')
        logon= datetime.strptime(data['attributes']['lastLogon'][0], '%Y-%m-%d %H:%M:%S.%f%z')
        valid_data = Customer(
            name=data['attributes']['cn'][0],
            lastlogoff=logoff,
            lastlogon=logon
        )
        return valid_data
