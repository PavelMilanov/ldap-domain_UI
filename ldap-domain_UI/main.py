from ldap3 import Server, Connection, ALL, NTLM
from environs import Env


env = Env()
env.read_env()


server = Server(env('DC'), get_info=ALL)
conn = Connection(server, user=env('domain_user'), password=env('domain_password') , auto_bind=True, authentication=NTLM)

conn.search(f"dc={env('domain_root')},dc={env('domain_forest')}", '(&(objectclass=person)(uid=Administrator))')
print(conn.entries)