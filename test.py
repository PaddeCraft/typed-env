from typed_env import *

vars = [
    v("FOO", str),
    v("TEST", int, OPTIONAL),
    v("INT", int),
    v("FLOAT", float),
    v("FLOAT_INT", float),
    v("BOOL_TRUE", bool),
    v("BOOL_FALSE", bool),
    v("BOOL_TRUE2", bool),
]
env = load_env(vars, filename="testing.env")

# print("ENV: ", env)
print("FOO:", env["FOO"])
print("FOOBAR:", env["FOOBAR"])
print("NON_EXIST:", env["NON_EXIST"])
print("FOOBARBAR:", env["FOOBARBAR"])
print("FOONOTEMPLATE: ", env["FOONOTEMPLATE"])

print("INT:", env["INT"])
print("FLOAT:", env["FLOAT"])
print("FLOAT_INT:", env["FLOAT_INT"])
print("BOOL_TRUE:", env["BOOL_TRUE"])
print("BOOL_FALSE:", env["BOOL_FALSE"])
print("BOOL_TRUE2:", env["BOOL_TRUE2"])
