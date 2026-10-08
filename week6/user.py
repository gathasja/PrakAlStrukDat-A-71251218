<<<<<<< HEAD
_user_db = None

def user_data_by_username():
    # https://www.w3schools.com/Python/ref_keyword_global.asp -> silahkan kalau mau baca baca terkait global
    global _user_db
    if _user_db is None:
        _user_db = {
            "Kiya":{
                "id": 1,
                "password": "123",
                "role": "Peserta"
            },
            "Kevin":{
                "id": 2,
                "password": "321",
                "role": "Peserta"
            },
            "Semmi":{
                "id": 3,
                "password": "admin",
                "role": "Admin"
            }
        }
=======
_user_db = None

def user_data_by_username():
    # https://www.w3schools.com/Python/ref_keyword_global.asp -> silahkan kalau mau baca baca terkait global
    global _user_db
    if _user_db is None:
        _user_db = {
            "Kiya":{
                "id": 1,
                "password": "123",
                "role": "Peserta"
            },
            "Kevin":{
                "id": 2,
                "password": "321",
                "role": "Peserta"
            },
            "Semmi":{
                "id": 3,
                "password": "admin",
                "role": "Admin"
            }
        }
>>>>>>> f623a06e2e536e326546add85cb7addf0433d0f2
    return _user_db