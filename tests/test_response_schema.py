from crew.response_schema import StructuredResponse
from crew.response_validator import ResponseValidator


def test_structured_response_to_dict_defaults():
    response = StructuredResponse(
        type="historical_facts",
        query="Quantas Copas o Brasil venceu?",
        answer="O Brasil venceu cinco Copas do Mundo.",
        main_facts=["Brasil e pentacampeao"],
    )

    payload = response.to_dict()

    assert payload["type"] == "historical_facts"
    assert payload["related_topics"] == []
    assert payload["sources"] == []
    assert payload["metadata"] == {}


def test_response_validator_accepts_valid_structured_payload():
    payload = {
        "type": "general_info",
        "query": "Quem venceu a Copa de 2002?",
        "answer": "O Brasil venceu a Copa do Mundo de 2002, disputada na Coreia do Sul e no Japao.",
        "main_facts": ["Brasil campeao", "Final contra a Alemanha"],
    }

    is_valid, message = ResponseValidator.validate_structured_response(payload)

    assert is_valid is True
    assert message in {"Valido", "Válido"}
