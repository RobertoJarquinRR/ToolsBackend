import firebase_admin
from firebase_admin import auth, credentials


cred = credentials.Certificate(r"doc\asistente-ac8f9-firebase-adminsdk-fbsvc-d32927e8b3.json")
firebase_admin.initialize_app(cred)


def validartoken(token):
    tokens = auth.verify_id_token(token)
    
    if tokens is None:
        return False
    
    return True



