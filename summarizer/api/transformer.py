import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
with open("config.json") as json_file:
    config = json.load(json_file)


class Transformer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("t5-base")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
        #self.tokenizer = AutoTokenizer.from_pretrained(config["PRE_TRAINED_MODEL"])
        #self.model = AutoModelForSeq2SeqLM.from_pretrained("PRE_TRAINED_MODEL")

    def summarize(self, text):
        encoded_text = self.tokenizer.encode(
            "summarize: " + text,
            max_length=config["MAX_INPUT_LEN"],
            return_tensors="pt",
            truncation=True
        )

        outputs =  self.model.generate(
            encoded_text,
            max_length=config["MAX_OUTPUT_LEN"],
            min_length=40,
            length_penalty=2.0,
            num_beams=4,
            early_stopping=True)
        
        return self.tokenizer.decode(outputs[0])


transformer = Transformer()


def get_transformer():
    return transformer