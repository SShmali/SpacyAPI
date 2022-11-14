from typing import Dict

from spacy.language import Language


class EntityExtractor:
    """class SpacyExtractor encapsulates logic to pipe Record with a text body
    through a spacy model and return entities.
    """

    def __init__(
        self, nlp: Language, input_text: str = "text"
    ):
        """Initialize the SpacyExtractor pipeline.
        
        nlp (spacy.language.Language): pre-loaded spacy language model
        input_text_col (str): property on document to run the model on

        RETURNS (EntityRecognizer): The newly constructed object.
        """
        self.nlp = nlp
        self.input_text = input_text

    def extract_entities(self, doc: Dict[str]):
        """Apply the pre-trained model to a batch of records
        
        doc : "document" dictionary each with an
            `text` property
        
        RETURNS (list): response containing
            the correlating document and a list of entities.
        """
        text = doc[self.input_text]
        spacy_doc = self.nlp.pipe(text)
        entities = []
        for ent in spacy_doc.ents:
            if ent.text in self.nlp.Defaults.stop_words:
              continue

            entity= {
                        "name": ent.text,
                        "label": ent.label_,
                        "match": [],
                    }
            entity["match"].append(
                    {"start": ent.start_char, "end": ent.end_char, "negation": ent._.negex}
                )
            entities.append(entity)

        return entities



