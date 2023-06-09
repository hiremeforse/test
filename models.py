from typing import Optional, List
from uuid import UUID,uuid4
from pydantic import BaseModel
from enum import Enum


class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    male = "admin"
    female = "user"
    student = "student"


class User(BaseModel):
    id : Optional[UUID] = uuid4()
    firstname : str
    middlename : Optional[str]
    lastname : str
    gender : Gender
    roles : List[Role]

class Userupaterequest(BaseModel):
    firstname : Optional[str]
    lastname : optional[str]




