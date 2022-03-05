from Classes.criptografia import Criptografia

string = "ola mundo"

def test_criptografia():
    assert Criptografia.criptografia(string) == "omd luo an"