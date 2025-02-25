"""Tests for ollama parameter conversion"""

import pytest

from dm_ollamalib.optionhelper import help_long, help_overview, to_ollama_options

# Pylint ... ignore missing function docstrings
# pylint: disable = C0116

# Ruff ... PLR2004 ignore magic value comparisons


def test_1param_and_int():
    tests = "num_ctx=8092"
    res = to_ollama_options(tests)
    assert len(res) == 1
    assert res["num_ctx"] == 8092  # noqa: PLR2004
    assert isinstance(res["num_ctx"], int)


def test_multiparam_and_float():
    tests = "top_p=0.9;temperature=0.8"
    res = to_ollama_options(tests)
    assert len(res) == 2  # noqa: PLR2004
    assert res["top_p"] == 0.9  # noqa: PLR2004
    assert res["temperature"] == 0.8  # noqa: PLR2004


def test_iterable():
    tests = ["top_p=0.9", "temperature=0.8"]
    res = to_ollama_options(tests)
    assert len(res) == 2  # noqa: PLR2004
    assert res["top_p"] == 0.9  # noqa: PLR2004
    assert res["temperature"] == 0.8  # noqa: PLR2004


def test_bool():
    tests = "low_vram=true;logits_all=FALSE"
    res = to_ollama_options(tests)
    assert len(res) == 2  # noqa: PLR2004
    assert res["low_vram"] is True
    assert res["logits_all"] is False
    assert isinstance(res["low_vram"], bool)


def test_lststr():
    tests = "stop=2;stop=blubb"
    res = to_ollama_options(tests)
    assert len(res) == 1
    assert res["stop"] == ["2", "blubb"]
    assert isinstance(res["stop"], list) and isinstance(res["stop"][0], str)


# no str parameters in Ollama atm
# def test_str():

# test edge cases


def test_empty():
    to_ollama_options("")
    to_ollama_options("   ")
    to_ollama_options(";  ;")


# tests for help strings
# As difficult to check 'correctness', just check whether
#  num_ctx is present ... will probably be there forever


def test_help_overview():
    s = help_overview()
    assert "num_ctx : int" in s


def test_help_long():
    s = help_long()
    assert "num_ctx : int" in s


# test expected failures


@pytest.mark.parametrize(
    "parameterstr",
    [
        ("ThisParamDoesNotExist=1024"),  # d'oh
        ("low_vram"),  # no =
        ("low_vram=True=Ooops"),  # too many =
        ("lowvram="),  # no value
        ("=1024"),  # no parameter name
        ("low_vram=rue"),  # bool error
        ("num_ctx=0x8000"),  # int error
        ("top_p=0.9x"),  # float error
    ],
)
def test_paramvalerror(parameterstr):
    with pytest.raises(ValueError):
        to_ollama_options(parameterstr)


def test_paramtypeerror():
    tests = 5
    with pytest.raises(TypeError):
        to_ollama_options(tests)
