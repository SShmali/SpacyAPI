from typing import Dict

from spacy.language import Language


class EntityExtractor:
    """class SpacyExtractor encapsulates logic to pipe Record with a text body
    through a spacy model and return entities.
    """

    def __init__(
        self, nlp: Language, input_text_col: str = "text"
    ):
        """Initialize the SpacyExtractor pipeline.
        
        nlp (spacy.language.Language): pre-loaded spacy language model
        input_text_col (str): property on document to run the model on

        RETURNS (EntityRecognizer): The newly constructed object.
        """
        self.nlp = nlp
        self.input_text_col = input_text_col

    def extract_entities(self, doc: Dict[str]):
        """Apply the pre-trained model to a batch of records
        
        doc : "document" dictionary each with an
            `text` property
        
        RETURNS (list): response containing
            the correlating document and a list of entities.
        """
        text = doc[self.input_text_col]
        spacy_doc = self.nlp.pipe(text)
        entities = {}
        for ent in spacy_doc.ents:
            entities= {
                        "name": ent.text,
                        "label": ent.label_,
                        "matches": [],
                    }
            entities["match"].append(
                    {"start": ent.start_char, "end": ent.end_char, "negation": ent._.negex}
                )



