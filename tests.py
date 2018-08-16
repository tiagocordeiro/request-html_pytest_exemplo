import pytest
from app import get_ulr_links


def test_response_code_200():
    response = get_ulr_links('https://www.mulhergorila.com')
    assert response.status_code == 200

def test_contact_link_in_home():
    response = get_ulr_links('https://www.mulhergorila.com')
    assert 'https://www.mulhergorila.com/contato/' in response.html.links

def test_if_is_form_in_contact_page():
    response = get_ulr_links('https://www.mulhergorila.com/contato/')
    form = response.html.find('#gform_1', first=True)
    assert 'Nome*\nE-mail*\nTelefone\nMensagem*' == form.text
