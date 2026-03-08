from pydantic import BaseModel


class GetRepoResponse(BaseModel):
    id: int
    name: str
    full_name: str
    private: bool
    description: str | None