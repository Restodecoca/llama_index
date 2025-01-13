from llama_index.core.llms import LLM
from llama_index.multi_modal_llms.gemini import GeminiMultiModal


def test_embedding_class():
    names_of_base_classes = [b.__name__ for b in GeminiMultiModal.__mro__]
    assert LLM.__name__ in names_of_base_classes
