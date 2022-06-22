import pytest
from datetime import datetime
import sys
sys.path.append('C:/repositorio/fase_3/exercicio_1/src/domain')
from enums.genero_enum import Genero
from config.config_atributos import *
from entities.main import Usuario


class TestUsuario:

    def test_instanciar_nome_vazio(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('', 'levi@gmail.com', '3fd4f34', '12312412', datetime(1997, 10, 27), '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_VAZIO

    def test_instanciar_nome_longo(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('a'*101, 'levi@gmail.com', '3fd4f34', '12312412', datetime(1997, 10, 27), '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_LONGO

    def test_instanciar_email_vazio(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', '', '3fd4f34', '123112', datetime(1997, 10, 27), '12131414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_VAZIO

    def test_instanciar_email_longo(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'a'*101, '3fd4f34', '12312412', datetime(1997, 10, 27), '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_LONGO

    def test_instanciar_senha_vazia(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'levi@gmail.com', '', '12312412', datetime(1997, 10, 27), '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_VAZIO

    def test_instanciar_senha_longa(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'levi@gmail.com', 'a'*21, '12312412', datetime(1997, 10, 27), '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_LONGO

    def test_instanciar_celular1_vazio(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'levi@gmail.com', 'sadas98das', '', datetime(1997, 10, 27), '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_VAZIO

    def test_instanciar_celular1_longo(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'levi@gmail.com', 'sadas98d98y', '435435435543', datetime(1997, 10, 27), '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_INVALIDO

    def test_instanciar_celular1_curto(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'levi@gmail.com', 'sadas98d98y', '43543543', datetime(1997, 10, 27), '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_INVALIDO

    def test_instanciar_celular2_longo(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'levi@gmail.com', 'sadas98das', '123124124', datetime(1997, 10, 27), '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_INVALIDO

    def test_instanciar_data_nasc_vazia(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'levi@gmail.com', 'sadas98das', '12233124124', '', '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_VAZIO

    def test_instanciar_data_nasc_invalida(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'levi@gmail.com', 'sadas98das', '12233124124', '1997-10-27', '1213141414','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_INVALIDO

    def test_instanciar_data_nasc_user_menor(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'levi@gmail.com', 'sadas98das', '12233124124', datetime(2012, 10, 27), '1213141414','',Genero.MASCULINO)
        assert str(e.value) == USUARIO_MENOR

    def test_instanciar_cpf_vazio(self) -> None:
        with pytest.raises(Exception) as e:
            Usuario('Levi Gabriel', 'levi@gmail.com', 'sadas98das', '12233124124', datetime(1997, 10, 27), '','',Genero.MASCULINO)
        assert str(e.value) == CAMPO_VAZIO