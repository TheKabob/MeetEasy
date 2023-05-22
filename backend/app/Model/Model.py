from pydantic import BaseModel, constr


class register_user(BaseModel):
    name: constr(min_length=1, strip_whitespace=True)
    email: constr(min_length=1, strip_whitespace=True)
    password: constr(min_length=1, strip_whitespace=True)


class login_user(BaseModel):
    email: constr(min_length=1, strip_whitespace=True)
    password: constr(min_length=1, strip_whitespace=True)
