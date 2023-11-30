import json
from pprint import pprint

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

oai_client = OpenAI()
print(oai_client.api_key)

word = "発行"

prompt = """Please write a simple sentence in Japanese which uses the word {word}.
Avoid using uncommon words.
Return the sentence as a JSON object.
It should contain the following keys:
'sentence' - should contain sentence itself.
'with_furigana' - should contain the sentence with furigana in square brackets added to all kanji.
    There should be a space before kanji in this version.
    Don't add furigana for katakana.
    Don't add furigana for hiragana.
'translation' - should contain English translation of the sentence.
"""

chat_completion = oai_client.chat.completions.create(
    messages=[{"role": "user", "content": prompt.format(word=word)}],
    model="gpt-4-1106-preview",
    response_format={"type": "json_object"},
)

choice = chat_completion.choices[0]
assert choice.finish_reason == "stop"
d_ = json.loads(choice.message.content)
pprint(d_)
