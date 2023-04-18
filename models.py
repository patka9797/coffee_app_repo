from pydantic import BaseModel

class Coffee(BaseModel):
    id: str = None
    name: str
    origin:str
    steps: list[str]
    body: str
    portions:int
    tags: list[str]

def __str__(self):

    return f"""/
    {self.name.capitalize()}

    Origin: {self.origin}
    Steps: {self.steps}
    Body: {self.body}
    Portions: {self.portions}
    Tags: {self.tags}"""