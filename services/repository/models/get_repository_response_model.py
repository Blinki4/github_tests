from pydantic import BaseModel


class GetRepositoryResponseOwnerModel(BaseModel):
    login: str
    id: int
    url: str
    type: str

class GetRepositoryResponseModel(BaseModel):
    id: int
    name: str
    full_name: str
    owner: GetRepositoryResponseOwnerModel
    private: bool
    description: str | None