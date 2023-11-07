from typed_env import *

# Define the variable definition for the following
"""
FOO=bar
FOOBAR=foo${FOO}
FOOBARBAR=${FOOBAR}bar
FOONOTEMPLATE='foo${FOO}'

INT=12
FLOAT=12.34
FLOAT_INT=12
BOOL_TRUE=true
BOOL_FALSE=false
BOOL_TRUE2=True"""

vars = [
    v("FOO", str),
    v("FOOBAR", str),
    v("FOOBARBAR", str),
    v("FOONOTEMPLATE", str),
    v("INT", int),
    v("FLOAT", float),
    v("FLOAT_INT", float),
    v("BOOL_TRUE", bool),
    v("BOOL_FALSE", bool),
    v("BOOL_TRUE2", bool),
]

# Load the environment variables from the file
env, errors = load_env(vars, filename="testing.env", exit_on_error=False)


def test_no_errors():
    assert errors == []


def test_variables_exist():
    for v in vars:
        assert env[v.name] is not None


def test_variables_are_correct_type():
    assert type(env["FOO"]) == str
    assert type(env["FOOBAR"]) == str
    assert type(env["FOOBARBAR"]) == str
    assert type(env["FOONOTEMPLATE"]) == str
    assert type(env["INT"]) == int
    assert type(env["FLOAT"]) == float
    assert type(env["FLOAT_INT"]) == float
    assert type(env["BOOL_TRUE"]) == bool
    assert type(env["BOOL_FALSE"]) == bool
    assert type(env["BOOL_TRUE2"]) == bool


def test_variables_are_correct_value():
    assert env["FOO"] == "bar"
    assert env["FOOBAR"] == "foobar"
    assert env["FOOBARBAR"] == "foobarbar"
    assert env["FOONOTEMPLATE"] == "foo${FOO}"
    assert env["INT"] == 12
    assert env["FLOAT"] == 12.34
    assert env["FLOAT_INT"] == 12.0
    assert env["BOOL_TRUE"] == True
    assert env["BOOL_FALSE"] == False
    assert env["BOOL_TRUE2"] == True

    # assert env["ESCAPING"] == "\t\n\r\\\"$'\u00a9\u263a"


def test_get_methods():
    for v in vars:
        assert env.get(v.name) == env[v.name]
