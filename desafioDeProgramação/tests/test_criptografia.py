from Classes.criptografia import Criptografia

string = "ola mundo"
#string2 = "tenha um bom dia"


def test_criptografia():
    assert Criptografia.criptografia(string) == "omd luo an"
    #assert Criptografia.criptografia(string2) == "taoa eum nmd hbi"

