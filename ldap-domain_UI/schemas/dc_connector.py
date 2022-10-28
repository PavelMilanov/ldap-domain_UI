from fastapi import APIRouter
from utils.ldap3 import Ldap3Connector
from models import ldap3


router = APIRouter(
    prefix='/api/v1/ldap3',
    tags=['ldap3']
)


@router.get('/')
def get_user(customer_name: str) -> ldap3.Customer:
    conn = Ldap3Connector()
    return conn.get_domain_user(customer_name)
    
