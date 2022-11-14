import spacy
import srsly
from fastapi import Body, FastAPI
from negspacy.negation import Negex
from pydantic import BaseModel
from starlette.responses import RedirectResponse

from app.entity_extractor import EntityExtractor
from app.models import RecordRequest, RecordResponse

app = FastAPI(
    title="health Text Analysis",
    version="1.0",
    description="exteaxt medical conditions entities from patient text notes",
)

example_request = srsly.read_json("app/data/example_request.json")

nlp = spacy.load("en_core_sci_scibert")

nlp.Defaults.stop_words |= {"patient","days",}

nlp.add_pipe("negex", config={"chunk_prefix": ["no"]},last=True)

extractor = EntityExtractor(nlp)

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse("/docs")


@app.post("/entities", response_model=RecordResponse, tags=["NER"])
async def extract_entities(body: RecordRequest = Body(..., example=example_request)):
    """Extract Named Entities from a document."""

    res = []
    document = {"text": body.data.text}

    entities_res = extractor.extract_entities(document)

    res = {"entities":  entities_res["entities"]}

    return {"values": res}